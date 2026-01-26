import seaborn as sns 
import plotly.express as px

tips = sns.load_dataset("tips")
# Plot using plotly.express instead of cufflinks .iplot()
fig = px.line(tips, y="total_bill", title="Total Bill")
# Calculate average tip by day
avg_tips = tips.groupby('day', observed=True)['tip'].mean().reset_index()
fig2 = px.bar(avg_tips, x='day', y='tip', title="Average Tip by Day")
fig3 = px.scatter(tips,x="total_bill",y="tip",color="sex",title="Total Bill vs Tip")
fig4 = px.box(tips,x="day",y="total_bill",title="Total Bill by Day")
fig4.show()
fig3.show()
fig2.show()
fig.show()
