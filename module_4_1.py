from fake_math import divide as fake_d
from true_math import divide as true_d


a, b = int(input('First_num: ')), int(input('Second_num: '))
result_from_fake = fake_d(a, b)
result_from_true = true_d(a, b)
print(f'fake_math: {result_from_fake}\ntrue_math: {result_from_true}')
