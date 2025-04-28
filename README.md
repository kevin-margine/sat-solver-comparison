# SAT Solver Comparison

This project implements and compares SAT solving algorithms:
- Resolution
- Davis-Putnam (DP)
- Davis–Putnam–Logemann–Loveland (DPLL)

## Project Structure

- `scripts/` – Python implementations of the solvers
- `data/` – Sample CNF test cases (DIMACS format)
- `enhanced_benchmark_runner.py` – Script to benchmark all solvers

## How to Install

1. Create a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/Scripts/activate  # On Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## How to Run

### Run a single solver:
```bash
python -m scripts.main --solver dpll --file data/sample_easy.cnf --strategy freq
```

### Run all benchmarks:
```bash
python enhanced_benchmark_runner.py
```

This will benchmark all solvers on all CNF files and display:
- SAT/UNSAT result
- Execution time
- Memory usage

## Requirements

- Python 3.8 or newer
- psutil (for memory measurement)

## License

This project is licensed under the MIT License.
