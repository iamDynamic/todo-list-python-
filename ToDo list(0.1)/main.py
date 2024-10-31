from tkinter import *

def Clicked():
    TextValue = input.get()
    print(TextValue)
    label = Label(Root,text=TextValue,bg=("lightblue"))
    label.pack()

Root = Tk()
Root.geometry("500x500")

input = Entry(Root)
submit = Button(Root,text="Submit",command=Clicked)


input.pack()
submit.pack()
Root.mainloop()