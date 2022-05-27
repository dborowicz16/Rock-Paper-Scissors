import random

print("Let's play rock, paper, scissors!")

# Creates a user class that holds total points and amount user wagers 
class user:
    totalPoints = 50
    wager = 0

# Creates a user object that is an instance of the user class
user = user()

# Logic for losing points
def losePoints():
    user.totalPoints = user.totalPoints - user.wager

# Logic for winning points
def winPoints():
    user.totalPoints = user.totalPoints + user.wager 

# Gives the user the option to continue playing or stop
def playAgain():
    decision = input("Do you want to play again?")

    if decision == "yes":
        choice()
    elif decision == "no":
        print("You finished with " + str(user.totalPoints) + " points! Thanks for playing!")

# User makes a wager & move. Points are added/subtracted based off result & user is given option to play again or not
def choice():
    user.wager = int(input("How many points do you want to wager?"))

    decision = input("Make a choice! Rock, paper, or scissors?")

    computerChoices = ["rock", "paper", "scissors"]
    computerChoice = random.choice(computerChoices)

    #Field user input and decide if winner or loser based on possible outcomes of user selection

    if decision == "rock":
        if computerChoice == "rock":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You tie!")
            losePoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()
        elif computerChoice == "paper":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You lose!")
            losePoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()
        elif computerChoice == "scissors":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You win!")
            winPoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()

        
    elif decision == "scissors":
        if computerChoice == "rock":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You lose!")
            losePoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()
        elif computerChoice == "paper":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You win!")
            winPoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()
        elif computerChoice == "scissors":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You tie!")
            losePoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()

    elif decision == "paper":
        if computerChoice == "rock":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You win!")
            winPoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()
        elif computerChoice == "paper":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You tie!")
            losePoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()
        elif computerChoice == "scissors":
            print("You picked " + decision + ". The computer picked " + computerChoice + ". You lose!")
            losePoints()
            print("You have " + str(user.totalPoints) + " points!")
            playAgain()
    
choice()