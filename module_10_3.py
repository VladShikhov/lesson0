from threading import Thread, Lock
import random
from time import sleep


class Bank:

    def __init__(self, balance, lock):
        self.balance = balance
        self.lock = lock

    def deposit(self):
        for i in range(100):
            refill = random.randint(50, 500)
            self.balance += refill
            print(f'Пополнение: {refill}. Баланс: {self.balance}')
            if self.balance >= 500 and self.lock.locked() == True:
                self.lock.release()
            sleep(0.001)

    def take(self):
        for i in range(100):
            refill = random.randint(50, 500)
            print(f'Запрос на {refill}')
            if refill <= self.balance:
                self.balance -= refill
                print(f'Снятие: {refill}. Баланс: {self.balance}')
            else:
                print('Запрос отклонен, недостаточно средств')
                self.lock.acquire()
            sleep(0.001)


bk = Bank(0, Lock())

th1 = Thread(target=Bank.deposit, args=(bk,))
th2 = Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
            
            
