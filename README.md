# Vasicek Short-Rate Model — Calibrated to Indian T-Bill Data

A from-scratch implementation of the Vasicek mean-reverting short-rate model, calibrated to real RBI 91-day Treasury Bill auction data rather than textbook parameters. Includes both a manually derived interest rate tree (with the non-standard recombining algorithm mean-reverting models require) and a 10,000-path Monte Carlo simulation, cross-validated against closed-form analytical results.

## Overview

The Vasicek model assumes the short-term interest rate is continuously pulled back toward a long-run equilibrium level, with random shocks layered on top:

```
dr = k(θ − r) dt + σ dw
```


This project:
1. Calibrates `k` (speed of mean reversion), `θ` (long-run mean), and `σ` (volatility) from 5 years of real weekly RBI 91-day T-bill auction data, using OLS regression on the discretized SDE.
2. Builds a 2-period interest rate tree by hand, demonstrating why Vasicek trees are non-recombining, then derives the probability-adjusted recombining version using mean/variance-matching.
3. Runs a 10,000-path, 5-year Monte Carlo simulation of the calibrated model.
4. Validates the simulation against closed-form expected-rate and half-life formulas.

## Data

Source: RBI auction results for the 91-day Government of India Treasury Bill, weekly frequency, April 2021 – July 2026 (268 usable observations after removing one data artifact showing a 0% yield). The Weighted Average Yield (%) column is used as the short-rate proxy.

## Methodology

### 1. Calibration (`parameter_calibration.py`)

The Vasicek SDE, discretized over irregular real-world time steps, reduces to a linear regression with no intercept:

```
dr = (kθ)·dt − k·(r_prev·dt) + error
```


Fit via OLS on `dt` and `r_prev·dt`, with `k`, `θ` recovered from the fitted coefficients and `σ` recovered from the scaled residual standard deviation.

**Calibrated parameters:**

| Parameter | Value |
|---|---|
| k (mean reversion speed) | 0.4478 |
| θ (long-run mean) | 6.39% |
| σ (volatility) | 0.617% |
| r0 (starting rate) | 5.32% |
| Half-life | ≈ 1.55 years |

### 2. Interest Rate Tree (`vasicek_tree.py`)

Builds a 2-period tree using the node-update formula `r_next = r + k(θ−r)dt ± σ√dt`, demonstrating that Vasicek trees do not recombine (the "up-then-down" and "down-then-up" paths land at slightly different rates, since mean reversion pulls harder on whichever branch sits further from θ). The script then implements the standard fix: collapsing the two near-duplicate middle nodes into one, and solving in closed form for adjusted (non-50/50) probabilities that preserve the original mean and variance of each branch.

### 3. Monte Carlo Simulation (`vasicek_monte_carlo.py`)

Simulates 10,000 independent 5-year rate paths (weekly steps) via Euler discretization of the SDE, then validates the simulation's terminal mean against the model's closed-form expected-rate formula:

```
E[r_T] = r0·e^(−kT) + θ·(1 − e^(−kT))
```

The simulated terminal mean (6.270%) matches the closed-form value (6.263%) to within a basis point.
![Simulated Vasicek paths](monte_carlo_paths.png)

## Repository Structure

```
.
├── parameter_calibration.py # Data loading, cleaning, OLS calibration
├── vasicek_tree.py # 2-period tree + recombining algorithm
├── vasicek_monte_carlo.py # Monte Carlo simulation + closed-form checks
├── Auctions_of_91_Day_Government_of_India_Treasury_Bills.xlsx
└── monte_carlo_paths.png
```

## Running

```bash
pip install pandas numpy statsmodels matplotlib openpyxl
python parameter_calibration.py
python vasicek_tree.py
python vasicek_monte_carlo.py
```

`vasicek_tree.py` and `vasicek_monte_carlo.py` both import calibrated parameters directly from `parameter_calibration.py`.

## Author

Yusuf Sayeed | FRM P1 | FMVA® |