#!/usr/bin/env python3
"""
Deep Search Miner Helper Script for idea-discovery skill.
Generates vertical Google Dork search matrices, queries public APIs/registries,
and structures prior-art verification audit logs.
"""

import sys
import json
import urllib.parse


# Every dork is tagged with the domain(s) it's relevant for. "all" dorks always run;
# a domain-specific dork only runs when it matches the requested domain (or when
# domain="all", in which case everything runs). This keeps the search surface
# proportionate: a mobile calculator app doesn't need Steam/BOOTH dorks, and a
# non-technical SaaS idea doesn't need a patent/arXiv pass unless it's flagged novel.
ALL_DOMAINS = {"mobile", "games", "saas", "web", "ai_tools"}

def generate_search_matrix(core_mechanic, domain="all", include_deep_tech=False):
    if domain != "all" and domain not in ALL_DOMAINS:
        raise ValueError(f"Unknown domain '{domain}'. Expected one of: all, {', '.join(sorted(ALL_DOMAINS))}")

    encoded_mech = urllib.parse.quote(core_mechanic)

    # (dork_key, dork_string, applicable_domains) — "all" means every domain.
    dork_defs = [
        ("app_store_ios", f'site:apps.apple.com "{core_mechanic}"', {"mobile"}),
        ("google_play", f'site:play.google.com/store/apps "{core_mechanic}"', {"mobile"}),
        ("steam_store", f'site:store.steampowered.com/app "{core_mechanic}"', {"games"}),
        ("steam_db", f'site:steamdb.info "{core_mechanic}"', {"games"}),
        ("japanese_booth", f'site:booth.pm "{core_mechanic}"', {"games"}),
        ("github_topics", f'site:github.com/topics "{core_mechanic}"', {"saas", "web", "ai_tools"}),
        ("product_hunt", f'site:producthunt.com/posts "{core_mechanic}"', "all"),
        ("canny_boards", f'site:canny.io "{core_mechanic}"', {"saas", "web", "ai_tools"}),
        ("reddit_workarounds", f'site:reddit.com "{core_mechanic}" ("manual workflow" OR "workaround")', "all"),
        ("upwork_jobs", f'site:upwork.com "{core_mechanic}" ("script" OR "automation")', {"saas", "web", "ai_tools"}),
    ]

    dorks = {
        key: dork for key, dork, applies_to in dork_defs
        if applies_to == "all" or domain == "all" or domain in applies_to
    }

    # Patent/academic prior-art search is expensive relative to its yield for
    # ordinary CRUD/utility ideas — only include it when the mechanism has been
    # flagged as technically novel (i.e. it's a real Proof 7 candidate).
    if include_deep_tech:
        dorks["google_patents"] = f'https://patents.google.com/?q={encoded_mech}'
        dorks["arxiv_papers"] = f'https://arxiv.org/search/?query={encoded_mech}&searchtype=all'

    matrix = {
        "core_mechanic": core_mechanic,
        "domain": domain,
        "include_deep_tech": include_deep_tech,
        "dorks": dorks,
        "search_urls": {
            "google_dork_combined": f'https://www.google.com/search?q={urllib.parse.quote(f"site:apps.apple.com OR site:store.steampowered.com OR site:producthunt.com {core_mechanic}")}',
        }
    }
    if include_deep_tech:
        matrix["search_urls"]["google_patents_direct"] = f'https://patents.google.com/?q={encoded_mech}'
        matrix["search_urls"]["arxiv_direct"] = f'https://arxiv.org/search/?query={encoded_mech}&searchtype=all'

    return matrix

# Consumer ideas and B2B ideas have different DIY/status-quo tiers and different
# review surfaces. Feeding Zapier/Notion/G2 dorks to a consumer app idea (or
# TikTok dorks to an accounting tool) burns queries and returns nothing, so the
# deep-dive matrix branches on this rather than emitting one generic set.
CONSUMER_DOMAINS = {"mobile", "games"}


