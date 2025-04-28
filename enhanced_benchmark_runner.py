# enhanced_benchmark_runner.py
import os
import time
import psutil
from scripts.dp_solver import dp_solver
from scripts.dpll_solver import dpll_solver
from scripts.resolution_solver import resolution_solver
from scripts.utils import parse_dimacs

def extract_symbols(clauses):
    return sorted({abs(lit) for clause in clauses for lit in clause})

def run_solver(solver_name, clauses, strategy='freq'):
    symbols = extract_symbols(clauses)
    start_time = time.time()
    process = psutil.Process()
    mem_before = process.memory_info().rss / (1024 * 1024)  # Convert to MB

    if solver_name == 'dp':
        result = dp_solver(clauses, symbols)
    elif solver_name == 'dpll':
        result = dpll_solver(clauses, [], strategy=strategy)
    elif solver_name == 'resolution':
        result = resolution_solver(clauses)
    else:
        raise ValueError(f"Unknown solver {solver_name}")

    mem_after = process.memory_info().rss / (1024 * 1024)
    end_time = time.time()

    elapsed_time = end_time - start_time
    mem_used = max(mem_after - mem_before, 0)  # Sometimes mem usage may fluctuate
    return result, elapsed_time, mem_used

def main():
    data_dir = "data"
    solvers = ['dp', 'dpll', 'resolution']
    strategy = 'freq'  # For DPLL

    cnf_files = [f for f in os.listdir(data_dir) if f.endswith('.cnf')]

    for cnf_file in cnf_files:
        cnf_path = os.path.join(data_dir, cnf_file)
        print(f"\nBenchmarking {cnf_file}:")

        clauses = parse_dimacs(cnf_path)

        for solver in solvers:
            try:
                result, duration, memory = run_solver(solver, clauses, strategy)
                print(f"  {solver.upper()} -> Result: {'SAT' if result else 'UNSAT'} | Time: {duration:.4f}s | Memory: {memory:.2f}MB")
            except Exception as e:
                print(f"  {solver.upper()} -> Failed with error: {e}")

if __name__ == '__main__':
    main()
