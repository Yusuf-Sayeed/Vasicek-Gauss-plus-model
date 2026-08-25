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
r_mid = (r_ud + r_du) / 2 
r_mid

# %%
M1 = 0.5 * (r_uu + r_ud)
M2 = 0.5 * (r_uu**2 + r_ud**2)
V = M2 - M1**2
V
# %%
p = (M1 - r_mid)**2 / (V + (M1 - r_mid)**2)
p
# %%
r_uu_new = r_mid + ((M1 - r_mid)/p)
r_uu_new
# %%
M1_lower = 0.5 * (r_du + r_dd)
M2_lower = 0.5 * (r_du**2 + r_dd**2)
V_lower = M2_lower - M1_lower**2

q = (M1_lower - r_mid)**2 / (V_lower + (M1_lower - r_mid)**2)
r_dd_new = r_mid + (M1_lower - r_mid) / q
r_dd_new
# %%
