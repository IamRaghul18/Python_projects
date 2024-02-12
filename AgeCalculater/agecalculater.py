#PACKAGES#
from tkinter import *
from datetime import date

#GUI#
root=Tk()
root.geometry('700x700')
root.resizable(False,False)
root.title("AgeCalculater")

#PHOTO#
image_path = "D:\git_projects\Python_projects\AgeCalculater\Age calculator  .png"
photo=PhotoImage(file=image_path)
myimage=Label(image=photo)
myimage.pack(padx=15,pady=15)

def on_enter(event):
    focus_next_label()

def focus_next_label():
    current_focus = root.focus_get()
    if current_focus == nameEntry:
        yearEntry.focus_set()
    elif current_focus == yearEntry:
        monthEntry.focus_set()
    elif current_focus == monthEntry:
        dayEntry.focus_set()
    elif current_focus == dayEntry:
        calculateAge()

#CALCULATIONS#
def calculateAge():
    today= date.today()
    birthday=date(int(yearEntry.get()),int(monthEntry.get()),int(dayEntry.get()))
    age=today.year-birthday.year-((today.month,today.day)<(birthday.month,birthday.day))
    Label(text=f"{nameValue.get()} Your Age is {age}",font=30).place(x=300,y=500)

#INPUTS#
Label(text="Name",font=23).place(x=200,y=250)
Label(text="Year",font=23).place(x=200,y=300)
Label(text="Month",font=23).place(x=200,y=350)
Label(text="Day",font=23).place(x=200,y=400)

nameValue=StringVar()
yearValue=StringVar()
monthValue=StringVar()
dayValue=StringVar()

#EntryFields#
nameEntry=Entry(root,textvariable=nameValue,width=30,bd=3,font=20)
nameEntry.place(x=300,y=250)
yearEntry=Entry(root,textvariable=yearValue,width=30,bd=3,font=20)
yearEntry.place(x=300,y=300)
monthEntry=Entry(root,textvariable=monthValue,width=30,bd=3,font=20)
monthEntry.place(x=300,y=350)
dayEntry=Entry(root,textvariable=dayValue,width=30,bd=3,font=20)
dayEntry.place(x=300,y=400)

nameEntry.bind('<Return>', on_enter)
yearEntry.bind('<Return>', on_enter)
monthEntry.bind('<Return>', on_enter)
dayEntry.bind('<Return>', on_enter)

Button(text="Calculate Age", font=20,bg="black",fg="white",width=11,height=2,command=calculateAge).place(x=300,y=450)
root.mainloop()
