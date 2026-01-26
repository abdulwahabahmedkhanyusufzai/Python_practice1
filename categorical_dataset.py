import seaborn as sns 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

df = sns.load_dataset("tips")

sns.countplot(x=df['sex'],hue=df["smoker"])
sns.countplot(x=df['sex'],hue=df["day"])
sns.countplot(x=df['sex'],hue=df["time"])
sns.countplot(x=df['sex'],hue=df["size"])

sns.barplot(x=df['sex'],y=df["total_bill"],estimator=np.sum)
sns.boxplot(x="tip",y='day',data=df,palette="rainbow")
sns.violinplot(x="tip",y='day',data=df,palette="rainbow")
sns.stripplot(x="tip",y='day',data=df,palette="rainbow")
sns.swarmplot(x="tip",y='day',data=df,palette="rainbow")
plt.show()