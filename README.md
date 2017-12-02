# pythonDatabaseGUI
A GUI interface for connecting with Microsft Access databases using TKinter and pyodbc

This was written as part of a project for a (non-progamming based) university project.

The premise of the project is that you are the owner of a video store. Part of the project is to create a Microsoft Access database containing details concerning your inventory and customers.

Wile not required by any means for the project, my rather lackluster opinion on Access sparked the intial idea to write this program.

As well, based on my experience in retail, it is unreasonable to expect lower-level employees to maintain a database.
Thus, I wanted to create an easy to use, visually driven program for employees to find, update, and enter data into the database.

I think it is also worthwhile mentioning that this is purely academic and entirely hypothetical. This program lacks the features necessary
to protect sensitive user-data and I make no intention or recommendation that this be used in a real-world, practical application.

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
