class Character:
    def init(self, name, health):
        self.name, self.health = name, max(0, health)

    def take_damage(self, amount):
        self.health = max(0, self.health - amount)
        print(f"{self.name}: - {amount}  Рівень життя:, {self.health}  Рівень життя:)

    def is_alive(self):
        return self.health > 0


class Warrior(Character):
    def init(self, name):
        super().init(name, 100)
    def attack(self): print( {self.name})


class Mage(Character):
    def init(self, name):
        super().init(name, 100)
    def attack(self): print(f"{self.name} Використовує магію. Хоче використати магію та вдарити гравця. ОБЕРЕЖНО!!!)

w, m = Warrior("Фелекс"), Mage("Хеката")
w.attack(),m.attack()
m.take_damage(30), print("{m.name} ЖИВИЙ? {m.is_alive()}")
m.take_damage(80), print("{m.name} ЖИВИЙ? {m.is_alive()}")