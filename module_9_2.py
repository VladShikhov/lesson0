first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(string_) for string_ in first_strings if len(string_) >= 5]

second_result = [(string_f, string_s) for string_f in first_strings for string_s in second_strings if len(string_f) == len(string_s)]

third_result = {string_fs: len(string_fs) for string_fs in first_strings + second_strings if len(string_fs) % 2 == 0}

print(first_result)
print(second_result)
print(third_result)
