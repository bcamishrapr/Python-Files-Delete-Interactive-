#AUTHOR: PRASOON MISHRA
import os
from tkinter import *
import time
base_path = '/home/prasoon/logs'

def remove_files(dir_path, n):
   # dir_path = dirpath.get()
   # n = number.get()
    all_files = os.listdir(dir_path)
    now = time.time()
    n_days = n * 86400
    for f in all_files:
        file_path = os.path.join(dir_path, f)
        if not os.path.isfile(file_path):
            continue
        if os.stat(file_path).st_mtime < now - n_days:
            os.remove(file_path)
            print("Deleted ", f)

#remove_files(base_path, 30)
app = Tk()
app.geometry("700x700")
app.title("Inter-active Files Delete Console---Made-By-PRASOON MISHRA")
heading = Label(text="Python Files Delete APP",bg="red",fg="black",font="10",width="500",height="3")
heading.pack()

filelocation = Label(text="File-Location :")
days = Label(text="Days :")

filelocation.place(x=15,y=70)
days.place(x=15,y=140)

dir_path = StringVar()
n = IntVar()
#print ("Days Value is", n.get())

filelocation_entry = Entry(textvariable=dir_path,width="30")
days_entry = Entry(textvariable=n,width="30")

filelocation_entry.place(x=15,y=100)
days_entry.place(x=15,y=180)

#Usually,When you run func with args in button then it can runs without waiting for button to be pressed
#lambda is used to prevent the func to be hold until Confirm button is not pressed,

button = Button(app,text="Confirm",command=lambda: remove_files(dir_path.get(), n.get()),width="30",height="2",bg="grey")
button.place(x=15,y=220)



mainloop()


