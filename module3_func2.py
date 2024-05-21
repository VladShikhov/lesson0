def print_programs(a = 1, b = 'строка', c = True):
    print(a, b, c)


print_programs(0)
print_programs(0, 'не строка')
print_programs(0, 'не строка', False)
print_programs(b = 25)
print_programs(c = [1, 2, 3])
print()

values_list = [0, 'не строка', False]
values_dict = {'a': 0, 'b': 'не строка', 'c': False}
print_programs(*values_list)
print_programs(**values_dict)
print()

values_list_2 = [0, 'не строка']
print_programs(*values_list_2, 42)