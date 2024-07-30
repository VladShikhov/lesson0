def is_prime(func):
    def wrapper(dig1, dig2, dig3):
        result = func(dig1, dig2, dig3)
        count = 0
        for i in range(1, result+1):
            if result % i == 0:
                count += 1
        if count == 2:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

@is_prime
def sum_three(dig1, dig2, dig3):
    sum_d = dig1 + dig2 + dig3
    return sum_d

result = sum_three(2, 3, 6)
print(result)