# TicTuqToe
This is a repository containing all of the source files used in a version of Tic Tac Toe made with PyQt6 for an application to Tuq.

Dependencies:
- PyQt6 (Note that PyQt5 probably will not be able to run this, despite how similar they are.)
- SQLite3

Additional Notes:
- The executable file in dist does not work at this time. I do not at present have a machine with which I can test creating an executable for Windows, and as such I cannot find out if that will work better than the Mac version of the executable created by pyinstaller. 
- Similarly, if you want to create an executable version of the program, it worked well for me to use "pyinstaller --one-file gui.py" in the main directory.
- If you would prefer to not do that and if you have the dependencies installed, then gui.py is the file you should run.
