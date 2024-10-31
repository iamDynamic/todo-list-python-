from tkinter import *

window = Tk()

window.geometry("500x350")

window.title("Todo0-List")

window.config(bg=("#0077b7"))
def removetask():
    with open("data.txt","w") as f:
        a = f.write("")
def close():
    window.destroy()
def seealldata():
    with open("data.txt","r") as f: 
        readfile = f.read()
    newfile = Toplevel()
    Label(newfile,text=readfile).pack()
tittle = Label(window,text="ToDo-List",font=("Arial",40)).place(x=130,y=20)


RemoveTask = Button(window,text="Remove All Data",bg=("#93081B"),fg=("#fff"),padx=10,pady=10,font=("Arial",10),command=removetask).place(x=320,y=150)

x = StringVar()

entry = Entry(window,width=40,textvariable=x).place(x=130,y=240)

def addtask():
    SavedData = x.get()

    if SavedData == "":
        erroremessege = Toplevel()
        L = Label(erroremessege,text="the input is empty").pack()
    else:
        with open("data.txt","a") as f:
          ADDEDTEXT = f.write(f"\n {SavedData}")
        
 
AddTask = Button(window,text="Add Text",bg=("#04921A"),fg=("#fff"),padx=10,pady=10,font=("Arial",10),command=addtask).place(x=80,y=150)

AddTask = Button(window,text="see all data",bg=("yellow"),fg=("#000"),padx=10,pady=10,font=("Arial",10),command=seealldata).place(x=200,y=150)

close = Button(window,text="close",padx=5,pady=5,bg=("#93081B"),fg=("#fff"),width=20,command=close).place(x=190,y=300)


window.mainloop()