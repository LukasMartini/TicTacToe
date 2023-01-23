import sqlite3 as sql
from sqlite3 import Error
from PyQt6.QtCore import QCoreApplication
import assets

class WinConDBControl():
    def __init__(self, dbfile):
        self.conn = "God knows I'm trying, and God knows as well as I do that it's not enough."
        try:
            filepath = QCoreApplication.applicationDirPath()
            self.conn = sql.connect(filepath + "WinCon.db")
        except Error as e:
            print("Database Connection Error: File may be missing.")
            print(e)

    def initAdjacencyTable(self):
        try:
            curs = self.conn.cursor()

            create = """CREATE TABLE IF NOT EXISTS adjacency (
                        sec_id integer, 
                        horizAdj1id integer, 
                        horizAdj2id integer, 
                        vertAdj1id integer,
                        vertAdj2id integer)"""
            curs.execute(create)

            curs.execute("DELETE FROM adjacency") # Again, this is to clear the table to prevent appending

            insert = "INSERT INTO adjacency(sec_id, horizAdj1id, horizAdj2id, vertAdj1id, vertAdj2id) VALUES(?,?,?,?,?)"

            # I know there's totally a more efficient way to do this, but my sec_id system is trash and I don't have a lot of time.
            curs.execute(insert, (0, 1, 2, 10, 20))
            curs.execute(insert, (1, 0, 2, 11, 12))
            curs.execute(insert, (2, 0, 1, 21, 22))
            curs.execute(insert, (10, 11, 12, 0, 20))
            curs.execute(insert, (11, 10, 12, 1, 21))
            curs.execute(insert, (12, 10, 11, 2, 22))
            curs.execute(insert, (20, 21, 22, 0, 10))
            curs.execute(insert, (21, 20, 22, 1, 11))
            curs.execute(insert, (22, 20, 21, 2, 12))

            self.conn.commit()

        except Error as e:
            print(e)

    def initLookUpTable(self):
        try:
            curs = self.conn.cursor() # NOTE: primary key really isn't necessary here because it's one column so it's omitted.

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

            self.conn.commit()

        except Error as e:
            print(e)

    def updateValue(self, sec_id, currTurn):
        try:
            curs = self.conn.cursor()

            # Attempt to update all tables because I'm tired and don't want to do it with if/else
            curs.execute("UPDATE columnZero SET currStatus = ? WHERE sec_id = ?", (currTurn, sec_id))
            curs.execute("UPDATE columnOne SET currStatus = ? WHERE sec_id = ?", (currTurn, sec_id))
            curs.execute("UPDATE columnTwo SET currStatus = ? WHERE sec_id = ?", (currTurn, sec_id))

            self.conn.commit()
        except Error as e:
            print(e)

    def checkWin(self, player, sec_id):
        try:
            curs = self.conn.cursor()
            checkData = []
            fullData = []
            fullData.append(curs.execute("SELECT currStatus FROM columnZero").fetchall())
            fullData.append(curs.execute("SELECT currStatus FROM columnOne").fetchall())
            fullData.append(curs.execute("SELECT currStatus FROM columnTwo").fetchall())
            allFull = 1
            for each in fullData:
                for peach in each:
                    if peach[0] == 0:
                        allFull = 0


            if sec_id == 0:
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (1,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (2,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (10,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (20,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (22,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player) or (checkData[4] == player and checkData[5] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 1:
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (0,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (2,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (21,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 2:
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (0,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (1,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (12,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (22,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (20,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player) or (checkData[4] == player and checkData[5] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 10:
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (12,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (0,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (20,)).fetchall()[0][0])
                if (checkData[0] == 1 and checkData[1] == 1) or (checkData[2] == 1 and checkData[3] == 1):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 11:
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (10,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (12,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (1,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (21,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (0,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (22,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (20,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (2,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player) or (checkData[4] == player and checkData[5] == player) or (checkData[6] == player and checkData[7] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 12:
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (10,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (2,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (22,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 20:
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (21,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (22,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (10,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (0,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (2,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player) or (checkData[4] == player and checkData[5] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 21:
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (20,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (22,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (1,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1
            elif sec_id == 22:
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (20,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (21,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (2,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (12,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (0,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player) or (checkData[4] == player and checkData[5] == player):
                    return player
                elif allFull == 1:
                    return -2
                else:
                    return -1

        except Error as e:
            print(e)


    def closeConnection(self):
        self.conn.close()