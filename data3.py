x = ["사과", "포도", "딸기"]
y = [12, 31, 24]
plt.title("과일 생산량")
plt.bar(x, y, color = "Lightblue", width = 0.5)
plt.xlabel("과일 종류")
plt.ylabel("판매량")
plt.ylim(0, 40)
plt.show()