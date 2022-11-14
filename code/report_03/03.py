class Unit:
    def __init__(self, name, health):
        self.name, self.health = name, health

    def __str__(self):
        return f'{self.name}\t:\t{self.health}'

    def damaged(self, amount):
        remain = self.health - amount
        self.health = remain                    # damage 입은 health update
        if self.health > 0:                          
            return f'{self.name} health : {self.health}'
        else:
            return f'{self.name} destroyed'

class Magician(Unit):                       
    def __init__(self, name, health, energy):   
        super().__init__(name, health)          # unit class 에서 속성을 상속받음
        self.energy = energy                    # Magician class의 별도속성 설정

    def __str__(self):
         return f'{self.name}\t:\t{self.health} ({self.energy})'       

    def skill(self, amount):
        remain = self.energy - amount
        self.energy = remain                    # 감소한 energy update
        if self.energy > 0:
            return f'{self.name} health : {self.energy}'
        else:
            return f'Not enough energy'      