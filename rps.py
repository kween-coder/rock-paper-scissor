#Rock paper scissors game
import random

#function to determine the winner
def rps(p1_turn,p2_turn):
	a=p1_turn.upper()
	b=p2_turn.upper()

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
		print("Computer wins.....!!")
	else:
		print("You won...!!")

#asking for a rematch	
	ans = input("Do you want to play again: Y/N\n").upper()
	if ans == 'Y':
		choice = int(input("Select your mode: \n")) #selecting the mode to play
		game(choice)

	else:
		print("Thank you for playing")


#Basic Intro 
print("Welcome to the Game of Rock-Paper-Scissors")
print("We'll use R for Rock,\n"+"P for Paper,\n"+"S for Scissor")
print("Winning Rules of the Rock paper scissor game as follows: \n"+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
print("There are two types of modes - ,\n"+"1. Single player mode ,\n"+"2. Two Player mode")

#selecting the mode to play
choice = int(input("Select your mode: \n")) 
def game(choice):

	action = ['R','P','S']
	if choice == 1:#Single player mode

		p1_turn = input("Enter a choice (rock, paper, scissors): ").upper()
		#handling invalid input
		if p1_turn not in action:
			print("Invalid input")
			exit()

		p2_turn=random.choice(action)
		p2_turn.upper()

		print("Computer's choice = ",p2_turn)

		rps(p1_turn,p2_turn)

	elif choice == 2:#multiplayer mode
		p1_turn = input("Enter a choice (rock, paper, scissors): ").upper()
		
		#handling invalid input
		if p1_turn not in action:
			print("Invalid input")
			exit()
			
		p2_turn = input("Enter a choice (rock, paper, scissors): ").upper()
		if p2_turn not in action:
			print("Invalid input")
			exit()
	
		rps(p1_turn,p2_turn)

	else:#handling invalid input
		print("Invalid input")
		exit()



game(choice)




	






