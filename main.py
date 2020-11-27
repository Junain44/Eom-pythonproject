from tkinter import *
from tkinter import messagebox


window1 = Tk()
window1.title("Client Information")
window1.geometry("200x95")


def log():
    age = age_entry.get()
    ages = int(age)
    if ages < 18:
        messagebox.showerror("Age!", "You Do Not Qualify")
        window1.destroy()
        window2()


# Login button
myButton = Button(window1, text="Login", command=log)
myButton.pack(side=BOTTOM)

# Label name
label1 = Label(window1, text="Age")
# Creating an entry
age_entry = Entry(window1, width=15)

# Placement for labels and entries
label1.pack(side=LEFT)
age_entry.pack(side=LEFT)


def window2():

        window2 = Tk()
        window2.geometry("500x100")

labelfr1 = LabelFrame(window2, text="Entry NUMBERS", pady=10)
labelfr1.pack(fill="both")

#Created Entries
entry=Entry(labelfr1,width = 3)
entry.grid(row=1, column=1, padx=25)
entry=Entry(labelfr1,width = 3)
entry.grid(row=1, column=2, padx=25)
entry=Entry(labelfr1,width = 3)
entry.grid(row=1, column=3, padx=25)
entry=Entry(labelfr1,width = 3)
entry.grid(row=1, column=4, padx=25)
entry=Entry(labelfr1,width =3)
entry.grid(row=1, column=5, padx=25)
entry=Entry(labelfr1,width =3)
entry.grid(row=1, column=6, padx=25)



window1.mainloop()