def _keywordize(topic, max_words=3):
    """Reduce a topic phrase to its most searchable short form.

    A deep-dive topic is usually written as a description ("watermelon ripeness
    acoustic tap"), and quoting that whole string inside a dork matches almost
    nothing — no page contains that exact phrase. Search engines want the two or
    three content words the market actually uses, so the long form is kept only
    where a broad match helps and the short form is used inside quotes.
    """
    stop = {"a", "an", "the", "for", "with", "using", "via", "and", "or", "of", "to", "app", "tool"}
    words = [w for w in topic.replace("-", " ").split() if w.lower() not in stop]
    return " ".join(words[:max_words]) if words else topic


def generate_deepdive_matrix(topic, domain="all"):
    """Query matrix for Vertical Deep-Dive Mode (see references/vertical_deepdive_playbook.md).

    Discovery mode asks "does prior art exist?" and stops at the two closest hits.
    A deep-dive asks "who is ALL of the prior art, what do their users hate, which
    of them are already dead, and what does the lab literature say the method can
    actually do?" — a different search surface, so it gets its own matrix. Grouped
    by deep-dive step so the output maps onto the report sections it feeds.
    """
    if domain != "all" and domain not in ALL_DOMAINS:
        raise ValueError(f"Unknown domain '{domain}'. Expected one of: all, {', '.join(sorted(ALL_DOMAINS))}")

    kw = _keywordize(topic)
    consumer = domain in CONSUMER_DOMAINS or domain == "all"
    business = domain not in CONSUMER_DOMAINS or domain == "all"

    store_dorks = {
        "mobile": [f'site:apps.apple.com "{kw}"', f'site:play.google.com/store/apps "{kw}"'],
        "games": [f'site:store.steampowered.com/app "{kw}"', f'site:itch.io "{kw}"'],
        "saas": [f'site:g2.com "{kw}"', f'site:capterra.com "{kw}"'],
        "web": [f'site:chromewebstore.google.com "{kw}"', f'site:producthunt.com/posts "{kw}"'],
        "ai_tools": [f'site:producthunt.com/posts "{kw}"', f'site:github.com/topics "{kw}"'],
    }
    domain_census = []
    for dom, queries in store_dorks.items():
        if domain in ("all", dom):
            domain_census.extend(queries)

    # Tier 3 of the census: what people do instead of buying anything. For a
    # consumer product that's a YouTube tutorial or a household trick; for a
    # business one it's a spreadsheet and a Zapier recipe. Rarely both.
    diy_tier = []
    if consumer:
        diy_tier += [
            f'site:youtube.com "how to" {kw}',
            f'site:reddit.com "{kw}" "trick" OR "hack" OR "old way"',
            f'"how to tell" {kw} without app',
        ]
    if business:
        diy_tier += [
            f'"{kw}" template site:notion.so OR site:airtable.com',
            f'"{kw}" site:zapier.com OR site:make.com OR site:n8n.io',
            f'site:reddit.com "{kw}" spreadsheet OR "google sheet"',
        ]

    complaint_dorks = [
        f'site:reddit.com "{kw}" (frustrating OR "doesn\'t work" OR inaccurate)',
        f'"{kw}" app review "not accurate" OR "waste of money"',
    ]
    if business:
        complaint_dorks.append(f'site:github.com "{kw}" label:wontfix OR label:stale')
    if consumer:
        complaint_dorks.append(f'site:youtube.com "{kw}" test OR "does it work"')

    return {
        "mode": "vertical_deepdive",
        "topic": topic,
        "search_keyword": kw,
        "domain": domain,
        "audience": "consumer" if (consumer and not business) else ("business" if business and not consumer else "mixed"),
        # D1 — census. The point is enumeration, not confirmation: aggregators and
        # vendors' own comparison pages name rivals a first-pass search never surfaces.
        "d1_competitor_census": {
            "aggregators": [
                f'site:alternativeto.net "{kw}"',
                f'"best {kw} apps" 2026',
                f'"{kw} alternatives"',
            ],
            "community_enumeration": [
                f'site:reddit.com "what do you use for" {kw}',
                f'site:news.ycombinator.com "{kw}"',
            ],
            "diy_status_quo_tier": diy_tier,
            "domain_stores": domain_census,
        },
        # D1 tier 5 — instrumented baseline. Only meaningful for sensor/accuracy ideas,
        # but there it is decisive: a 95% figure from a laser vibrometer says nothing
        # reassuring about a phone microphone.
        "d1_instrumented_baseline": {
            "note": "Run these when the idea infers a physical property from a sensor or claims an accuracy threshold. Compare instrument to instrument, not number to number.",
            "queries": [
                f'"{kw}" accuracy site:pmc.ncbi.nlm.nih.gov OR site:doaj.org',
                f'"{kw}" classification accuracy site:arxiv.org',
                f'"{kw}" sensor OR spectrometer OR vibrometer detection accuracy study',
            ],
        },
        # D2 — voice of customer, plus the higher-grade independent tests.
        "d2_voice_of_customer": {
            "churn_threads": [
                f'site:reddit.com "switched from" "{kw}"',
                f'"why I left" OR "moving away from" "{kw}"',
            ],
            "complaint_mining": complaint_dorks,
            "independent_tests": [
                f'"{kw}" "we tested" OR "hands on" OR "does it actually work"',
                f'"{kw}" test comparison consumer association OR university OR institute',
            ],
            "unmet_requests": [
                f'site:canny.io "{kw}"',
                f'"{kw}" "feature request" -site:twitter.com',
            ] if business else [
                f'"{kw}" "wish the app" OR "app should"',
            ],
        },
        # D4 — graveyard. Two independent deaths from the same structural cause is a
        # category property, not bad luck; these queries are how that gets found.
        "d4_graveyard": {
            "shutdown_signals": [
                f'"{kw}" "shutting down" OR "sunset" OR "discontinued"',
                f'"{kw}" post-mortem OR postmortem startup',
                f'site:reddit.com "whatever happened to" "{kw}"',
                f'site:github.com "{kw}" archived',
            ],
        },
        # D5 — economics. Observed prices beat assumed ones; a free incumbent tier
        # caps pricing power far below whatever the value story suggests.
        "d5_revenue_signals": {
            "pricing_reality": [
                f'"{kw}" pricing OR "per month" OR "one-time purchase"',
                f'"{kw}" "free plan" OR "free tier" limits',
            ],
            "audience_sizing": [
                f'site:reddit.com "{kw}" community members',
                f'"{kw}" "how many" users OR professionals statistics',
            ],
            "seasonality": [
                f'"{kw}" seasonal demand OR "google trends"',
            ],
        },
        # D6 — legal, EU-first (see legal_risk_playbook.md + playbook D6).
        "d6_legal_surfaces": {
            "queries": [
                f'"{kw}" GDPR personal data requirements',
                f'"{kw}" "EU AI Act" transparency obligations',
                f'"{kw}" terms of service "automated access" OR scraping prohibited',
                f'"{kw}" App Store review guidelines rejection',
                f'"{kw}" misleading advertising claim consumer protection',
            ],
        },
        "non_english_pass": {
            "note": "Run the census again in the target market's language plus one large software market — whole categories are mature in one language and invisible in another, and local press tests often exist only there.",
            "suggested_locales": ["it", "de", "es", "fr", "ja", "zh"],
        },
        "depth_contract_reminder": {
            "min_competitors": 8,
            "min_vocabularies": 3,
            "min_voc_sources": 15,
            "min_dead_products_investigated": 2,
            "note": "Every entry must come from a real tool call. Tag each pain as product-specific or category-inherent — category-inherent pains are evidence against the category, never a wedge.",
        },
    }


