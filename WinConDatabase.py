import sqlite3 as sql
from sqlite3 import Error
from PyQt6.QtCore import QCoreApplication
import assets

class WinConDBControl():
    def __init__(self, dbfile):
        # Set up connection to the database.
        self.conn = "God knows I'm trying, and God knows as well as I do that it's not enough."
        try:
            filepath = QCoreApplication.applicationDirPath()
            self.conn = sql.connect(filepath + "WinCon.db")
        except Error as e:
            print("Database Connection Error: File may be missing.")
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
            # Grabs all data from the tables
            fullData = []
            fullData.append(curs.execute("SELECT currStatus FROM columnZero").fetchall())
            fullData.append(curs.execute("SELECT currStatus FROM columnOne").fetchall())
            fullData.append(curs.execute("SELECT currStatus FROM columnTwo").fetchall())
            # Checks if any of the sections haven't been clicked yet. This is used to check for a tie
            allFull = 1
            for each in fullData:
                for peach in each:
                    if peach[0] == 0:
                        allFull = 0


            # Brute force check to see if there is a win
            if sec_id == 0:
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (1,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (2,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (10,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnZero WHERE sec_id = ?", (20,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnOne WHERE sec_id = ?", (11,)).fetchall()[0][0])
                checkData.append(curs.execute("SELECT currStatus FROM columnTwo WHERE sec_id = ?", (22,)).fetchall()[0][0])
                if (checkData[0] == player and checkData[1] == player) or (checkData[2] == player and checkData[3] == player) or (checkData[4] == player and checkData[5] == player):
                    return player # If any of the win methods are met, return the current player number
                elif allFull == 1:
                    return -2 # If all of the sections have been used, return the marker of a tie
                else:
                    return -1 # Otherwise return the marker to continue play.
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
