#!/usr/bin/env python3

import sys
import json

for line in sys.stdin:
    line = line.strip()
    if not line:
        continue

    try:
        item = json.loads(line)
    except json.JSONDecodeError:
        continue  # skip malformed lines

    if item.get("quantity", 0) <= 100:
        print(json.dumps(item))
