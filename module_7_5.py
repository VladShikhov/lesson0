import time

import os
#from time import mktime
#from datetime import datetime


directory = "."

for dirpath, dirnames, filenames in os.walk(directory):
    for file in filenames:
        print()
        print('*' * 27)
        print(f'Обнаружен файл: {file}')
        print('- ' * 7)
        full_file_path = os.path.join(dirpath, file)
        # full_file_path = os.path.join(os.path.abspath(os.path.dirname(__file__)))
        # formatted_time = time.strftime("%d.%m.%Y %H:%M", time.localtime(filetime))
        print(f'Расположение файла: {full_file_path}')
        secs = os.path.getmtime(full_file_path)
        file_time = time.gmtime(secs)
        print(f'Последнее изменение: {file_time[2]}.{file_time[1]}.{file_time[0]} {file_time[3]}:{file_time[4]}') # '%d.%m.%Y %H:%M' | datetime.fromtimestamp(mktime(file_time))
        print(f'Размер файла: {os.path.getsize(file)} байт')
        print(f'Родительская директория: {os.path.dirname(file)}')