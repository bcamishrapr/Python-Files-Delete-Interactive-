#AUTHOR: PRASOON MISHRA
import os
from tkinter import *
import time
import shutil
from time import strftime

base_path = '/home/prasoon/logs'
target1  = '/home/prasoon/backups'

#Defining Function for deleting files
def remove_files(dir_path, n):
   # dir_path = dirpath.get()
   # n = number.get()
    all_files = os.listdir(dir_path)
    now = time.time()
    n_days = n * 86400
    for f in all_files:
        file_path = os.path.join(dir_path, f)
        print ("File-Path is", file_path)
        if not os.path.isfile(file_path):
            continue
        if os.stat(file_path).st_mtime < now - n_days:
            os.remove(file_path)
            print("Deleted ", f)
#Defining Function for copying files
def copy_files(dir_path, n, target):
    
    all_files = os.listdir(dir_path)
    now = time.time()
    n_days = n * 86400
    for f in all_files:
        file_path = os.path.join(dir_path, f)
        #print ("File-Path is", file_path)
        if not os.path.isfile(file_path):
            continue
        if os.stat(file_path).st_mtime < now - n_days:
            #target = '/home/prasoon/backups'

            shutil.copy(file_path, target)
            dest_file_path = os.path.join(target , f)
            print ("Files to be Copied is:", dest_file_path)



#copy_files(base_path, 10 , target1)

#remove_files(base_path, 30)
app = Tk()
app.geometry("700x700")
app.title("Inter-active Files Delete Console---Made-By-PRASOON MISHRA")
heading = Label(text="Python Files Delete APP",bg="green",fg="black",font="10",width="500",height="3")
heading.pack()

L1 = Label(app, text="Enter the Location from file to be Deleted")
L1.pack( side = RIGHT)
L1.place(x=15,y=100)


L2 = Label(app, text="How many days old files")
L2.pack( side = RIGHT)
L2.place(x=15,y=200)

filelocation = Label(text="File-Location :")
filelocation.place(x=15,y=80)

days = Label(text="Days :")
days.place(x=15,y=180)

backup = Label(text="Backup-Location :")
backup.place(x=15,y=370)

dir_path = StringVar()
#This Is Used to set Default Value for dir_path variable
dir_path.set("/home/prasoon/logs")


n = IntVar()
#This Is Used to set Default Value for n variable
n.set(20)
#print ("Days Value is", n.get())

dest_path = StringVar()
dest_path.set("/home/prasoon/backups")

backuplocation_entry = Entry(textvariable=dest_path,width="30")
backuplocation_entry.place(x=15,y=390)



filelocation_entry = Entry(textvariable=dir_path,width="30")
filelocation_entry.place(x=15,y=150)

days_entry = Entry(textvariable=n,width="30")
days_entry.place(x=15,y=250)



r1 = Radiobutton(app,text="Backup",command=lambda: copy_files(dir_path.get(), n.get(), dest_path.get()),width="20",height="2",bg="green")
r1.pack(side = LEFT)
r1.place(x=15,y=330)


#Usually,When you run func with args in button then it can runs without waiting for button to be pressed
#lambda is used to prevent the func to be hold until Confirm button is not pressed,

button = Radiobutton(app,text="Delete",command=lambda: remove_files(dir_path.get(), n.get()),width="20",height="2",bg="red")
button.place(x=400,y=330)


##button = Button(app,text="Confirm",command=lambda: remove_files(dir_path.get(), n.get()),width="30",height="2",bg="grey")
##button.place(x=15,y=450)


# Button for closing
exit_button = Button(app, text="Exit", command=app.destroy,width="25",height="2",bg="white")

#exit_button.place(x=400,y=450, anchor=SE)
exit_button.place(relx=1.0, rely=1.0, anchor=SE)




mainloop()


