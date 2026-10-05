#!/usr/bin/env python3
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
p=ROOT/'data/game-data.json'
d=json.loads(p.read_text(encoding='utf-8'))
assert d.get('schemaVersion')==2
assert d.get('policy',{}).get('gameVerifiedProtection') is True
assert len(d.get('fusionRecipes',[]))==17
names=[x.get('name') for x in d.get('droids',[])]
assert len(names)==len(set(names)), 'Duplicate droid names'
locked=d['lockedVerifiedMechanics']['blueprintSchedule']
assert locked=={'stellar':{'intervalSeconds':1800,'offsetSeconds':300},'mythic':{'intervalSeconds':3600,'offsetSeconds':3300},'kyber':{'intervalSeconds':3600,'offsetSeconds':900}}
mission=d['lockedVerifiedMechanics']['mission']
assert mission['intervalSeconds']==2100 and mission['activeSeconds']==300 and mission['anchorUtc']=='2026-10-05T03:45:30Z'
print(f'OK: schema v2, {len(names)} droids, 17 fusion recipes, verified mechanics preserved')
