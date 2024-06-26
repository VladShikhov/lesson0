def custom_write(file_name, strings):
    file = open(file_name, 'a', encoding='utf-8')
    strings_positions = {}
    count = 0
    for p in strings:
        count += 1
        strings_positions[(count, file.tell())] = p
        file.write(p+'\n')
    file.close()
    return strings_positions


info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)
