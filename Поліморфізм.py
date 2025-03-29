#Поліморфізм
class Animal:# new
    def sound(self):# new*
        pass #пустий код
class DogAnimal:# new
    def sound(self):# new*
        return "Гав"
class CatAnimal:# new
    def sound(self):# new*
        return "Мяу"
class CowAnimal:# new
    def sound(self):# new*
        return "Му"


def speak(an): # new
    print(an.sound())
a1=Dog()
a2=Cat()
a3=Cow()
speak(a1)
speak(a2)
speak(a3)



# Робота 2
class Pay:
    def process(self,money):
        pass
class Credit(Pay):
    def process(self,money):#new
#return"Оплата "str (money) карткою"
#class Cash(Pay):#new


#Iнкапсуляція

class Dog: # new
    def __init__(self,name):
        self.name=name
dog1=Dog("Бані")
#print(dog1.name)

#2) private
class Dog: # new
    def __init__(self,name): # new*
        self.name=name
        self.__age=2
    def info(self): #new*
        return self.__age
  #  dog1=Dog("Бані")
 #   print(dog1.info())
 #3) protected
 class Dog:#new*
#    def __init__(self,name):#new*
#         self._bread="бульдог"
#class D(Dog):#
#   def info(self):
#        return "Це щеня породи"+self._breed
#dog1=D("Бані")
#print(dog1.info())

class Person: #new *
def init__(self, name, age, salary):# new *
    self.name=name  # публічний атрибут
    self.age=age  # захищений
    self__salary=salary # приватний
#1
def info(self): new *
    print("Вітаю! Мене звати", self.name)
    self._infoAge()
self.infoSalary()
def _infoAge(self):#new *
    print('Miñ вік', self._age))
def _infoSalary(self):# new *
    print('Моя 3П', self.__salary)

class Employee(Person):#new*
 def __init__(self, name, age, salary, pos): new *
    super().__init__(name,age,salary)
    self.pos=pos
    def printInfo(self): new *
    print('Моя посада', self.pos)
    print('Miù вік', self._age)
    print('Моя 3П', self.__salary)
#human=Person(name= 'Олеся', age=20, salary=20000'касир')
#emp=Employee(name='Петро' , age=25,salary=1000000'стоматолог')
#print(human.name)

# Самостійна робота
import random as r
class Character:# new *
    def __init__(self, name, health): #new *
        self.__name=name
        self.__health-r.randint ( a= 0, b= 100)
    def infoName (self):# new *
        return self.__name
    def infoHP(self):# new *
        return self.__health
    def attack(self): #new *
        pass
    def take_dagame(self) :# new *
        self.__health-=r.randint ( a: 0, b: 10)
    def is_alive (self): #new *
     return self.__health>0
    def str(self): 3new *
        return self.__name +" моє здоров'я: "+str (self.__health





