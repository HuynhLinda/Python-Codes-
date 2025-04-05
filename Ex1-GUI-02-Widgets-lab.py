#Linda Huynh 
try:
    import Tkinter as tk
except:
    import tkinter as tk
import tkinter
from tkinter import *


root = tk.Tk()
root.geometry('300x300')
root.config(bg='white')
root.title('Color')

entry = tk.Entry(root)
entry.pack()
#I assign the root to the entry command 

label = tk.Label(root, text='Enter "red" or "blue"')
label.pack()
#I made a label to let the user know what to enter

def enter_button():
  
    text = entry.get()

    label.config(text=text)
 
    if text == "red":
        root.config(bg="red")
    elif text == "blue":
        root.config(bg="blue")
    else:
        root.config(bg="white")
#I made an If statement to define what the program does when red or blue or nothing is enter

button = tk.Button(root, text="Enter", command=enter_button)
button.pack()
#I made a button to finalize the user input and show what happens to the background once the text is entered

root.mainloop()