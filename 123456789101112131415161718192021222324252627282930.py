import random as r
class Student: # 1 usage new
    def __init__(self, name):
        self.name = name
        self.happy = r.randint(10, 100)
        self.progress = r.randint(0, 10)
        self.alive = True
    def study(self):
        print("Час для навчання")
        self.happy -= r.randint(1, 50)
        self.progress += r.randint(1, 10)
    def sleep(self):
        print("Час для сну")
        self.happy += r.randint(1, 10)
    def chill(self):
        print("Час для відпочинку")
        self.happy += r.randint(50, 100)
        self.progress -= r.randint(5, 10)
    def isAlive(self):# 1 usage new
        if 1 < self.progress < 5:
            print("Ти на грані відрахування. Починай навчатися")
        elif self.progress <= 1:
            print("Відрахування з інституту")
            self.alive = False
        elif self.progress >= 5:
            print("Відмінно навчаєшся")
            self.alive = False