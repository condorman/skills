#!/usr/bin/env python3
"""
Deep Search Miner Helper Script for idea-discovery skill.
Generates vertical Google Dork search matrices, queries public APIs/registries,
and structures prior-art verification audit logs.
"""

import sys
import json
import urllib.parse

def generate_search_matrix(core_mechanic, domain="all"):
    encoded_mech = urllib.parse.quote(core_mechanic)
    
    matrix = {
        "core_mechanic": core_mechanic,
        "dorks": {
            "app_store_ios": f'site:apps.apple.com "{core_mechanic}"',
            "google_play": f'site:play.google.com/store/apps "{core_mechanic}"',
            "steam_store": f'site:store.steampowered.com/app "{core_mechanic}"',
            "steam_db": f'site:steamdb.info "{core_mechanic}"',
            "github_topics": f'site:github.com/topics "{core_mechanic}"',
            "product_hunt": f'site:producthunt.com/posts "{core_mechanic}"',
            "canny_boards": f'site:canny.io "{core_mechanic}"',
            "google_patents": f'https://patents.google.com/?q={encoded_mech}',
            "arxiv_papers": f'https://arxiv.org/search/?query={encoded_mech}&searchtype=all',
            "reddit_workarounds": f'site:reddit.com "{core_mechanic}" ("manual workflow" OR "workaround")',
            "upwork_jobs": f'site:upwork.com "{core_mechanic}" ("script" OR "automation")',
            "japanese_booth": f'site:booth.pm "{core_mechanic}"'
        },
        "search_urls": {
            "google_dork_combined": f'https://www.google.com/search?q={urllib.parse.quote(f"site:apps.apple.com OR site:store.steampowered.com OR site:producthunt.com {core_mechanic}")}',
            "google_patents_direct": f'https://patents.google.com/?q={encoded_mech}',
            "arxiv_direct": f'https://arxiv.org/search/?query={encoded_mech}&searchtype=all'
        }
    }
    return matrix

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: python deep_search_miner.py '<core_mechanic>' [domain]"}, indent=2))
        sys.exit(1)
        
    core_mechanic = sys.argv[1]
    domain = sys.argv[2] if len(sys.argv) > 2 else "all"
    
    result = generate_search_matrix(core_mechanic, domain)
    print(json.dumps(result, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
