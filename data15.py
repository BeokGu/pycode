graph["사회"].plot.hist(bins = 20, color = "blue", edgecolor = "blue", alpha = 0.5, title = "히스토그램")
graph["과학"].plot.hist(bins = 20, color = "red", edgecolor = "red", alpha = 0.5, grid = True)
plt.show( )