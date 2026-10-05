#!/usr/bin/env python3
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
src = ROOT / 'data' / 'game-data.json'
out = ROOT / 'data' / 'game-data.js'
data = json.loads(src.read_text(encoding='utf-8'))
if data.get('schemaVersion') != 2:
    raise RuntimeError('Unsupported game-data schema')
if not isinstance(data.get('droids'), list) or not isinstance(data.get('fusionRecipes'), list):
    raise RuntimeError('game-data.json is missing droids or fusionRecipes')
browser = {
    'schemaVersion': data['schemaVersion'],
    'droids': data['droids'],
    'fusion': data['fusionRecipes'],
    'nova': data.get('nova', {}),
}
out.write_text('window.KYBER_GAME_DATA=' + json.dumps(browser, separators=(',', ':')) + ';\n', encoding='utf-8')
print(f'Built {out.relative_to(ROOT)}: {len(browser["droids"])} droids, {len(browser["fusion"])} fusion recipes')
