# %%
import pandas as pd

# %%
raw_data = pd.read_excel("Auctions_of_91_Day_Government_of_India_Treasury_Bills.xlsx")

# %%
r = raw_data.iloc[:, 3] / 100
r.describe()

# %%
raw_data = raw_data[raw_data.iloc[:, 3] != 0].reset_index(drop=True)

# %%
dates = raw_data.iloc[:, 0]
dt = dates.diff().dt.days / 365
dt.dropna(how = any, inplace = True)
dt.describe()

# %%
dr = r.diff()
dr.dropna(how = any, inplace = True)
# %%
