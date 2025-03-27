#Тварини
class Animal:
    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def make_sound(self):
        return "Ця тварина видає звук"

    def __str__(self):
        return f"Я {self.name}, мені {self.age} років, я {self.species}."

    rex = Dog("Рекс", 5, "Німецька вівчарка")
    murka = Cat("Мурка", 3, "Руда")
    print(rex)
    print(rex.make_sound())
    print(murka)
    print(murka.make_sound())


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age, "Собака")
        self.breed = breed

    def make_sound(self):
        return "Гав-гав!"

    def __str__(self):
        return super().__str__() + f" Порода: {self.breed}."


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age, "Кіт")
        self.color = color

    def make_sound(self):
        return "Мяу-мяу!"

    def __str__(self):
        return super().__str__() + f" Колір: {self.color}."

    rex = Dog("Рекс", 5, "Німецька вівчарка")
    murka = Cat("Мурка", 3, "Руда")

#Транспорти
class TransportVehicle:
    def __init__(self, speed, capacity):
        self.speed = speed
        self.capacity = capacity

    def move(self):
        return f"Транспортний засіб рухається зі швидкістю {self.speed} км/год"

    def __str__(self):
        return f"Швидкість: {self.speed} км/год, місткість: {self.capacity} осіб."


class Car(TransportVehicle):
    def __init__(self, speed, capacity, brand):
        super().__init__(speed, capacity)
        self.brand = brand

    def move(self):
        return f"Автомобіль {self.brand} рухається зі швидкістю {self.speed} км/год"

    def __str__(self):
        return super().__str__() + f" Марка: {self.brand}."


class Bicycle(TransportVehicle):
    def __init__(self, speed, capacity, type):
        super().__init__(speed, capacity)
        self.type = type

    def move(self):
        return f"Велосипед ({self.type}) рухається зі швидкістю {self.speed} км/год"

    def __str__(self):
        return super().__str__() + f" Тип: {self.type}."


class Bus(TransportVehicle):
    def __init__(self, speed, capacity, route):
        super().__init__(speed, capacity)
        self.route = route

    def move(self):
        return f"Автобус на маршруті {self.route} рухається зі швидкістю {self.speed} км/год"

    def __str__(self):
        return super().__str__() + f" Маршрут: {self.route}."

    car = Car(120, 5, "Toyota")
    bike = Bicycle(25, 1, "Гірський")
    bus = Bus(80, 50, "№23")
    print(car.move())
    print(car)
    print(bike.move())
    print(bike)
    print(bus.move())
    print(bus)