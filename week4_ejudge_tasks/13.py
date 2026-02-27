import json

data = json.loads(input())
q = int(input())

for _ in range(q):
    path = input().strip()
    cur = data
    ok = True
    i = 0
    while i < len(path):
        if path[i] == '.':
            i += 1
            continue
        if path[i] == '[':
            i += 1
            num = ""
            while i < len(path) and path[i] != ']':
                num += path[i]
                i += 1
            i += 1
            if not num.isdigit():
                ok = False
                break
            idx = int(num)
            if not isinstance(cur, list) or idx < 0 or idx >= len(cur):
                ok = False
                break
            cur = cur[idx]
        else:
            key = ""
            while i < len(path) and path[i] not in '.[':
                key += path[i]
                i += 1
            if not isinstance(cur, dict) or key not in cur:
                ok = False
                break
            cur = cur[key]
    if ok:
        print(json.dumps(cur, separators=(',', ':')))
    else:
        print("NOT_FOUND")