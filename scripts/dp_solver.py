# dp_solver.py
# Simple implementation of Davis-Putnam (DP) algorithm

def dp_solver(clauses, symbols):
    if not clauses:
        return True  # All clauses satisfied
    if [] in clauses:
        return False  # Conflict: empty clause found

    symbol = symbols[0] if symbols else None
    if symbol is None:
        return False

    rest_symbols = symbols[1:]
    # Try assigning True
    new_clauses = simplify(clauses, symbol)
    if dp_solver(new_clauses, rest_symbols):
        return True
    # Try assigning False
    new_clauses = simplify(clauses, -symbol)
    return dp_solver(new_clauses, rest_symbols)

def simplify(clauses, literal):
    result = []
    for clause in clauses:
        if literal in clause:
            continue  # Clause is satisfied
        new_clause = [x for x in clause if x != -literal]
        result.append(new_clause)
    return result
