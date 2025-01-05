import time
import random
import threading

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for _ in range(100):
            random_replenishment = random.randint(50, 500)
            self.balance += random_replenishment
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()

            print(f'Пополнение: {random_replenishment}. Баланс: {self.balance}')
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            random_withdrawing = random.randint(50, 500)
            print(f'Запрос на {random_withdrawing}')
            if random_withdrawing <= self.balance:
                self.balance = self.balance - random_withdrawing
                print(f'Снятие: {random_withdrawing}. Баланс: {self.balance}')
            else:
                print('Запрос отклонён, недостаточно средств')
                self.lock.acquire()
bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')