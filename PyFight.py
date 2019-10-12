from random import *
# A python fighting game, me learning casses

class Person:

	def __init__(self, name, health):
		self.name = name
		self.health = health

	def attack(self, enemy):
		damage = randrange(1, 5)
		enemy.health-=damage
		print(f"{self.name} hit {enemy.name} for {damage} points!")

	def print_info(self):
		print(f"{self.name}: {self.health} health")


class Human(Person):
	pass

class Enemy(Person):
	pass


name = input("Name: ")
player = Human(name, randrange(20, 30))
orc = Enemy("Steve", randrange(20, 30))

game = True

while game:
	player.print_info()
	orc.print_info()

	print(f"Attack {orc.name}?")
	val = input()

	if(val == "Y"):
		player.attack(orc)
	orc.attack(player)

	if(orc.health <= 0 or player.health <= 0):
		game = False

if(orc.health > player.health):
	print("You lose!")
else:
	print("You win!")

