class Building:
    total = 0

    def __init__(self, object):
        self.object = object
        Building.total += 1


build = [Building(f'Объект класса Building №{i + 1}') for i in range(40)]
for i in range(len(build)):
    print(build[i].object)
print()
print(f'Всего построено: {Building.total} зданий')