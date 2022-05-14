class human:
    def __init__(self, energy, maxspeed):
        self.energy = energy
        self.maxspeed = maxspeed

    def refuel(self, amount):
            self.energy += amount

    def walk(self):
        if self.energy > 0:
            print('Walking')
            self.energy -=1
        else:
            print('He is tired')

Artem = human(35, 15)
print(Artem.energy)
print(Artem.maxspeed)

Andrii = human(40, 15)
print(Andrii.energy)
print(Andrii.maxspeed)
print('---------------------')
print(Artem.energy)
Artem.refuel(20)
print(Artem.energy)
print('---------------------')
print(Andrii.energy)
Andrii.walk()
print(Andrii.energy)