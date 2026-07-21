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
r_uu = r_up + (k*(theta - r_up)*dt_tree + sigma*np.sqrt(dt_tree))
r_ud = r_up + (k*(theta - r_up)*dt_tree - sigma*np.sqrt(dt_tree))

r_du = r_down + (k*(theta - r_down)*dt_tree + sigma*np.sqrt(dt_tree))
r_dd = r_down + (k*(theta - r_down)*dt_tree - sigma*np.sqrt(dt_tree))

print(f"r_uu : {r_uu} \nr_ud : {r_ud} \nr_du : {r_du} \nr_dd : {r_dd}")

# %%
r_mid = (r_ud + r_du).mean()

# %%
