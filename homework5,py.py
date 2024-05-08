# работа со списками
my_list = ['banana','mango','apple','orange', 'lime']
print('Список:', my_list)
print(f'''Первый элемент: {my_list[0]}
Последний элемент: {my_list[-1]}''')
print(f'Подсписок my_list с третьего до пятого элементов: {my_list[2:5]}')
my_list[2] = 'pineapple'
print(f'Измененный список: {my_list}')

# работа со словарями
my_dict = {'one': 'один', 'two': 'два', 'free': 'три', 'four': 'четыре', 'five': 'пять'}
print()
print('Словарь: ', my_dict)
print('Представляем вам словарь, в который входят следующие значения: ')
for i in my_dict:
    print(f'- {i}')
k = input('Введите слово, перевод которого хотели бы узнать: ')
print(f'Тадамс! А вот и перевод: {k}: {my_dict[k]}')
print('Согласны ли вы с переводом(yes | no):', end=' ')
answer = input()
if answer == 'yes':
    print('Здорово! Давайте добавим новое слово в наш словарь!')
    new_word = input('Введите слово на английском языке: ')
    new_translate = input('Пожалуйста укажите его перевод: ')
    my_dict[new_word] = new_translate
    print('Давайте посмотрим на наш новый словарик:')
    for i in my_dict:
        print(f'- {i}: {my_dict[i]}')
elif answer == 'no':
    print('Эхх.. Ну, тогда укажите свой вариант перевода. Давайте его изменим: ', end=' ')
    new_translate = input(f'Новый перевод слова {my_dict[k]}: ')
    my_dict[k] = new_translate
    print('Давайте посмотрим на наш новый словарик:')
    for i in my_dict:
        print(f'- {i}: {my_dict[i]}')