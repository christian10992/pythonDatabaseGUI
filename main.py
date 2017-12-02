# This program is written in Python 3.
# Change tkinter to Tkinter for Python 2.
import tkinter as tk
import tkinter.messagebox

import pyodbc

import profilesPane
import inventoryPane

# These are the login and function selection panes for a program intended for a
# small business to use to manage their customer and inventory database. As a
# disclaimer, this was written for a class project and not intended for any
# practical application.


# Establish driver, file, and authentification information.
# This may need to be changed depending on your server and system settings.
cnxn=pyodbc.connect("""DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};
                    Dbq=C:videoStore.accdb;UID=admin;PWD=")
                    """)


# Define connection cursor
cursor=cnxn.cursor()

      
# Set encoding
cnxn.setdecoding(pyodbc.SQL_CHAR, encoding = "utf-8")
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding = "utf-8")
cnxn.setencoding(encoding = "utf-8")

# Window dimension constants
W = 200
H = 225

# This class is the login pane
class login():
    def __init__(self):
        # Set main window title, dimensions, and position
        self.mainWindow=tk.Tk()
        self.mainWindow.title("Login")
        self.mainWindow.resizable(width=False, height=False)
        self.mainWindow.geometry('{}x{}'.format(W, H))
        # Get screen dimensions
        ws = self.mainWindow.winfo_screenwidth()
        hs = self.mainWindow.winfo_screenheight()
        # Calculate coordinates on screen
        x = (ws/2) - (W/2)
        y = (hs/2) - (H)
        # Place window in starting position
        self.mainWindow.geometry('%dx%d+%d+%d' % (W, H, x, y))
        

        # Set form objects
        self.labelUser=tk.Label(text = "Username")
        self.labelUser.grid(row = 0, column = 1,
                            padx = (40, 0), pady = (15, 5))
        self.userEntry=tk.Entry(width = 20)

        
        self.userEntry.grid(row = 1, column = 1,
                            padx = (40, 0), pady = (0, 15))
        self.labelPass=tk.Label(text = "Password")

        
        self.labelPass.grid(row = 2, column = 1,
                            padx = (40, 0), pady = (0, 5))
        self.passEntry=tk.Entry(width = 20,
                                show = "*")

        
        self.passEntry.grid(row = 3, column = 1,
                            padx = (40, 0), pady = (0,30))
        self.submitButton=tk.Button(text = "Submit",
                                    command=self.validate)

        
        self.submitButton.grid(row = 4, column = 1,
                               padx = (40, 0), pady = (0, 7.5))
        self.quitButton=tk.Button(text = "Quit",
                                  command=self.mainWindow.destroy)

        
        self.quitButton.grid(row = 5, column = 1,
                             padx = (40, 0))
        
        
        # tkinter main loop
        tk.mainloop()


    # Function definition for submit button click
    def validate(self):
        user = str(self.userEntry.get())
        password = str(self.passEntry.get())


        # Find username in database
        cursor.execute("""
            SELECT Username from users
            WHERE Username = ?
            """, user)
        result=cursor.fetchone()
        # If the username is not found, it will return an error,
        # otherwise it will validate the password.
        # The validation is performed in two stages so that the user
        # can see if it is the username or password that is incorrect.
        if result is None:
            tkinter.messagebox.showinfo("Error",
                "Username not found. Please check your credentials and try again.")
        else:
            cursor.execute("""
                SELECT Username, Password from users
                WHERE Username = ?
                AND Password = ?
                """, user, password)
            result = cursor.fetchone()
            if result is None:
                tkinter.messagebox.showinfo("Error",
                    "Password incorrect. Please check your credentials and try again.")
            else:
                # Before window closes, it will log
                # coordinates for next window to use
                global X
                X = self.mainWindow.winfo_x()
                global Y
                Y = self.mainWindow.winfo_y()
                self.mainWindow.destroy()
                selector()


# This class is the pane to select between the
# two different parts of the program,
# editing the customer or inventory databases
class selector():
    def __init__(self):
        self.mainWindow=tk.Tk()
        self.mainWindow.title("Launch")
        self.mainWindow.resizable(width=False, height=False)
        self.mainWindow.geometry('{}x{}'.format(W, H))
        try:
            self.mainWindow.geometry('%dx%d+%d+%d' % (W, H, X, Y))
        except:
            ws = self.mainWindow.winfo_screenwidth()
            hs = self.mainWindow.winfo_screenheight()
            x = (ws/2) - (W/2)
            y = (hs/2) - (H)
            self.mainWindow.geometry('%dx%d+%d+%d' % (W, H, x, y))
            

        self.buttonProfiles=tk.Button(text = "Customer Info",
                                      command=self.viewCust)
        self.buttonProfiles.grid(row = 0, column = 1,
                                 padx = (60, 0), pady = (40, 30))

        
        self.buttonInventory=tk.Button(text = "Inventory",
                                       command=self.viewInventory)
        self.buttonInventory.grid(row = 1, column = 1,
                                  padx = (60, 0), pady = (0, 30))

        
        self.quitButton=tk.Button(text = "Quit",
                                  command=self.mainWindow.destroy)
        self.quitButton.grid(row = 3, column = 1,
                             padx = (60, 0))


        tk.mainloop()


    def viewCust(self):
        self.mainWindow.destroy()
        profilesPane.profiles()


    def viewInventory(self):
        self.mainWindow.destroy()
        inventoryPane.inventory()


if __name__ == "__main__":
    login=login()
