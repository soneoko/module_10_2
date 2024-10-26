from threading import Thread
from time import sleep
class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemies = 100
        for i in range(1, 100 // self.power):
            enemies -= self.power
            sleep(1)
            print(f'{self.name} сражается {i} ..., осталось {enemies} воинов.')
        if enemies != 0:
            sleep(1)
            print(f'{self.name} сражается {i + 1} ..., осталось {0} воинов.')
            print(f'{self.name} одержал победу спустя {i + 1} дней(дня)!')
        else:
            print(f'{self.name} одержал победу спустя {i} дней(дня)!')

first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print('Все битвы закончились!')
