# TSP Genetic Algorithm

A genetic algorithm for the Travelling Salesman Problem, written from scratch in Python: no optimisation library, just the population loop, the selection, crossover and mutation operators, and three TSPLIB benchmark instances.

## What is in it

| Path | Contents |
|---|---|
| `charles/charles.py` | `Individual` and `Population`, the generational loop, elitism and fitness sharing |
| `charles/selection.py` | fitness-proportionate, ranking and tournament selection |
| `charles/crossover.py` | cycle, PMX and order-1 crossover |
| `charles/mutation.py` | swap, inversion and shuffle mutation |
| `charles/search.py` | hill climbing and simulated annealing (kept as written, not used by the GA) |
| `data/tsp_data.py` | swiss42, bayg29 and brazil58 from TSPLIB, plus a 13-city example |
| `tsp.py` | one GA run on swiss42 |
| `plot_progress.py` | the same run with and without elitism, saved as `elitism_comparison.png` |
| `check.py` | a short run on all three instances that checks every reported tour length |

## Run it

```bash
pip install -r requirements.txt
python check.py           # under a minute
python tsp.py             # one run on swiss42
python plot_progress.py   # elitism comparison figure
```

Settings are constants at the bottom of `tsp.py` and `plot_progress.py`. To use another instance, change `DISTANCE_MATRIX`, `SOL_SIZE` and `VALID_SET` together. The GitHub Actions workflow runs all three scripts on every push and uploads the figure.

## Implementation notes

- Every child inherits its population's distance matrix, so a run is always scored on the instance it is solving. `check.py` asserts this on all three instances.
- The swiss42 matrix is checked for symmetry; TSPLIB's cell `[25][9]` is 65.
- Dependencies are pinned in `requirements.txt` and tested on Python 3.12 in CI.
- The simulated annealing in `search.py` is not used by the GA and is not tuned for minimisation.

## Data

swiss42, bayg29 and brazil58 come from [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/). The 13-city example comes from the Google OR-Tools documentation.

## Licence

GPL-3.0, see `LICENSE`.
