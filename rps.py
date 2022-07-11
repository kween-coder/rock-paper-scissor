#Rock paper scissors game
import random

#function to determine the winner
def rps(p1_turn,p2_turn):
	if ((p2_turn == 'P' and p1_turn == 'R') or (p2_turn == 'R' and p1_turn == 'P')):
		print("Paper wins")
		result = "P"

	elif ((p2_turn == 'R' and p1_turn == 'S') or (p2_turn == 'S' and p1_turn == 'R')):
		print("Rock  wins")
		result = "R"

	elif ((p2_turn == 'P' and p1_turn == 'S') or (p2_turn == 'S' and p1_turn == 'P')):
		print("Scissor wins")
		result = "S"

	else:
		result = 'Draw'


	if result == 'Draw':
		print("It's a draw")
	elif result == p2_turn:
		print("Computer wins.....!!")
	else:
		print("You won...!!")


#Basic Intro 
print("Welcome to the Game of Rock-Paper-Scissors")
print("We'll use R for Rock,\n"+"P for Paper,\n"+"S for Scissor")
print("Winning Rules of the Rock paper scissor game as follows: \n"+"Rock vs paper->paper wins \n"
								+ "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
print("There are two types of modes - ,\n"+"1. Single player mode ,\n"+"2. Two Player mode")
choice = int(input("Select your mode: \n")) #selecting the mode to play
def game(choice):
	p1_turn = input("Enter a choice (rock, paper, scissors): ")
	if ((p1_turn != 'S') or (p1_turn != 'P') or (p1_turn != 'R')):
		print("Enter valid choice.")
		break


	if choice == 1:
		action = ['R','P','S']
		p2_turn=random.choice(action)
		print("Computer's choice = ",p2_turn)

		rps(p1_turn,p2_turn)

	else:
		p2_turn = input("Enter a choice (rock, paper, scissors): ")
		rps(p1_turn,p2_turn)



game(choice)

ans = input("Do you want to play again: Y/N\n")
 
if ans == 'Y':
	choice = int(input("Select your mode: \n")) #selecting the mode to play
	game(choice)

else:
	print("Thank you for playing")



	






