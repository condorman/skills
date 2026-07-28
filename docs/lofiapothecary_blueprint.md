# Technical Architecture Blueprint: LofiApothecary AI

### 💡 LofiApothecary AI: Audio-Visual ASMR Soundscape Crafting & Cozy Nook Studio

**Target Platform**: iOS & Android Native (Flutter / React Native Expo)  
**Architecture Pattern**: Offline-First Local Reactive State + Native WebAudio/FMOD Stem Engine + iOS Live Activities / Dynamic Island Background Audio System

---

## 1. System Architecture Diagram

```mermaid
graph TD
    subgraph Mobile Client (iOS / Android)
        UI[Cozy 2.5D Room & Tea Crafting UI - Rive/Canvas]
        Store[State Manager - Zustand / Riverpod]
        DB[(Local SQLite Database - Recipes, Decor, Inventory)]
        
        subgraph Audio Core Engine
            Mixer[WebAudio / FMOD Stem Audio Engine]
            Stems[Spatial Audio Stems: Rain, Fire, Teapot, Lofi Synth, Vinyl]
        end
        
        subgraph Native System Integration
            LiveAct[iOS Live Activities & Dynamic Island Controller]
            BackgroundAudio[Native Background Audio Session Handler]
            WidgetEngine[Lock Screen Pomodoro & Soundscape Widget]
        end
    end
    
    subgraph On-Device / Cloud AI Layer
        LLM[Local Procedural Visitor Dialogue & Mood Generator]
    end

    UI --> Store
    Store --> DB
    Store --> Mixer
    Mixer --> Stems
    Mixer --> BackgroundAudio
    BackgroundAudio --> LiveAct
    BackgroundAudio --> WidgetEngine
    Store --> LLM
```

---

## 2. Database Schema (SQLite / WatermelonDB / Supabase SQL)

```sql
-- Inventory of botanical ingredients and audio stems
CREATE TABLE IF NOT EXISTS botanical_ingredients (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    category TEXT CHECK (category IN ('tea_leaf', 'flower', 'herb', 'spice', 'sweetener')),
    stem_audio_path TEXT NOT NULL, -- Path to 24-bit seamless WAV/OGG loop
    visual_asset_path TEXT NOT NULL,
    base_notes TEXT NOT NULL, -- e.g. "Floral, Earthy, Spicy"
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Player unlocked decor and room themes
CREATE TABLE IF NOT EXISTS room_decor (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    slot_type TEXT CHECK (slot_type IN ('window_weather', 'fireplace', 'radio', 'plant', 'lighting', 'desk')),
    ambient_stem_path TEXT, -- e.g. rain_on_tin.ogg, fire_crackle.ogg
    visual_asset_path TEXT NOT NULL,
    is_unlocked BOOLEAN DEFAULT FALSE
);

-- Tea Recipes and Soundscape Formulas
CREATE TABLE IF NOT EXISTS tea_recipes (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    description TEXT NOT NULL,
    required_ingredients JSON NOT NULL, -- Array of ingredient_ids
    target_mood TEXT NOT NULL, -- e.g. "Study Focus", "Deep Sleep", "Anxiety Relief"
    default_lofi_stem TEXT NOT NULL,
    reward_coins INTEGER DEFAULT 50
);

-- Active User Custom Soundscapes & Pomodoro Presets
CREATE TABLE IF NOT EXISTS custom_soundscapes (
    id TEXT PRIMARY KEY,
    title TEXT NOT NULL,
    stem_volumes JSON NOT NULL, -- e.g. {"rain": 0.8, "fire": 0.4, "chamomile_pour": 0.6, "lofi_keys": 0.5}
    pomodoro_duration_minutes INTEGER DEFAULT 25,
    is_favorite BOOLEAN DEFAULT FALSE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

---

## 3. Core API & Sound Engine Data Contracts

### 3.1 WebAudio Stem Mixer Interface
```typescript
interface AudioStem {
  id: string;
  category: 'weather' | 'botanical' | 'utensil' | 'music' | 'ambient';
  filePath: string;
  volume: number; // 0.0 to 1.0
  pan: number; // -1.0 to 1.0 (spatial balance)
  isLooping: boolean;
}

interface SoundscapeState {
  activeStems: Map<string, AudioStem>;
  masterVolume: number;
  isBackgroundPlaybackActive: boolean;
  currentTargetMood: string | null;
  pomodoroTimerRemainingSeconds: number;
}
```

### 3.2 Dynamic Island & Lock Screen Sync Contract
```typescript
interface LiveActivityPayload {
  recipeTitle: string;
  activeMood: string;
  timerRemainingFormatted: string; // e.g. "18:45"
  isPaused: boolean;
  activeStemCount: number;
}
```

---

## 4. UI/UX Hierarchy & Aesthetic Color Tokens

### 4.1 Palette Tokens (Cozy Nocturnal Palette)
- **Background Primary**: `#1E1B2E` (Deep Midnight Plum)
- **Surface Elevation**: `#2D2845` (Warm Lavender Slate)
- **Accent Gold (Tea Honey)**: `#E6AF2E` (Warm Glowing Amber)
- **Botanical Sage**: `#6B8E23` (Soft Herbal Green)
- **Text Primary**: `#F4F1DE` (Warm Cream Linen)
- **Subtle Muted**: `#9A8C98` (Dusty Lilac Gray)

### 4.2 Key Screens Hierarchy
1. **The Teahouse Sanctuary (Main Screen)**:
   - 2.5D interactive cozy window view (rain/snow/sunshine toggle).
   - Steeping station with drag-and-drop botanicals into glass teapots.
   - Live ASMR audio stem volume sliders styled as antique brass knobs.
2. **Visitor Order Book**:
   - Nocturnal visitors arriving with subjective mood requests & stories.
   - Recipe matching visual feedback + steeping timer.
3. **Soundscape Studio & Pomodoro Companion**:
   - Soundscape preset saver + export audio stems.
   - Pomodoro focus session launcher + background Lock Screen integration.
4. **Nook Decorator**:
   - Decorate window sills, wallpapers, fireplaces, and lofi radios.

---

## 5. Day 1 - Day 14 Solopreneur MVP Implementation Roadmap

- **Days 1–3 (Core Audio & Visual Engine)**:
  - Setup Expo / Flutter project with WebAudio / FMOD multi-stem engine.
  - Implement seamless stem looping, volume cross-fading, and spatial pan control for 8 stems.
- **Days 4–6 (Teahouse Crafting & Inventory System)**:
  - Create local SQLite database with initial 15 botanical ingredients, 10 tea recipes, and 8 decor items.
  - Build drag-and-drop steeping station UI with Rive interactive animations.
- **Days 7–8 (Visitor Procedural System & Pomodoro Timer)**:
  - Implement offline visitor arrival queue with procedural mood-request text templates.
  - Integrate 25-minute Pomodoro focus timer linked to active soundscape steeping.
- **Days 9–10 (iOS Live Activities & Dynamic Island Integration)**:
  - Write native iOS Swift module for Live Activities background audio session sync.
  - Connect Lock Screen widget controls (Play/Pause, Soundscape volume).
- **Days 11–12 (Polish, Sound Balancing & Launch)**:
  - Master audio stems for zero distortion across iPhone & Android speakers / AirPods.
  - Generate App Store screenshots, viral ASMR TikTok demo videos, and submit for review.
