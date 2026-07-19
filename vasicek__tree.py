# %%
from parameter_calibration import sigma, k, theta, r0
import numpy as np
import pandas as pd

# %%
print(f"sigma : {sigma}\nk : {k}\ntheta :  {theta}\nr0 :  {r0}")

# %%
dt_tree = 1/52

# %%
r_up = r0 + (k*(theta - r0)*dt_tree + sigma*np.sqrt(dt_tree))
r_down = r0 + (k*(theta - r0)*dt_tree - sigma*np.sqrt(dt_tree))

print(f"r_up : {r_up} \nr_down : {r_down}")

# %%
