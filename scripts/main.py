# main.py
import argparse
import time
from scripts.dp_solver import dp_solver
from scripts.dpll_solver import dpll_solver
from scripts.resolution_solver import resolution_solver
from scripts.utils import parse_dimacs

def extract_symbols(clauses):
    return sorted({abs(lit) for clause in clauses for lit in clause})

def main():
    parser = argparse.ArgumentParser(description='Run a SAT solver.')
    parser.add_argument('--solver', type=str, required=True, help='Choose solver: dp, dpll, resolution')
    parser.add_argument('--file', type=str, required=True, help='Path to CNF file')
    parser.add_argument('--strategy', type=str, default='freq', help='Heuristic strategy (for DPLL): freq or random')
    args = parser.parse_args()

    clauses = parse_dimacs(args.file)
    symbols = extract_symbols(clauses)

    start = time.time()
    if args.solver == 'dp':
        result = dp_solver(clauses, symbols)
    elif args.solver == 'dpll':
        result = dpll_solver(clauses, [], strategy=args.strategy)
    elif args.solver == 'resolution':
        result = resolution_solver(clauses)
    else:
        print("Unknown solver.")
        return
    end = time.time()

    print(f"Solver: {args.solver.upper()}")
    print(f"Strategy: {args.strategy if args.solver == 'dpll' else 'N/A'}")
    print(f"Result: {'SAT' if result else 'UNSAT'}")
    print(f"Time: {end - start:.4f} seconds")

if __name__ == '__main__':
    main()