# ---------------------------------------------------------------------------
# Anchored mining (Step 1, Original Discovery Mode)
# ---------------------------------------------------------------------------
# Mining queries built out of adjectives -- "wastes time", "manual workaround",
# "abandoned", "frustrating" -- reliably return content marketing and infoproduct
# funnels, because those are the exact words vendors optimise for. The queries
# that actually surface unserved friction are anchored to a *dated, checkable
# fact*: a regulation with a compliance date, a platform policy change with a
# cutoff, a feature request with a vote count and an age, a published rate card,
# a tender document. An anchor can be verified in one click and cannot be
# manufactured by a marketing team; an adjective can be both.
#
# Rule of thumb when reading the output: if a query result can't be traced back
# to a document with a date on it, it is not evidence.

LOCALES = {
    "en": {
        "in_force": '"comes into force" OR "compliance deadline"',
        "obligation": '"are required to" OR "must comply"',
        "small_business": '"small business" OR SME',
        "price_increase": '"price increase" OR "raising prices"',
        "is_there_a_tool": '"is there a tool that" OR "is there an app that"',
        "what_do_you_use": '"what do you use for"',
        "tender": 'tender OR "request for proposal" specification',
        "still_manual": '"still done by hand" OR "still on paper"',
        "sites": "",
    },
    "it": {
        "in_force": '"entra in vigore" OR "a decorrere dal" OR "obbligo dal"',
        "obligation": '"sono tenuti a" OR "adempimento obbligatorio"',
        "small_business": '"piccole imprese" OR PMI OR artigiani',
        "price_increase": '"aumento dei prezzi" OR "rincaro" OR "nuovo listino"',
        "is_there_a_tool": '"esiste un software che" OR "esiste un gestionale per"',
        "what_do_you_use": '"che programma usate per" OR "che gestionale usate"',
        "tender": 'bando OR capitolato OR "avviso pubblico"',
        "still_manual": '"ancora a mano" OR "ancora su carta" OR "con Excel"',
        "sites": "site:.it",
    },
}


