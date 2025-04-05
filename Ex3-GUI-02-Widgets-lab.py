#Linda Huynh

import tkinter as tk


root = tk.Tk()
root.geometry('300x300')
root.config(bg='white')
root.title('color Changer')

#This will be the list box 
listbox = tk.Listbox(root)

# I made a list of colors
colors = ["red", "green", "blue", "yellow", "orange", "purple"]
for color in colors:
    listbox.insert(tk.END, color)


# This will change the background color 
def change_color():
    # get the selected color from the listbox
    selected_color = listbox.get(listbox.curselection())
    # change the window background color
    root.config(bg=selected_color)
    # update the label text
    label.config(text=selected_color)

# This label will tell what color will be displayed once the clicked on
label = tk.Label(root, text="Select a color")

# This button will change the button 
button = tk.Button(root, text="Change color", command=change_color)

listbox.pack()
label.pack()
button.pack()


root.mainloop()

