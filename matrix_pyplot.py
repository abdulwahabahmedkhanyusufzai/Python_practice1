import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = sns.load_dataset("tips")

tipscorr = df[['total_bill','tip','size']]
tipscorr.corr()
sns.heatmap(tipscorr.corr(),annot=True)

corr_matrix = df.corr(numeric_only=True)

# 2. Plot Clustermap
# cmap='coolwarm' makes it easier to see positive vs negative correlations
# annot=True adds the numbers for research accuracy
sns.clustermap(corr_matrix, annot=True, cmap='coolwarm', figsize=(7, 7))

pivotflight = df.pivot_table(index='sex',columns='day',values='tip')
sns.heatmap(pivotflight,annot=True)
plt.show()