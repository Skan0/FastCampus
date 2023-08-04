class Monster:
    def __init__(self,hp,atk,speed):
        self.hp = hp
        self.atk = atk
        self.speed = speed
    def decrease_health(self,num):
        self.hp-=num
    def get_health(self):
        return self.hp
goblin = Monster(800,120,300)
goblin.decrease_health(100)
print(goblin.get_health())

wolf = Monster(1500,200,350)
wolf.decrease_health(1000)
print(wolf.get_health())