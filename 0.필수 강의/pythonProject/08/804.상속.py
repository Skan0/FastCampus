# 상속
# 클래스들에 중복된 코드를 제거하고 유지보수를 쉽게 하기 위해서 사용
class Monster:
    def __init__(self,name,health,attack):
        self.name = name
        self.health = health
        self.attack = attack
    def move(self):
        print(f"[{self.name}] 지상에서 이동하기")

class Wolf(Monster):
    pass
class Goblin(Monster):
    pass
class Shark(Monster):
    def move(self):
        print(f"[{self.name}] 물에서 헤엄치기")
class Dragon(Monster):
    def move(self):
        print(f"[{self.name}] 날기")

wolf = Wolf("울프", 1500,200)
wolf.move()
shark = Shark("상어", 3000,400)
shark.move()
dragon = Dragon("용", 8000,1000)
dragon.move()