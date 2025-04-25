# resolution_solver.py
def resolution_solver(clauses):
    new = set()
    clauses = [frozenset(c) for c in clauses]
    while True:
        pairs = [(c1, c2) for i, c1 in enumerate(clauses) for c2 in clauses[i+1:]]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if frozenset() in resolvents:
                return False
            new.update(resolvents)
        if new.issubset(clauses):
            return True
        clauses.extend(new - set(clauses))

def resolve(ci, cj):
    resolvents = set()
    for l in ci:
        if -l in cj:
            resolvent = ci.union(cj) - {l, -l}
            resolvents.add(frozenset(resolvent))
    return resolvents
