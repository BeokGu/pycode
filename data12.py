class_c = graph.groupby("반").size( )
class_c.plot.pie(title = "반별 인원수 분포", ylabel = "반", autopct = "%1.1f%%", explode = (0.1, 0, 0), shadow = True)
plt.show( )