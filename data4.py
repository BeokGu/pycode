x = ["사과", "포도", "딸기", "참외"]
y = [12, 31, 24, 46]
colors = ["coral", "cornsilk", "pink", "aqua"]
plt.title("원 그래프")
plt.pie(y, labels = x, autopct = "%1.1f%%", colors = colors, shadow = True)
plt.show()