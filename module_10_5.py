import multiprocessing
from datetime import datetime


def read_info(name):
    all_data = []
    f = open(name, 'r')
    while True:
        l = f.readline()
        all_data.append(l)
        if l == '':
            break
    f.close()


files_list = [f'file {i}.txt' for i in range(1, 5)]

# линейный запуск

start = datetime.now()
for file in files_list:
    read_info(file)
end = datetime.now()
print(end-start, '(линейный)')

# многопроцессорный запуск

if __name__ == '__main__':
    start = datetime.now()
    with multiprocessing.Pool(processes=6) as pool:
        pool.map(read_info, files_list)
    end = datetime.now()
    print(end-start, '(многопроцессорный)')