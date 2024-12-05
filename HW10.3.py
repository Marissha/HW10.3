import threading
import random
import time
from threading import Thread

lock = threading.Lock()

class Bank():
    balance = 0
    lock = threading.Lock()


    def deposit(self):
        for i in range(100):
            if self.balance >= 500 and self.lock.locked():
                time.sleep(0.01)
                self.lock.release()
            a = random.randint(50, 500)
            self.balance += a
            print(f'Пополнение: {a}. Баланс: {self.balance}.')
            time.sleep(0.1)

    def take(self):
        self.lock.acquire()
        for i in range(100):
            a = random.randint(50, 500)
            print(f'Запрос на {a}')
            time.sleep(0.01)
            if self.balance >= a:
                self.balance -= a
                print(f'Снятие: {a}. Баланс: {self.balance}')
                time.sleep(0.01)
            else:
                print('Запрос отклонен, недостаточно средств.')
                time.sleep(0.1)
                self.lock.acquire()

bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))
th1.start()
th2.start()
th1.join()
th2.join()
print(f'Итоговый баланс: {bk.balance}')