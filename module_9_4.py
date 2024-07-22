# lambda - функция

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda x, y: x == y, first, second))
print(result)

# замыкание

def get_advanced_writer(file_name):

    def write_everything(*data_set):
        for i in range(len(data_set)):
            with open(file_name, 'a', encoding='UTF-8') as file:
                file.write(f'{str(data_set[i])}\n')

    return write_everything

write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])

# метод __call__
import random


class MysticBall:

    def __init__(self, *words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)
    

first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
