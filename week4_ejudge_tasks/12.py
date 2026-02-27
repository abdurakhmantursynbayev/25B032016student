import json

def j(v):
    return json.dumps(v, ensure_ascii=False, separators=(',', ':'), sort_keys=True)

def differences(a, b, c=""):
    diffs = []
    keys = set()
    if isinstance(a, dict):
        keys |= set(a.keys())
    if isinstance(b, dict):
        keys |= set(b.keys())
    for key in keys:
        path = f"{c}{key}"
        in_a = isinstance(a, dict) and key in a
        in_b = isinstance(b, dict) and key in b
        if not in_a:
            diffs.append((path, "<missing>", j(b[key])))
            continue
        if not in_b:
            diffs.append((path, j(a[key]), "<missing>"))
            continue
        va = a[key]
        vb = b[key]

        if isinstance(va, dict) and isinstance(vb, dict):
            diffs.extend(differences(va, vb, path + "."))
        else:
            if va != vb:
                diffs.append((path, j(va), j(vb)))
    return diffs
first = input()
second = input()
dictf = json.loads(first)
dicts = json.loads(second)
diffs = differences(dictf, dicts, "")
if not diffs:
    print("No differences")
else:
    diffs.sort(key=lambda x: x[0])
    for path, oldv, newv in diffs:
        print(f"{path} : {oldv} -> {newv}")