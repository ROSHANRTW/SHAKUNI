import itertools

def generate_combinations(data):
    keys = [k for k in data if k != "suffix"]
    values = [data[k] for k in keys]

    base = set()
    for r in range(1, len(values)+1):
        for perm in itertools.permutations(values, r):
            joined = ''.join(perm)
            base.add(joined)

            # smart combos
            if "dob" in data:
                base.add(f"{perm[0]}@{data['dob'][-4:]}")
            base.add(f"{perm[0]}!123")
            base.add(f"{perm[0]}#99")

    return list(base)
