#aggregation
class Serigala():
    def __init__(self, hp, power, damage):
        self.hp = hp
        self.power = power
        self.damage = damage

    def description(self):
        print(f"Serigala dengan hp : {self.hp}, power {self.power}, damage {self.damage}")


    def attack(self, enemy):
        enemy.hp = enemy.hp - (self.power + self.damage)
        print(f"Serigala menyerang dengan kekuatan {self.power + self.damage}")



class Kelinci():
    def __init__(self, hp):
        self.hp = hp

    def description(self):
        print(f"kelinci memiliki hp : {self.hp}")

    def run(self):
        print(f"kelinci lari")

    def hiding(self):
        print("kelinci bersmebunyi")

s1 = Serigala(10, 15, 45)
s2 = Serigala(10, 60, 45)
k1 = Kelinci(87)

s1.description()
k1.description()

s1.attack(k1)
k1.description()
s2.attack(k1)

k1.description()
