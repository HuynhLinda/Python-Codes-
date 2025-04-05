import random
#Linda Huynh
#print all the choices 
print("Enter your choice of Rock(R), Paper(P), and Scissors(S)")
print("The program will print out it's random choice of Rock, Paper, or Scissors ")
print("The program will compare the choices ")

#use Input to allow the user to choose a variable 
userInput = input('Enter "R","P", or "S":')
print(userInput)

#computer will choose a random number from 0-2 
#each variable is assigned a number 
computer = random.randint(0,2)
if (computer == 0):
  computer = "R"
elif(computer ==1):
  computer = "P"
else:
  computer = "S"
  
  print(computer)

#if the input and computer both choose the same option, it's a tie 
if(userInput == computer):
  print("It's a tie")
