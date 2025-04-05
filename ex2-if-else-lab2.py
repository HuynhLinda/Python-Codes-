#Linda Huynh 
#make a list of animals 
Animals = ["Fish","Tarantula","Snake","Octopus"]

#tell the user to choose an animal
print("Choose one of the following animals and remember")
userinput = input("Type 1 for fish, type 2 for tarantula, type 3 for snake, type 4 for octopus ") 

#user select will assign the animals 
UserSelect = Animals[int(userinput)-1] 

#asking a question to figure out the animal 
firstinput = input("Does your animal live in water?(Yes/No): ")

#asking if the animal lives in water to eliminate other animals
if firstinput.lower() == "yes": 
    waterinput = input("Does your animal have limbs?(Yes/No): ") 
    #ask the user if the animal is in water 
    if waterinput.lower() == "yes": 
        print(f"Im guessing your animal is {Animals[3]}, you put {UserSelect}")
    else: 
        print(f"Im guessing your animal is {Animals[0]}, you put {UserSelect}")

#figuring out if the animal lives on land 
elif firstinput.lower() == "no": 
    Landinput = input("Does your animal have limbs?(Yes/No): ")
    #asking the user if the animal lives on land to conclude 
    if Landinput.lower() == "yes": 
        print(f"Im guessing your animal is {Animals[1]}, you put {UserSelect}")
    else:
        print(f"Im guessing your animal is {Animals[2]}, you put {UserSelect}")