height = [155, 160, 163, 167, 170, 174, 178, 182, 186, 190]
weight = [44, 46, 48, 50, 57, 62, 70, 74, 79, 82]
plt.title("선 그래프")
plt.xlabel("몸무게")
plt.ylabel("키")
plt.plot(weight, height, color = "blue", lw = 1)
plt.scatter(weight, height, color = "red", s = 100)
plt.show()