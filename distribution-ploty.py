import seaborn as sns 
import matplotlib.pyplot as plt 

# Set the style to 'whitegrid' for a professional "Google Research" look
sns.set_theme(style="whitegrid")

df = sns.load_dataset("tips")

plt.subplot(1,2,1)
# Creating a high-quality distribution plot with a KDE line
sns.displot(data=df, x='total_bill', kde=True, color='purple', aspect=1.5)

plt.subplot(1,2,2)
sns.displot(data=df, x='tip', kde=True, color='purple', aspect=1.5)

plt.title("Distribution of Total Bill Amounts")
sns.jointplot(x="total_bill",y="tip",data=df)
sns.jointplot(x="total_bill",y="tip",data=df,kind="kde")
sns.jointplot(x="total_bill",y="tip",data=df,kind="hex")
sns.jointplot(x="total_bill",y="tip",data=df,kind="reg")
sns.pairplot(df,hue="sex")
sns.pairplot(df,hue="size",palette="rainbow")
sns.rugplot(df["total_bill"])

plt.show()