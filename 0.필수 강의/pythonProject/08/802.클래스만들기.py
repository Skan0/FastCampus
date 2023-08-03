class Monster:
    def __init__(self,hp,atk,speed):
        self.hp = hp
        self.atk = atk
        self.speed = speed
    def say(self):
        print("나는 몬스터다!")
    def decrease_health(self,num):
        self.hp-=num
    def get_health(self):
        return self.hp
    
goblin = Monster(800,1120,300)
wolf = Monster(1500,200,350)
goblin.say()