def generate_anchor_mining_matrix(sector, domain="all", locale="en"):
    """Anchored candidate-mining queries for Step 1 of Original Discovery Mode.

    `sector` is the field being mined ("electrical contractors", "importatori
    di caffe'", "dental labs") -- not a product idea. The point of this stage is
    to find the friction before naming the product, so the queries describe who
    the people are and what dated obligation or change is landing on them.
    """
    if domain != "all" and domain not in ALL_DOMAINS:
        raise ValueError(f"Unknown domain '{domain}'. Expected one of: all, {', '.join(sorted(ALL_DOMAINS))}")
    if locale not in LOCALES:
        raise ValueError(f"Unknown locale '{locale}'. Expected one of: {', '.join(sorted(LOCALES))}")

    L = LOCALES[locale]
    s = _keywordize(sector, max_words=4)
    site = f" {L['sites']}" if L["sites"] else ""

    return {
        "mode": "anchor_mining",
        "sector": sector,
        "search_keyword": s,
        "domain": domain,
        "locale": locale,
        "principle": (
            "Every candidate must trace to a document with a date on it. Adjective-based "
            "queries ('wastes hours', 'hacky workaround') return SEO content and Gumroad "
            "funnels; anchor-based queries return the obligation, the policy, the vote "
            "count or the price list that created the friction."
        ),
        # A regulation with a compliance date is the strongest anchor there is: the
        # demand has a deadline attached, the affected population is defined by law,
        # and the "why now" writes itself.
        "a_regulatory_deadlines": [
            f'{s} {L["in_force"]} 2026 OR 2027{site}',
            f'{s} {L["obligation"]} {L["small_business"]}{site}',
            f'{s} "due diligence" OR dichiarazione OR declaration obligation deadline{site}',
            f'{s} adempimenti OR compliance checklist scadenze{site}',
        ],
        # Platform policy changes (store rules, API deprecations, mandated formats)
        # move whole categories on a fixed date and are published, not rumoured.
        "b_platform_policy_changes": [
            f'{s} "target API level" OR "app store guidelines" change deadline',
            f'{s} API deprecation OR "sunset" developers must migrate 2026',
            f'{s} mandatory format OR e-invoicing OR interoperability requirement 2026',
        ],
        # A feature request with votes and an age is demand that has already been
        # counted by someone else, on the record.
        "c_unmet_feature_requests": [
            f'site:canny.io {s}',
            f'site:featurebase.app OR site:productboard.com {s}',
            f'site:github.com {s} "feature request" label:wontfix OR label:stale',
            f'{s} roadmap "not planned" OR "won\'t fix" votes',
        ],
        # Published prices and rate cards: proof money already moves, and how much.
        "d_money_already_moving": [
            f'{s} {L["price_increase"]} 2026{site}',
            f'{s} "tariffario" OR "rate card" OR "listino" consulenza{site}',
            f'site:upwork.com OR site:fiverr.com {s} automation recurring',
            f'{s} {L["tender"]} software{site}',
        ],
        # Practitioner-to-practitioner threads, but phrased as enumeration rather
        # than complaint -- "what do you use" lists real tools, "I waste hours"
        # lists blog posts.
        "e_practitioner_enumeration": [
            f'site:reddit.com {L["what_do_you_use"]} {s}',
            f'{L["is_there_a_tool"]} {s}{site}',
            f'{s} forum {L["still_manual"]}{site}',
        ],
        "usage_note": (
            "These five families are a menu, not a checklist. Run the ones that plausibly "
            "apply to this sector and say which you skipped and why -- the platform-policy "
            "family is irrelevant to a coffee importer, the tender family to a consumer app. "
            "A padded sweep that ran everything is worth less than three anchored hits."
        ),
        "anti_patterns": [
            "Do NOT run: '<sector> wastes hours per week' -- returns vendor content marketing.",
            "Do NOT run: '<sector> manual workaround' -- returns infoproduct and template funnels.",
            "Do NOT accept a candidate whose only evidence is a listicle or a tool vendor's blog.",
        ],
        "locale_note": (
            "For a market-specific idea, run these in the market's language first. "
            "An English-only sweep of an Italian, German or Spanish B2B niche systematically "
            "misses both the incumbents and the regulation that created the demand."
        ),
    }


