# KYBER-TOOL

Droid Tycoon companion app.

## Data architecture v2

- `data/game-data.json` is the canonical game-data database.
- `data/game-data.js` is generated from the canonical JSON for the static browser app.
- `scripts/build_game_data_js.py` regenerates the browser data file.
- `scripts/validate_game_data.py` protects the verified blueprint and mission baseline and validates core data.
- `data/live-data.json` remains separate for changing live information such as the Sandcrawler Limited Deal.

The UI is intentionally kept separate from the data/update layer. Verified timer mechanics are preserved and are not silently overwritten by automated game-data updates.
