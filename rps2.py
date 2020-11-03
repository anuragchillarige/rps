import random

playerOneScore = 0
playerTwoScore = 0

playerTurn = 0

class Player():
	def __init__(self,nameIn):
		self.nameIn = nameIn

	def roll(self):
		global playerTurn
		playerTurn += 1

		userChoice = input("Enter r, p, or s\n")

		if playerTurn % 2 != 0:
			global playerOneScore
			playerOneScore += int(compRoll(userChoice, self.nameIn))

def compRoll(choiceIn, person):

	#Determining If user or Computer Won
	if compChoice == choiceIn:
		print(f'{person} has tied with the computer!')
		return int(0)

	if compChoice == "r" and choiceIn == "p":
		print(f'{person} has gained a point!')
		return int(1)

	if compChoice == "r" and choiceIn == "s":
		print(f'{person} has lost!')
		return int(0)

	if compChoice == "p" and choiceIn == "r":
		print(f'{person} has lost!')
		return int(0)

	if compChoice == "p" and choiceIn == "s":
		print(f'{person} has gained a point!')
		return int(1)

	if compChoice == "s" and choiceIn == "r":
		print(f'{person} has gained a point!')
		return int(1)

	if compChoice == "s" and choiceIn == "p":
		print(f'{person} has lost!')
		return int(0)

def runGame():
	playerOne = Player("Anurag")
	playerTwo = Player("Bob")

	while True:


		if playerOneScore == 3 or playerTwoScore == 3:
			if playerOneScore == 3: 
				print("Player 1 Won")
			if playerTwoScore == 3:
				print("Player 2 Won")

			else:
				playerOne.roll()
				playerTwo.roll()

runGame()

