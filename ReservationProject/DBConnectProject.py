import sqlite3
class DBConnect:
    def __init__(self):
        self._db = sqlite3.connect("Reservation.db")
        self._db.row_factory = sqlite3.Row
        self._db.execute("create table if not exists ticket(ID integer primary key autoincrement,name text,gender int,comments text)")
        self._db.commit()

    def Add(self,Name,Gender,Comments):
        self._db.row_factory = sqlite3.Row
        self._db.execute("insert into ticket(name,gender,comments) values(?,?,?)",(Name,Gender,Comments))
        self._db.commit()
        return("record is added")

    def ListTickets(self):
        cursor=self._db.execute("Select * from ticket")
        return cursor

    def Delete(self,name):
        self._db.row_factory = sqlite3.Row
        self._db.execute("Delete from ticket where name=?",(name,))
        self._db.commit()
        return("record is deleted")

    def Update(self,Name,Comments):
        self._db.row_factory = sqlite3.Row
        self._db.execute("Update ticket set comments=? where name=?",(Comments,Name))
        self._db.commit()
        return("record is updated")
