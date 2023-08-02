class Item:
    def __init__(self,name,price,weight,isdropable):
        self.name = name
        self.price = price
        self.weight = weight
        self.isdropable = isdropable

    def sale(self):
        print(f"[{self.name}] price is [{self.price}]")

    def discard(self):
        if self.isdropable():
            print(f"Throw up [{self.name}]")
        else:
            print(f"Can not throw up [{self.name}]")

class Wearable(Item):
    def __init__(self,name,price,weight,isdropable,effect):
        super().__init__(name,price,weight,isdropable)
        self.effect = effect

    def wear(self):
        print(f"Wear [{self.name}] [{self.effect}]")

class Useable(Item):
    def __init__(self,name,price,weight,isdropable,effect):
        super().__init__(name, price, weight, isdropable)
        self.effect = effect
    def use(self):
        print(f"Used [{self.name}] {self.effect}")

sword = Wearable("이가닌자의검",30000,3.5,True,"체력 5000증가")
sword.wear()
sword.sale()
sword.discard()

potion = Useable("물약",150000,0.1,False,"투명투명해짐")
potion.discard()
potion.sale()
potion.use()