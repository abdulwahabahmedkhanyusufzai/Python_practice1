import seaborn as sns 
import matplotlib.pyplot as plt 
import numpy as np 
import pandas as pd 

df = sns.load_dataset("tips")
sns.lmplot(x="total_bill",y="tip",data=df)
sns.lmplot(x="total_bill",y="tip",data=df,hue="sex")
sns.lmplot(x="total_bill",y="tip",data=df,hue="sex",palette="rainbow")
sns.lmplot(x="total_bill",y="tip",data=df,hue="sex",palette="rainbow",markers=["o","v"])
sns.lmplot(x="total_bill",y="tip",data=df,hue="sex",palette="rainbow",markers=["o","v"],aspect=0.5,scatter_kws={"s":100})
plt.show()