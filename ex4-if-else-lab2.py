#Linda Huynh 
#ask the user if the shape is red 
userinput = input("Is the shape Red?(Yes/No): ") 

#If the user selects yes it narrows half the choices down
if userinput.lower() == "yes": 
    #ask the user if the shape has a circle around it to narrow down the choices half again
    userinput2 = input("Does your shape have a circle around it?(Yes/No): ")

    if userinput2.lower() == "yes":
        #3rd and final question asks the user if the shape has 3 sides  
        userinput3 = input("Does your shape have 3 sides?(Yes/No): ") 
        #if user selects yes it is a red triangle else it is a red octagon 
        if userinput3.lower() == "yes": 
            print("Your shape is a red triangle")
        else: 
            print("Your shape is a red octagon")
    #else statement for no cirlce around shape
    else: 
        #Another 3rd and final question ask the user if the shape has 4 sides 
        userinput3 = input("Does your shape have 4 sides?(Yes/No): ") 
        #if the user selects yes it is a red square else it is a red pentagon 
        if userinput3.lower() == "yes": 
            print("Your shape is a red square")
        else: 
            print("Your shape is a red pentagon")
#else if select user selects no the shape is blue
elif userinput.lower() == "no": 
    #ask user second question if there is a circle around the shape
    userinput2 = input("Does your shape have a circle around it?(Yes/No): ")

    if userinput2.lower() == "yes": 
        #Ask 3rd and final question if the shape has 3 sides
        userinput3 = input("Does your shape have 3 sides?(Yes/No): ") 

        #if the user selects yes then it is a blue triangle else it is an blue octagon
        if userinput3.lower() == "yes": 
            print("Your shape is a blue triangle")
        else: 
            print("Your shape is a blue octagon")

    else: 
        #Another 3rd and final question asking if the shape has 4 sides 
        userinput3 = input("Does your shape have 4 sides?(Yes/No): ") 

        #if user selects yes it is a blue square else it is a blue pentagon 
        if userinput3.lower() == "yes": 
            print("Your shape is a blue square")
        else: 
            print("Your shape is a blue pentagon")
