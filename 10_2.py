import time
import threading

class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.days = 0
        self.enemies = 100

    # def timer(self):
    #     while True:
    #         time.sleep(1)
    #         self.days += 1
    #         print(f'{self.name} сражается {self.days}..., осталось {self.power} воинов.')

    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemies:
            self.enemies -= self.power
            time.sleep(1)
            self.days += 1
            print(f'{self.name} сражается {self.days}..., осталось {self.enemies} воинов.')

        print(f'{self.name} одержал победу спустя {self.days} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.run()
second_knight.run()

