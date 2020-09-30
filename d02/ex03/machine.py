import random
from beverages import *

class CoffeeMachine():
    use = int()
    def __init__(self):
        self.use = 0

    class EmptyCup(HotBeverage):
        price = 0.90
        def description(self):
            return("An empty cup?! Gimme my money back!")

    class BrokenMachineException(Exception):
        def __init__(self, str = 'This coffee machine has to be repaired.'):
            super().__init__(self, str)

    def repair(self):
        self.use = 0

    def serve(self, Beverage):
        self.use = self.use + 1
        if self.use > 10:
            raise self.BrokenMachineException()
        if random.choice([0, 1]) == 0:
            return self.EmptyCup()
        else:
            return Beverage()

if __name__ == "__main__":
	for i in range(2):
		try:
			machine = CoffeeMachine()

			print(machine.serve(HotBeverage))
			print(machine.serve(Coffee))
			print(machine.serve(Coffee))
			print(machine.serve(Coffee))
			print(machine.serve(Tea))
			print(machine.serve(Tea))
			print(machine.serve(Cappuccino))
			print(machine.serve(Coffee))
			print(machine.serve(Tea))
			print(machine.serve(Tea))
			print(machine.serve(Cappuccino))
		except Exception as e:
			print(e)
			machine.repair()