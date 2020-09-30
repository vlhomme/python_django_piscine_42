class HotBeverage():
    price = 0.30
    name = "hot beverage"

    def description(self):
        return ("Just some hot water in a cup.")
    
    def __str__(self):
        return('name : ' + self.name + '\nprice : ' + str(self.price) + '\ndescription : ' + self.description())

class Coffee(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self)
        self.price = 0.40
        self.name ='coffee'
    def description(self):
        return("A coffee, to stay awake.")

class Tea(HotBeverage):
    name = 'tea'

class Chocolate(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self)
        self.price = 0.50
        self.name ='chocolate'
    def description(self):
        return("Chocolate, sweet chocolate...")

class Cappuccino(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self)
        self.price = 0.45
        self.name ='cappuccino'
    def description(self):
        return("Un po' di Italia nella sua tazza!")

if __name__ == '__main__':
    a = HotBeverage()
    print(a)
    b = Coffee()
    print(b)
    c = Tea()
    print(c)
    d = Chocolate()
    print(d)
    e = Cappuccino()
    print(e)