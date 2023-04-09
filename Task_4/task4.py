import json
from datetime import datetime

dt = datetime.now()
with open('task4.json') as f:
    d = json.load(f)
    for item in d:
        item["updated"] = dt.isoformat()
with open('task4_res.json', 'w') as wr:
    json.dump(d, wr)