def generate_flanking_matrix(target, domain="all", locale="en"):
    """Candidate mining + eligibility evidence for Flanking Discovery Mode.

    `target` is either a named product being assessed, or the category being
    swept for vulnerable incumbents. Queries are grouped by the evidence bar each
    pattern in flanking_playbook.md demands, so the output maps onto the gate.
    """
    if locale not in LOCALES:
        raise ValueError(f"Unknown locale '{locale}'. Expected one of: {', '.join(sorted(LOCALES))}")
    t = _keywordize(target, max_words=4)

    return {
        "mode": "flanking",
        "target": target,
        "search_keyword": t,
        "domain": domain,
        "locale": locale,
        "principle": (
            "'Looks neglected' is an impression. The gate wants three dated facts per "
            "candidate: traction that existed, maintenance that stopped, and demand that "
            "didn't. Check the store listing and the target API level before anything else."
        ),
        # Pattern 1 -- abandoned but proven. The complaint pattern is what separates a
        # dead app from a finished one; a stable utility with no updates is not a target.
        "p1_abandonment_evidence": [
            f'"{t}" "no longer maintained" OR "last update" OR abandoned',
            f'site:reddit.com "is {t} still maintained" OR "{t} died"',
            f'"{t}" reviews crash OR broken OR "support never replied" 2026',
            f'site:github.com "{t}" archived',
        ],
        # The platform is now doing part of the displacement for you -- and removing
        # part of the prize at the same time. Check this BEFORE valuing the target.
        "p1_platform_visibility_window": {
            "note": (
                "Google Play: apps not meeting the current target API level stop being "
                "discoverable to new users on newer Android versions. An abandoned app is "
                "therefore losing its ranking inertia on a schedule you can look up -- which "
                "makes displacement easier AND makes the vacancy visible to every other "
                "builder at the same time. Record the target API level and the applicable "
                "cutoff date alongside the last-update date."
            ),
            "queries": [
                'site:support.google.com "target API level requirements" Google Play',
                f'"{t}" targetSdkVersion OR "target API" site:apkmirror.com OR site:apkcombo.com',
            ],
        },
        # Pattern 2 -- stagnant. Changelogs and vote-aged requests, not vibes.
        "p2_stagnation_evidence": [
            f'"{t}" changelog OR "release notes" 2025 2026',
            f'site:canny.io "{t}"',
            f'"{t}" "feature request" votes "still not" OR "years"',
        ],
        # Pattern 3 -- good foundation, sourced gap. Needs 3+ independent complaints.
        "p3_gap_corroboration": [
            f'"{t} alternative because" OR "switched from {t}"',
            f'site:g2.com OR site:capterra.com "{t}" 2 star OR 3 star review',
            f'site:reddit.com "{t}" "the only thing missing" OR "wish it could"',
        ],
        # The gate's second check, made searchable: is the dissatisfied cohort still
        # unserved, or did a fork/competitor already absorb it?
        "gate_displacement_feasibility": [
            f'"{t}" fork OR successor OR "picks up where"',
            f'"best {t} alternatives" 2026',
            f'"{t}" alternative site:alternativeto.net',
        ],
        "disqualifiers": [
            "Death caused by a platform/API policy (third-party clients of a closed platform) "
            "is structural, not abandonment -- the cause of death is inherited by any rebuild.",
            "A free, credible successor already shipped (especially an open-source fork by an "
            "original contributor) means the dissatisfied cohort is already captured: gate FAIL.",
            "A stable, finished utility with old updates but no complaint pattern is not abandoned.",
        ],
    }


