def calculate_structure_sum(*args, count=[]):
    for i in range(len(args)):
        if not isinstance(args[i], str) and not isinstance(args[i], int) and not isinstance(args[i], dict):
            calculate_structure_sum(*args[i])
        elif isinstance(args[i], str):
            count.append(len(args[i]))
        elif isinstance(args[i], int):
            count.append(args[i])
        elif isinstance(args[i], dict):
            for key, value in args[i].items():
                if isinstance(key, str):
                    count.append(len(key))
                elif isinstance(key, int):
                    count.append(key)
                else:
                    calculate_structure_sum(args[i])
                if isinstance(value, str):
                    count.append(len(value))
                elif isinstance(value, int):
                    count.append(value)
                else:
                    calculate_structure_sum(args[i])
    return sum(count)



data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
result = calculate_structure_sum(data_structure)
print(result)
