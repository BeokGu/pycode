fruit = ["사과", "포도", "딸기", "참외"]
sales = [12, 31, 24, 46]
df=pd.Series(sales, index=fruit)

df.plot.pie(title="과일 판매량", ylabel="과일", autopct="%1.1f%%", explode=(0.1, 0, 0, 0), shdaow=True)
plt.show( )