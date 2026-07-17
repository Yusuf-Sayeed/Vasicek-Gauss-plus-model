# %%
import pandas as pd

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
# %%
reg_data = pd.DataFrame({'dt': dt, 'dr': dr, 'r_prev': r_prev})
reg_data = reg_data.dropna().reset_index(drop=True)
reg_data