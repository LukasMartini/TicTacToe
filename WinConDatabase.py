import sqlite3 as sql
from sqlite3 import Error

class WinConDBControl():
    def __init__(self, dbfile):
        self.conn = "God knows I'm trying, and God knows as well as I do that it's not enough."
        try:
            self.conn = sql.connect("/Users/almostfishy/PycharmProjects/TicTuqToe/dbfiles/WinCon.db")
        except Error:
            print("Database Connection Error: File may be missing.")

    def initLookUpTable(self, conn):
        try:
            curs = conn.cursor() # NOTE: primary key really isn't necessary here because it's one column so it's omitted.

            # Create lookup tables
            curs.execute("CREATE TABLE IF NOT EXISTS columnZero (sec_id integer, currStatus integer);")
            curs.execute("CREATE TABLE IF NOT EXISTS columnOne (sec_id integer, currStatus integer);")
            curs.execute("CREATE TABLE IF NOT EXISTS columnTwo (sec_id integer, currStatus integer);")

            # Reset tables. Would use update, but because I'm manually adding data I don't believe that's any better.
            curs.execute("DELETE FROM columnZero")
            curs.execute("DELETE FROM columnOne")
            curs.execute("DELETE FROM columnTwo")

            # Create insert commands
            addC0 = "INSERT INTO columnZero(sec_id, currStatus) VALUES(?,?)"
            addC1 = "INSERT INTO columnOne(sec_id, currStatus) VALUES(?,?)"
            addC2 = "INSERT INTO columnTwo(sec_id, currStatus) VALUES(?,?)"

            # Insert values
            curs.execute(addC0, (0, 0))
            curs.execute(addC0, (10, 0))
            curs.execute(addC0, (20, 0))

            curs.execute(addC1, (1, 0))
            curs.execute(addC1, (11, 0))
            curs.execute(addC1, (21, 0))

            curs.execute(addC2, (2, 0))
            curs.execute(addC2, (12, 0))
            curs.execute(addC2, (22, 0))

        except Error as e:
            print(e)

    def updateValue(self, sec_id):
        pass


    def closeConnection(self):
        self.conn.close()