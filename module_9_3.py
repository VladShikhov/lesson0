first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result  = (len(tuple_[0]) - len(tuple_[1]) for tuple_ in zip(first, second) if len(tuple_[0]) != len(tuple_[1]))

second_result = (True if len(first[i]) == len(second[i]) else False for i in range(len(first)))

print(list(first_result))
print(list(second_result))