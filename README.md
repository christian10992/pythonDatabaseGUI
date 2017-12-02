# pythonDatabaseGUI
A GUI interface for connecting with Microsft Access databases using TKinter and pyodbc

This was written as part of a project for a (non-progamming based) university project.

The premise of the project is that you are the owner of a video store. Part of the project is to create a Microsoft Access database containing details concerning your inventory and customers.

Since I am a benevolent business owner, and in my experience in retail, it is unreasonable to expect my employees to maintain a database.
Thus, I wanted to create an easy to use, visually driven program for employees to find, update, and enter data into the database.

# A few notes
## Tkinter
This program was written using Python 3.X.
If you are using 2.X, you will need to change the import from 'tkinter' to 'Tkinter.'
As far as I am aware, everything else should work between the versions, but I am not well versed in 2.X.

## Establishing a connection
The connection statement in my program is written in relation to my home computer's settings.
You may need to change them in order for the program to work on your computer.
See the pyodbc documentation for further info if you are having trouble.

## Pull requests
This is my first time using either Tkinter or pyodbc, so feel free to create a request if you see something wrong or would like to
share a better way of doing something. I have only been working with Python a short time and am always interested in learning more.
