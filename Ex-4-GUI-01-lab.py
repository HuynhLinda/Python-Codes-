#Linda Huynh 


import tkinter as tk
from tkinter import *
from tkinter import messagebox
import random



window= tk.Tk()
window.geometry("300x300")
window.title("buttons")

random_number=str(random.randint(0,100))
#I defined the function to a string and random.randint to generate a random number 

def click_1():
    button.config(text="The first button has been clicked")
    #I used def to use the function later, when the button is clicked it will display this text
  
def click_2():
    random_numb= str(random.randint(0,100))
    button_2.config(text=random_number)
#I used def to use the function later, when the button is clicked it will choose a random number from 1-100
  
button = tk.Button(window, text = "First Button", width=35, height=5, command=click_1)

button_2 = Button(window, text="Second Button",width=40, height =7, bg='red',fg='white',command= click_2)
#These two functions will display the text on the window as well as have a fixed width and length
#Then I use command and assignt each function to a def function to preform accordingly 


button.pack(side=tk.LEFT)
button_2.pack(side=tk.RIGHT)
#I used the side function to determine where the buttons will go 
window.mainloop()
