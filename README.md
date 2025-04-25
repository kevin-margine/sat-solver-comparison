# SAT Solver Comparison

This project implements and compares SAT solving algorithms: Resolution, Davis-Putnam (DP), and DPLL.

## Contents

- `scripts/`: Python implementations of the solvers
- `data/`: Sample CNF test cases in DIMACS format
- `results/`: Collected experiment results

## How to Run

Install dependencies:

```bash
pip install -r requirements.txt
python scripts/main.py --solver dpll --file data/sample.cnf --strategy freq

