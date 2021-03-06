from tkinter import *
from tkinter import ttk
from DBConnectProject import DBConnect
class ListTickets:
    def __init__(self):
        self._dbConnect=DBConnect()
        self._root=Tk()
        tv=ttk.Treeview(self._root)
        tv.pack()
        tv.heading('#0',text="ID")
        tv.configure(column=('Name','Gender','Comments'))
        tv.heading('Name', text="Full Name")
        tv.heading('Gender', text="Gender")
        tv.heading('Comments', text="Comments")
        cursor=self._dbConnect.ListTickets()
        for row in cursor:
            tv.insert('','end','#{}'.format(row["ID"]),text=row["ID"])
            tv.set('#{}'.format(row["ID"]),'#1',row["Name"])
            tv.set('#{}'.format(row["ID"]),'#2',row["Gender"])
            tv.set('#{}'.format(row["ID"]),'#3',row["Comments"])
        self._root.mainloop()

