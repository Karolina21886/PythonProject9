import random as r

class Student:  # 1 usage new # Уху… студент отримав перші гроші!!!)))
    def __init__(self, name):
        self.name = name
        self.happy = r.randint(10, 100)
        self.progress = r.randint(0, 10)
        self.money = r.randint(100, 350)
        self.alive = True

    def study(self):
        print("Час для навчання")
        self.happy -= r.randint(1, 50)
        self.progress += r.randint(1, 10)
        self.money -= r.randint(50, 200)  # Витрати на навчання

    def sleep(self):
        print("Час для сну")
        self.happy += r.randint(1, 10)

    def chill(self):# Студент відпочиває. Ой студент грає в азарт.
        print("Час для відпочинку")
        self.happy += r.randint(50, 100)
        self.progress -= r.randint(500, 1000)
        self.money -= r.randint(1000, 500)

    def isAlive(self):  # 1 usage new
        if self.money <= 0:
            print("Гроші закінчились студент програв гроші»)
            self.alive = False
        elif self.progress <= 1:
            print("Відрахування з інституту")
            self.alive = False
        elif 1 < self.progress < 5:
            print("Ти на грані відрахування. Починай навчатися")
        elif self.progress >= 5:
            print("Відмінно навчаєшся")
            self.alive = False