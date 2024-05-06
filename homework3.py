# организуем программу
my_string = input()
print('Длина строки: ', len(my_string))

# работаем с методами строк
print(f'Вывод строки в верхнем регистре: {my_string.upper()}')
print(f'Вывод строки в верхнем регистре: {my_string.lower()}')
print(f'Вывод строки без пробелов: {my_string.replace(' ', '')}')
print(f'Вывод первого символа строки: {my_string[0]}')
print(f'Вывод последнего символа строки: {my_string[-1]}')
