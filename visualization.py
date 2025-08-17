import matplotlib.pyplot as plt
import seaborn as sns
x=[]
x.extend((final_data['Type'].value_counts()['A'],final_data['Type'].value_counts()['B'],final_data['Type'].value_counts()['C']))
print(x)

def func(pct, allvalues):
    absolute = int(pct / 100.*np.sum(allvalues))
    return "{:.1f}%\n({:d} g)".format(pct, absolute)
l=['A','B',"C"]
fig, ax = plt.subplots(figsize =(10, 7))
wedges, texts, autotexts = ax.pie(x,autopct = lambda pct: func(pct, x),labels=l)

fig = plt.figure(figsize =(10, 7))
sns.barplot(data=final_data,x="Size",y="Weekly_Sales",hue="Type")
plt.show()

#cpi vs weekly sales
fig = plt.figure(figsize =(10, 7))
sns.scatterplot(data=final_data,x="CPI",y="Weekly_Sales",hue="Type")
plt.show()

#unemp vs weekly sales
fig = plt.figure(figsize =(10, 7))
sns.scatterplot(data=final_data,x="Unemployment",y="Weekly_Sales",hue="Type")
plt.show()

sns.scatterplot(data=final_data,x="MarkDown3",y="Weekly_Sales",hue="Type")


