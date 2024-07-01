def game(team1_num, team2_num, score1, score2, team1_time, team2_time, challenge_result, tasks_total, time_avg):
    print('В команде Мастера кода участников: %(team1_num)s!' % {'team1_num': team1_num})
    print('В команде Волшебники данных кода участников: %(team2_num)s!' % {'team2_num': team2_num})
    print('Итого сегодня в командах участников: %(team1_num)s и %(team2_num)s!' % {'team1_num': team1_num, 'team2_num': team2_num})

    print('Команда Мастера кода решила задач: {score1}'.format(score1=score1))
    print('Мастера кода решили задачи за {team1_time} c!'.format(team1_time=team1_time))
    print('Команда Волшебники данных решила задач: {score2}'.format(score2=score2))
    print('Волшебники данных решили задачи за {team2_time} c!'.format(team2_time=team2_time))

    print(f'Команды решили {score1} и {score2} задач')
    print(f'Результат битвы: {challenge_result}')
    print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу')


team1_num, team2_num = int(input('Колличество участников в команде Мастера кода: ')), int(input('Колличество участников в команде Волшебники данных: '))
score1, score2 = int(input('Команда Мастера кода решила задач: ')), int(input('Команда Волшебники данных решили задач: '))
team1_time, team2_time = float(input('Мастера кода решили задачи за (сек): ')), float(input('Волшебники данных решили задачи за (сек): '))

if score1 > score2:
    challenge_result = 'Победа команды Мастера кода!'
elif score1 < score2:
    challenge_result = 'Победа команды Волшебники данных!'
else:
    challenge_result = 'Победила дружба!'

tasks_total = score1 + score2
time_avg = (team1_time + team2_time) / tasks_total

print('-'*20)

game(team1_num, team2_num, score1, score2, team1_time, team2_time, challenge_result, tasks_total, time_avg)


