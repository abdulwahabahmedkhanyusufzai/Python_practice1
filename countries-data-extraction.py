import numpy as np
import pandas as pd

df = pd.read_csv('Countries.csv')


idx_max = df['population'].idxmax()
idx_min = df['population'].idxmin()

highest_pop_info = df.loc[idx_max, ['country', 'capital_city']]
least_pop_info = df.loc[idx_min, ['country', 'capital_city']]

# Correct sorting logic
df.sort_values(by="democracy_score", ascending=False, inplace=True)

print(f"Highest Population: {highest_pop_info['country']} (Capital: {highest_pop_info['capital_city']})")
print(f"Least Population: {least_pop_info['country']} (Capital: {least_pop_info['capital_city']})")
print("\nRegion Distribution:")
print(df["region"].value_counts())
print(df[df["region"] == "Eastern Europe"]["country"])
print(df[df["population"] == df["population"].nlargest(2).iloc[1]]["political_leader"])
print(df[df['political_leader'].isna()]["country"])
print(df[df["country_long"].str.contains("Republic")]["country"].count())
print(df[df["region"].str.contains("Africa")]["population"].max())