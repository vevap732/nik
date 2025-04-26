import matplotlib.pyplot as plt
subjects = ['Математический анализ', 'Линейная алгебра', 'Физика', 'Варкт']
grades = [4, 5, 5, 5]
colors = ['blue', 'green', 'orange', 'purple']
fig, ax = plt.subplots()
ax.bar(subjects, grades, color=colors)
ax.set_ylim([2, 5])
ax.set_title("Оценки за прошедшее полугодие")
ax.set_xlabel("Предметы")
ax.set_ylabel("Оценка")
legend_labels = [f"{subject}: {grade}" for subject, grade in zip(subjects, grades)]
ax.legend(legend_labels, loc="upper right")
plt.show()
