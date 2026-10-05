#!/usr/bin/env python3
import json
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
OUT = Path(__file__).resolve().parents[1] / "data" / "live-data.json"
URL = "https://gonk.tools/api/droid-alerts/limited-deal"
def pick(obj, *keys):
    for key in keys:
        if isinstance(obj, dict) and obj.get(key) not in (None, ""):
            return obj[key]
    return None
req = urllib.request.Request(URL,headers={"User-Agent":"KYBER-TOOL GitHub updater","Accept":"application/json"})
with urllib.request.urlopen(req, timeout=20) as response:
    raw=json.loads(response.read().decode("utf-8"))
root=raw
for key in ("data","deal","current"):
    if isinstance(root,dict) and isinstance(root.get(key),dict): root=root[key]
name=pick(root,"name","title","droid","displayName","item","dealName")
if not name: raise RuntimeError("Unrecognised deal response; refusing to overwrite live-data.json")
variant=pick(root,"variant","tier","finish","rarityVariant") or ""
rarity=pick(root,"rarity","class") or ""
seconds=pick(root,"secondsRemaining","seconds_remaining","remainingSeconds","ttl","nextDealSeconds")
try: seconds=int(float(seconds)) if seconds is not None else None
except (TypeError,ValueError): seconds=None
payload={"updatedAt":datetime.now(timezone.utc).isoformat(),"source":"gonk.tools","status":"live","deal":{"name":str(name),"variant":str(variant),"rarity":str(rarity),"secondsRemaining":seconds}}
OUT.write_text(json.dumps(payload,indent=2)+"\n",encoding="utf-8")
print(payload["deal"])
