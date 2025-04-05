#Linda Huynh 
#imports random 
import random

#Assign secret number to a random number
secretNum = random.randint(1,10)

print()
print("The computer has selected a secret number from 1 to 10 inclusive.")
print("You have to guess it in as few tries as possible.")
print("To do this enter a number between 1 and 10 and the computer will")
print("tell you if your guess is lower than, higher than, or equal to the secret number.")
print("When you guess the correct number the computer will tell you")
print()

#for loop for 4 tries 
for i in range(4): 
    #takes user input for a number
    userinput = input("Select a number (1-10): ") 
    #checks if userinput is less than secret number and will print your number is less than secret number
    if int(userinput) < secretNum: 
        print("Your number is less than secret number") 
        #checks if userinput is greater than secret number and will print your number is greater than secret number
    elif int(userinput) > secretNum: 
        print("Your number is more than secret number")
        #default to this statement when the number is equal to.
    else: 
        print("You guessed the correct number") 
        #This break statement stops the for loop when the answer is correct.
        break 

