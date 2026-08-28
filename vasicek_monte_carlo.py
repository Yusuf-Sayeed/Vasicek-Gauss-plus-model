# %%
from parameter_calibration import sigma, k, theta, r0
import numpy as np
import matplotlib.pyplot as plt

# %%
n_steps = 260
n_paths = 10000
dt_tree = 1/52

# %%
# %%
paths = np.zeros((n_paths, n_steps + 1))
paths[:, 0] = r0
paths

# %%
np.random.seed(123)
z = np.random.normal(loc = 0, scale=1, size = (n_paths, n_steps))

# %%
for t in range(n_steps):
    paths[:, t+1] = paths[:, t] + k*(theta - paths[:, t])*dt_tree + sigma*np.sqrt(dt_tree)*z[:, t]

paths
paths[:, -1].mean(), paths[:, -1].std()


# Visualisation
# %%
time_axis = np.linspace(0, n_steps*dt_tree, n_steps+1)

# %%
sample_idx = np.random.choice(n_paths, size=75, replace=False)

# %%
plt.figure(figsize=(11, 6))
for i in sample_idx:
    plt.plot(time_axis, paths[i], color='steelblue', alpha=0.15, linewidth=0.8)

plt.plot(time_axis, paths.mean(axis=0), color='darkred', linewidth=2, label='Mean path')
plt.axhline(theta, color='black', linestyle='--', linewidth=1, label=f'θ = {theta:.4%}')

plt.title('Vasicek Monte Carlo Simulation — 91-Day T-Bill Short Rate (5-Year Horizon)')
plt.xlabel('Years')
plt.ylabel('Short Rate')
plt.legend()
plt.tight_layout()
plt.show()

# Expected Rate

# %%
def expected_rate(T):

    expected_rate = r0*np.exp(-k*T) + (theta * (1 - np.exp(-k*T)))

    return expected_rate

# %%

# Half Life

def half_life():
    tau = np.log(2) / k
    return tau

# %%
expected_rate(5), half_life()

