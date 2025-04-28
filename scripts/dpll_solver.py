# dpll_solver.py
def dpll_solver(clauses, assignment, strategy='freq'):
    clauses, assignment = unit_propagate(clauses, assignment)
    if clauses is None:
        return False
    if not clauses:
        return True

    symbols = get_unassigned_symbols(clauses, assignment)
    if not symbols:
        return True

    variable = choose_variable(symbols, strategy)
    for val in [variable, -variable]:
        new_clauses = simplify(clauses, val)
        new_assignment = assignment + [val]
        if dpll_solver(new_clauses, new_assignment, strategy):
            return True
    return False

def unit_propagate(clauses, assignment):
    changed = True
    while changed:
        changed = False
        unit_literals = [c[0] for c in clauses if len(c) == 1]
        if not unit_literals:
            break
        for lit in unit_literals:
            assignment.append(lit)
            clauses = simplify(clauses, lit)
            if [] in clauses:
                return None, assignment
            changed = True
    return clauses, assignment

def simplify(clauses, literal):
    return [ [l for l in c if l != -literal] for c in clauses if literal not in c ]

def get_unassigned_symbols(clauses, assignment):
    assigned = set(abs(lit) for lit in assignment)
    return sorted(set(abs(l) for c in clauses for l in c) - assigned)

def choose_variable(symbols, strategy):
    import random
    if strategy == 'random':
        return random.choice(symbols)
    return symbols[0]
