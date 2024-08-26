team1 = "Мастера кода"
team2 = "Волшебники данных"
def num(team1_nume=0, team2_nume=0):


    print("В команде %s участников: %s !" % (team1,team1_num))
    print("В команде %s участников: %s !" % (team2,team2_num))

def time(team1_nume=0, team2_nume=0):


    print(" Команда {} решила задач:{}!".format(team1,score_1))
    print("{} решили задачи за {} секунд.!".format(team2,team2_time))


def challenge_result(tasks_total=0,time_avg=0):
    print(f"Команды решили{score_1} и {score_2} задач")

    if score_1 > score_2:
        print(f"Результат битвы: победа команды {team1}!")

    else:
        print(f"Результат битвы:победа команды{team2}!")


    print(f"Сегодня было решено {tasks_total} задач, в среднем по {time_avg}секунды на задачу!.")
print(num, time, challenge_result)


team1_num = 5
team2_num = 6
score_1 = 40
score_2 = 42
team1_time = 1552.512
team2_time = 2153.31451
tasks_total = 82
time_avg = 45.2

num(team1_num, team2_num)
time(team1_time, team2_time)
challenge_result(tasks_total, time_avg)