def main():
    if len(sys.argv) < 2:
        print(json.dumps({
            "error": "Usage: python deep_search_miner.py '<topic>' [domain] [--mining|--deepdive|--flanking] [--deep-tech] [--locale=xx]",
            "domains": sorted(ALL_DOMAINS | {"all"}),
            "locales": sorted(LOCALES),
            "flags": {
                "--mining": "emits anchored candidate-mining queries for Step 1 (topic = the sector being mined, not a product)",
                "--deepdive": "emits the Vertical Deep-Dive matrix (census / VoC / graveyard / revenue / legal)",
                "--flanking": "emits Flanking pattern-evidence and eligibility-gate queries (topic = target product or category)",
                "--deep-tech": "adds the Patent/arXiv pass to the prior-art matrix (only for genuinely novel mechanisms)",
                "--locale=it": "emit market-language query fragments; default en. Run the market's language first for local B2B niches.",
            }
        }, indent=2))
        sys.exit(1)

    core_mechanic = sys.argv[1]
    rest = sys.argv[2:]
    include_deep_tech = "--deep-tech" in rest
    deepdive = "--deepdive" in rest
    mining = "--mining" in rest
    flanking = "--flanking" in rest
    locale = "en"
    for a in rest:
        if a.startswith("--locale="):
            locale = a.split("=", 1)[1]
    rest = [a for a in rest if not a.startswith("--")]
    domain = rest[0] if rest else "all"

    try:
        if mining:
            result = generate_anchor_mining_matrix(core_mechanic, domain, locale)
        elif flanking:
            result = generate_flanking_matrix(core_mechanic, domain, locale)
        elif deepdive:
            result = generate_deepdive_matrix(core_mechanic, domain)
        else:
            result = generate_search_matrix(core_mechanic, domain, include_deep_tech)
    except ValueError as e:
        print(json.dumps({"error": str(e)}, indent=2))
        sys.exit(1)

    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
