# Задаем переменные разных типов данных:
print('Кортеж:')
immutable_var = (1, 'a', ['a','b','c'], 2.3, {'d': 123}, {1, 2, 3, 4})
for i in range(len(immutable_var)):
    print(i+1, f'-({type(immutable_var[i])})', ': ', immutable_var[i], sep='')

# Пробуем изменить значения переменных в кортеже(попытка_1)
s = 'Hello world!'
n = int(input('Укажите элемент кортежа, приведенного выше: '))
print(f'Вы выбрали элемент: {immutable_var[n-1]}. Его тип: {type(immutable_var[n-1])}')
print(f'Давайте попробуем заменить элемент кортежа №{n} на "{s}"', end='\n')
input(f'**Для продолжения нажмите "Enter"')
print(f'''
Пишем:
***
immutable_var[{n-1}] = {s}
print('immutable_var')
***
Запускаем!''', end='\n')
print(f'Для продолжения нажмите "Enter"')
input()
print()
print('думает.. думает..')
print()
print('Вы сломали компьютер!', end='\n')
input(f'**Для продолжения нажмите "Enter"')

#Создаем изменяемые структуры данных
print('', '----БДМС! Компьютер ожил!----', '', sep='\n')
mutable_list = [1, 2, 3, 4]
ex_dict = ['один', 'два', 'три', 'четыре']
print(f'Теперь у нас есть список: {mutable_list}. Давайте его изменим', 'Думаем, думаем..', 'Получаем: ', sep='\n', end='\n')
for i in range(len(mutable_list)):
    mutable_list[i] = ex_dict[i]
input(f'**Для продолжения нажмите "Enter"')
print(mutable_list, 'Список изменен!', sep='\n', end='\n')
input(f'**Для продолжения нажмите "Enter"')
# Пробуем изменить значения переменных в кортеже(попытка_2)
# Ломаем программу
n = int(input(f'''Давайте вспомним наш кортеж immutable_var = {immutable_var}
Выберите любой из его элементов(от 1 до 6): '''))
print('Теперь мы на самом деле его заменим. \n----Готовьтесь к ошибке!---- \nИ вот..: ')
immutable_var[n-1] = 'Bye, bye world!'