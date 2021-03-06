from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from DBConnectProject import DBConnect
from ListReservation import ListTickets
dbConnect=DBConnect()
root=Tk()
root.title("Data Management Project")
root.configure(background='#e1d8b2')

ttk.Label(root, text="Full Name").grid(row=0, column=0, padx=10, pady=10)
ttk.Label(root, text="Gender").grid(row=1, column=0)
ttk.Label(root, text="Comments").grid(row=2, column=0)
style=ttk.Style()
style.theme_use("classic")
style.configure("TLabel",background="#e1d8b2")
style.configure("TButton",background="#e1d8b2")
style.configure("TRadiobutton",background="#e1d8b2")
e1=ttk.Entry(root, width=30, font=('Arial', 10))
e1.grid(row=0,column=1, columnspan=2)
Gender=StringVar()
Gender.set('Male')
r1=ttk.Radiobutton(root, text='Male', variable=Gender, value='Male')
r2=ttk.Radiobutton(root, text='Female', variable=Gender, value='Female')
r1.grid(row=1, column=1)
r2.grid(row=1, column=2)
e2=Text(root, width=30, height=5,font=('Arial',10))
e2.grid(row=2,column=1,columnspan=2)
Bu=ttk.Button(root,text='Submit')
Bu.grid(row=3,column=3)
Bu2=ttk.Button(root,text='List Comments')
Bu2.grid(row=4,column=3)
Bu3=ttk.Button(root,text="Edit Comments")
Bu3.grid(row=5,column=3)
Bu4=ttk.Button(root,text='Delete record')
Bu4.grid(row=6,column=3)


def BClk():
    print("Name:{}".format(e1.get()))
    print("Gender:{}".format(Gender.get()))
    print("Comments:{}".format(e2.get('1.0','end')))
    msg=dbConnect.Add(e1.get(),Gender.get(),e2.get('1.0','end'))
    messagebox.showinfo(title='Add info',message=msg)
    e1.delete(0,'end')
    e2.delete(1.0,'end')


def BClkList():
    listTickets=ListTickets()


def BClk2():
    msg=dbConnect.Update(e1.get(), e2.get('1.0', 'end'))
    messagebox.showinfo(title='Update info', message=msg)
    e1.delete(0, 'end')
    e2.delete(1.0, 'end')


def BClk3():
    msg = dbConnect.Delete(e1.get())
    messagebox.showinfo(title='Delete info', message=msg)
    e1.delete(0, 'end')
    e2.delete(1.0, 'end')
Bu2.config(command=BClkList)
Bu.config(command=BClk)
Bu3.config(command=BClk2)
Bu4.config(command=BClk3)
root.mainloop()