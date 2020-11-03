#In this program, we will create a 2 player rock paper scissors app
#Both players will play against the computer
#And will gain a point if they win
#First player to 3 points wins

import random
playerOneScore = 0
playerTwoScore = 0

class Player1():
	def __init__(self, nameIn):
		self.nameIn = nameIn

	def roll(self):
		userroll = input(f"\n{self.nameIn}, enter rock, paper or scissors. " +
			"You can also type r, p, or s for ease\n")
		roundScore = computerChoice(userroll, self.nameIn)
		global playerOneScore
		playerOneScore += roundScore
		print(f"{self.nameIn}, your current score is {playerOneScore}.")

	def win(self):
		print(f"Congrats, {self.nameIn}, you won!!! Your prize is...\n\n\nNOTHING!!!")

class Player2():
	def __init__(self, nameIn):
		self.nameIn = nameIn

	def roll(self):
		userroll = input(f"\n{self.nameIn}, enter rock, paper or scissors" +
			". You can also type r, p, or s for ease\n")
		roundScore = computerChoice(userroll, self.nameIn)
		global playerTwoScore
		playerTwoScore += roundScore
		print(f"{self.nameIn}, your current score is {playerTwoScore}.")

	def win(self):
		print(f"Congrats, {self.nameIn}, you won!!! Your prize is...\n\n\nNOTHING!!!")


def computerChoice(choiceIn, person):
	#setting all the variables to a constant
	compChoice = random.choice(['r','p','s'])
	if choiceIn == "rock":
		choiceIn = "r"
	if choiceIn == "paper":
		choiceIn = "p"
	if choiceIn == "scissors":
		choiceIn = "s"

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

def startProg():
	print("WELCOME!!!!!!\nThis is just a program made by anewragg, " +
		"which is me! I just want to utilize the true powers of OOP, so I made this program! Enjoy! :-)\n\n\n")
	print("If you don't know the rules of rock paper scissors, you can type 'Rules'. If not, type 'Start' to get started!")
	while True:
		start = input("")
		if start == "Help":
			helpText()
		if start == "Start":
			getUserInfo()

def getUserInfo():
	name1 = input("Enter Your name, Player 1.\n")
	name2 = input("Enter your name, Player 2.\n")
	print(f"Alright! Let the game begin!")
	runGame(name1,name2)

def helpText():
	print("--RULES--\n" + 
		  "The rules are actually pretty simple. Rock beats paper, paper beats scissors, and scissors beats rock." +
		  "If you match one of those conditions, a point will be rewarded to you. If not, you won't gain a point." + 
		  "If you and the computer make the same choice, it is a tie. No point is rewarded either.")

def runGame(name1,name2):
	while True:
		playerOne = Player1(name1)
		playerTwo = Player2(name2)
		if playerOneScore == 5 or playerTwoScore == 5:
			if playerOneScore == 5:
				playerOne.win()
				break
			else:
				playerTwo.win()
				break
				
		else:
			playerOne.roll()
			playerTwo.roll()

startProg()