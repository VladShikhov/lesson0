from time import sleep

# part 1
print('Part 1')
sleep(1)
x = 38

print('дратути!')
if x < 0:
    print('Меньше нуля')
print('дотвидания!')
sleep(1)

# part 2
print('Part 2')
sleep(1)
a, b = 10, 5

if a > b:
    print('a>b')

if a > b and a > 0:
    print('успех')

if (a > b) and (a > 0 or b < 1000):
    print('успех')

if 5 < b and b < 10:
    print('успех')
sleep(1)

# part3
print('Part 3')
sleep(1)
if '34' > '123':
    print('успех')

if '123' > '12':
    print('успех')

if [1, 2] > [1, 1]:
    print('успех')
sleep(1)

#part4
print('Part 4')
sleep(1)
if '6' != 5:
    print('успех')
    
if '6' > 5:
    print('успех')

if [5, 6] > 5:
    print('успех')

