# utils.py
def parse_dimacs(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    clauses = []
    for line in lines:
        if line.startswith('c') or line.startswith('p'):
            continue
        clause = list(map(int, line.strip().split()))
        if clause[-1] == 0:
            clause = clause[:-1]
        clauses.append(clause)
    return clauses
