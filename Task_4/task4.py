import json
from datetime import datetime


def update_date(dt):
    with open('Task_4/task4.json') as f:
        d = json.load(f)
        for item in d:
            item["updated"] = dt.isoformat()
    with open('Task_4/task4_res.json', 'w') as wr:
        json.dump(d, wr)


update_date(datetime.now())

