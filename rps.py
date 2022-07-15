#Rock paper scissors game
import random


def rps(p1_turn,p2_turn,p1_name,p2_name):

	'''This Function takes the names and the turns of the players and decides who wins the game based on the rules. 
		Based on the rules the element that wins is selected and the player who chose the element is the winner'''
	a=p1_turn.upper()
	b=p2_turn.upper()
	p=p1_name
	q=p2_name

	if ((b == 'P' and a == 'R') or (b == 'R' and a == 'P')):
		print("Paper wins")
		result = "P"

	elif ((b == 'R' and a == 'S') or (b == 'S' and a == 'R')):
		print("Rock  wins")
		result = "R"

	elif ((b == 'P' and a == 'S') or (b == 'S' and a == 'P')):
		print("Scissor wins")
		result = "S"

	else:
		result = 'Draw'

#checking which player wins
	if result == 'Draw':
		print("It's a draw")
	elif result == b:
		if s != True:
			print("Computer wins.....!!")
		else:
			print(q,"wins.....!!")
	else:
		if s != True:
			print(p,"wins...!!")
		else:
			print(p,"wins.....!!")


#asking for a rematch
	ans = input("Do you want to play again: Y/N\n").upper()
	if ans == 'Y':
		#selecting the mode to play
		choice = int(input("Select your mode: \n")) 
		game(choice)

	else:
		print("Thank you for playing")


def game(choice):
	'''This function handles the two modes available for the game, taking the choice as input. Based on the input, the inteded
		inputs for the game is taken and respective functions are called'''

	action = ['R','P','S']
	#Single player mode
	if choice == 1:
		p1_name=input("Player 1, Enter your name: ")
		p1_turn = input("Enter a choice (rock, paper or scissors): ").upper()
		#handling invalid input
		if p1_turn not in action:
			raise Exception("Enter only Rock,Paper or Scissors")

		p2_turn=random.choice(action)
		p2_name='Computer'
		p2_turn.upper()

		print("Computer's choice = ",p2_turn)

		rps(p1_turn,p2_turn,p1_name,p2_name)
		

	#multiplayer mode	
	elif choice == 2:
		s=False
		p1_name=input("Player 1, Enter your name: ")
		p1_turn = input(" Enter a choice (rock, paper, scissors): ").upper()

		#handling invalid input
		if p1_turn not in action:
			#print("Invalid input")
			raise Exception("Enter valid input")

		p2_name=input("Player 2, Enter your name: ")	
		p2_turn = input("enter a choice (rock, paper, scissors): ").upper()
		if p2_turn not in action:
			#print("Invalid input")
			raise Exception("Enter valid input")

		rps(p1_turn,p2_turn,p1_name,p2_name)
		
	#handling invalid input
	else:
		raise Exception("Enter only 1 or 2")
		print("Invalid input")
		exit()


	#Basic Intro 
	print("Welcome to the Game of Rock-Paper-Scissors \n We'll use R for Rock,\n P for Paper,\n S for Scissor \n \n Winning Rules of the Rock paper scissor game as follows: \n Rock vs paper->paper wins \n Rock vs scissor->Rock wins \n paper vs scissor->scissor wins \n")
	print("There are two types of modes - \n1. Single player mode \n2. Two Player mode")

	#selecting the mode to play
	choice = int(input("Select your mode: \n")) 
	s=True
	result=''

	game(choice)