from tkinter import *
from random import sample
from tkinter import messagebox

root = Tk()
root.geometry("500x200")

labelfr1 = LabelFrame(root, text="Entry Numbers", pady=10)
labelfr1.pack(fill="both")

#Created Entries
entry1=Entry(labelfr1,width = 3)
entry2=Entry(labelfr1,width = 3)
entry3=Entry(labelfr1,width = 3)
entry4=Entry(labelfr1,width = 3)
entry5=Entry(labelfr1,width =3)
entry6=Entry(labelfr1,width =3)

#Created Grids
entry1.grid(row=1, column=1, padx=25)
entry2.grid(row=1, column=2, padx=25)
entry3.grid(row=1, column=3, padx=25)
entry4.grid(row=1, column=4, padx=25)
entry5.grid(row=1, column=5, padx=25)
entry6.grid(row=1, column=6, padx=25)

def user_entries():
    int1 = int(entry1.get())
    int2 = int(entry2.get())
    int3 = int(entry3.get())
    int4 = int(entry4.get())
    int5 = int(entry5.get())
    int6 = int(entry6.get())

    List = [int1, int2, int3, int4, int5, int6]
    return List

def random_list():
    random_list = sample(range(1,49),7)
    random_list.sort()
    labelshow.configure(text=random_list)

    counter = 0
    for numbers in user_entries():
        if numbers in random_list:
            counter += 1
        if counter <= 1:
            messagebox.showinfo("You", " won nothing ")

        elif counter == 2:
            messagebox.showinfo("You won R20")

        elif counter == 3:
            messagebox.showinfo("You won R100")

        elif counter == 4:
            messagebox.showinfo("You won R2,384.00")

        elif counter == 5:
            messagebox.showinfo("You won R2,384.00")

        elif counter == 6:
            messagebox.showinfo("You won R10,000 000.00")

click_btn =Button(root, text="press", command=random_list)
click_btn.place(x = 15, y = 135)

click_btn.configure(command=random_list)

labelnum=Label(root, text="Lotto Numbers!")
labelnum.place(x = 10 , y = 85)

labelshow=Label(root)
labelshow.place(x = 130, y = 85)

root.mainloop()




















