# resolution_solver.py
def resolution_solver(clauses):
    clauses = [frozenset(c) for c in clauses]
    new = set()

    while True:
        pairs = [(clauses[i], clauses[j]) for i in range(len(clauses)) for j in range(i+1, len(clauses))]
        for (ci, cj) in pairs:
            resolvents = resolve(ci, cj)
            if frozenset() in resolvents:
                return False  # UNSAT
            new.update(resolvents)

        if new.issubset(set(clauses)):
            return True  # SAT

        clauses.extend(list(new - set(clauses)))

def resolve(ci, cj):
    resolvents = set()
    for l in ci:
        if -l in cj:
            resolvent = (ci.union(cj)) - {l, -l}
            resolvents.add(frozenset(resolvent))
    return resolvents
