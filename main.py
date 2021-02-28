print ("You have joined rock, paper, scissors game!")
from random import randint
print('Please enter your move:')
t = ["Rock", "Paper", "Scissors"]
computer = t[randint(0,2)]
player = False
while player == False:
   player = input("Rock, Paper, Scissors?")
   if player == computer:
       print("Tie!")
   elif player == "Rock":
       if computer == "Paper":
           print("Nice Try! You Lost!", computer, "covers", player)
       else:
           print("Wow! You won!", player, "smashes", computer)
   elif player == "Paper":
       if computer == "Scissors":
           print("Tough luck, you lost!", computer, "cut", player)
       else:
           print("Great job! You won!", player, "covers", computer)
   elif player == "Scissors":
       if computer == "Rock":
           print("Almost there, Try Again...", computer, "smashes", player)
       else:
           print("You won!", player, "cut", computer)
   else:
       print("Sorry that is not a valid play. Please check your spelling!")
   player = False
   computer = t[randint(0,2)]
