# %%
from parameter_calibration import sigma, k, theta, r0
import numpy as np

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
