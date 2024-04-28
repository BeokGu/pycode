a = graph.iloc[:, 2:7].mean( ).plot.barh(gird = True, color = "blue")
a.set_xlabel("평균")
a.set_title("과목별 평균 점수")
plt.show( )