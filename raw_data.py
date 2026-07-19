# %%
import pandas as pd
import statsmodels.api as sm
import numpy as np

# %%
raw_data = pd.read_excel("Auctions_of_91_Day_Government_of_India_Treasury_Bills.xlsx")

# %%
raw_data = raw_data[raw_data.iloc[:, 3] != 0].reset_index(drop=True)


# %%
r = raw_data.iloc[:, 3] / 100
r.describe()

# %%
dates = raw_data.iloc[:, 0]
dt = dates.diff().dt.days / 365
dt.describe()

# %%
dr = r.diff()
dr.describe()

# %%
r_prev = r.shift(1)
r_prev

# %%
r_prev__dt = r_prev * dt
# %%
reg_data = pd.DataFrame({"dt": dt, "dr": dr, "r_prev": r_prev, "r_prev_dt" : r_prev__dt})
reg_data = reg_data.dropna().reset_index(drop=True)
reg_data
# %%


x = reg_data[["dt", "r_prev_dt"]]
y = reg_data["dr"]

model = sm.OLS(y, x).fit()
print(model.summary())

# %%
residuals = model.resid
sigma = np.std(residuals / np.sqrt(reg_data['dt']), ddof=1)

a = model.params['dt']
b = model.params['r_prev_dt']
k = -b
theta = a / k

sigma, k, theta
