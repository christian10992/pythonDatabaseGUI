import tkinter as tk
import tkinter.messagebox
from tkinter import ttk

import pyodbc

import main
import profileModule


cnxn = pyodbc.connect("""DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};
                      Dbq=C:videoStore.accdb;UID=admin;PWD=""")


cursor = cnxn.cursor()


cnxn.setdecoding(pyodbc.SQL_CHAR, encoding = "utf-8")
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding = "utf-8")
cnxn.setencoding(encoding = "utf-8")


STATES = ("--", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL",
          "GA", "GU", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME",
          "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ",
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "PR", "RI", "SC",
          "SD", "TN", "TX", "UT", "VT", "VA", "VI", "WA", "WV", "WI", "WY")
W = 525
H = 350


class profiles:
    def __init__(self):
        self.mainWindow=tk.Tk()
        self.mainWindow.title("Customer Profiles")
        self.mainWindow.resizable(width=False, height=False)
        self.mainWindow.geometry('{}x{}'.format(W, H))
        ws = self.mainWindow.winfo_screenwidth()
        hs = self.mainWindow.winfo_screenheight()
        x = (ws/2) - (W/2)
        y = (hs/2) - (H/1.5)
        self.mainWindow.geometry('%dx%d+%d+%d' % (W, H, x, y))


        # Create StringVar objects for setting textvariables
        self.first = tk.StringVar()
        self.last = tk.StringVar()
        self.phone = tk.StringVar()
        self.address = tk.StringVar()
        self.apt = tk.StringVar()
        self.zipCode = tk.StringVar()
        self.state = tk.StringVar()
        self.eMail = tk.StringVar()


        # Create IntVar objects for setting checkbuttons
        self.rMemb = tk.IntVar()
        self.mList = tk.IntVar()
        self.eList = tk.IntVar()
        self.rMemb.set(0)
        self.mList.set(0)
        self.eList.set(0)


        self.labelFirst=tk.Label(text = "First Name")
        self.labelFirst.grid(row = 1, column = 1, columnspan = 6,
                             sticky = "W",
                             padx = (30,15), pady = (27, 0))
        self.firstEntry=tk.Entry(textvariable = self.first,
                                 width = 25)
        self.firstEntry.grid(row = 1, column = 6, columnspan = 14,
                             padx = (0, 30), pady = (30, 0))
        self.labelLast=tk.Label(text = "Last Name")
        self.labelLast.grid(row = 1, column = 15, columnspan = 10,
                            pady = (27, 0))
        self.lastEntry=tk.Entry(textvariable = self.last,
                                width = 25)
        self.lastEntry.grid(row = 1, column = 26, columnspan = 15,
                            pady = (30, 0))

        
        self.cbRMemb=tk.Checkbutton(text = "Rewards Member",
                                    variable = self.rMemb)
        self.cbRMemb.grid(row = 2, column = 3, columnspan = 7,
                          pady = (5, 0))

                
        self.labelPhone=tk.Label(text = "Phone Number")
        self.labelPhone.grid(row = 3, column = 1, columnspan = 8,
                             sticky = "W",
                             padx = (30, 10), pady = (10, 0))
        self.phoneEntry=tk.Entry(textvariable = self.phone,
                                 width = 20)
        self.phoneEntry.grid(row = 3, column = 7, columnspan = 15,
                             pady = (12, 0))


        self.labelAddress=tk.Label(text = "Address")
        self.labelAddress.grid(row = 4, column = 1, columnspan = 8,
                               sticky = "W",
                               padx = (30, 0), pady = (13, 0))
        self.addressEntry=tk.Entry(textvariable = self.address,
                                   width = 40)
        self.addressEntry.grid(row = 4, column = 7, columnspan = 20,
                               padx = (0, 15), pady = (15, 0))
        self.labelApt=tk.Label(text = "Apt #")
        self.labelApt.grid(row = 4, column = 30, columnspan = 5,
                           padx = (0, 10), pady = (13, 0))
        self.aptEntry=tk.Entry(textvariable = self.apt,
                               width = 12)
        self.aptEntry.grid(row = 4, column = 36, columnspan = 5,
                           pady = (15, 0))


        self.labelZip=tk.Label(text = "ZIP Code")
        self.labelZip.grid(row = 5, column = 1, columnspan = 5,
                           sticky = "W",
                           padx = (30, 0), pady = (13, 0))
        self.zipEntry=tk.Entry(textvariable = self.zipCode,
                               width = 12)
        self.zipEntry.grid(row = 5, column = 7, columnspan = 2,
                           pady = (15, 0))
        self.labelState=tk.Label(text = "State")
        self.labelState.grid(row = 5, column = 9, columnspan = 9,
                             padx = (10, 0), pady = (13, 0))
        self.stateEntry=ttk.Combobox(values = STATES,
                                     textvariable = self.state,
                                     state = "readonly",
                                     width = 8)
        self.stateEntry.grid(row = 5, column = 16, columnspan = 6,
                             pady = (15, 0))
        self.cbMList=tk.Checkbutton(text = "Mailing List",
                                    variable=self.mList)
        self.cbMList.grid(row = 5, column = 26, columnspan = 15,
                          pady = (13, 0))


        self.labelEMail=tk.Label(text = "E-Mail")
        self.labelEMail.grid(row = 6, column = 1, columnspan = 5,
                             sticky = "W",
                             padx = (30, 0), pady = (13, 0))
        self.eMailEntry=tk.Entry(textvariable = self.eMail,
                                 width = 25)
        self.eMailEntry.grid(row = 6, column = 7, columnspan = 5,
                             pady = (15, 0))
        self.cbEList=tk.Checkbutton(text = "E-Mail List",
                                    variable=self.eList)
        self.cbEList.grid(row = 6, column = 18, columnspan = 10,
                          pady = (15, 0))
        

        self.buttonFind=tk.Button(text = "Find Profile",
                                  command=self.findProfile)
        self.buttonFind.grid(row = 7, column = 4, columnspan = 10,
                             pady = (30, 0))
        self.buttonUpdate=tk.Button(text = "Update Profile",
                                    command=self.updateProfile)
        self.buttonUpdate.grid(row = 7, column = 10, columnspan = 11,
                               padx = (0, 5), pady = (30, 0))
        self.buttonNew=tk.Button(text = "Create New Profile",
                                 command=self.newProfile)
        self.buttonNew.grid(row = 7, column = 23, columnspan = 14,
                            pady = (30,0))



        self.buttonBack=tk.Button(text = "Back",
                                  command=self.goBack)
        self.buttonBack.grid(row = 8, column = 7, columnspan = 10,
                             pady = (20, 0))
        self.buttonClear=tk.Button(text = "Clear Form",
                                   command=self.clearForm)
        self.buttonClear.grid(row = 8, column = 10, columnspan = 10,
                              pady = (20, 0))
        self.quitButton=tk.Button(text = "Quit",
                                  command=self.mainWindow.destroy)
        self.quitButton.grid(row = 8, column = 19, columnspan = 10,
                             pady = (20, 0))
        



        tk.mainloop()

    def findProfile(self):
        first = str(self.firstEntry.get())
        last = str(self.lastEntry.get())


        if first == "" or last == "":
            tkinter.messagebox.showinfo("Error",
                "You must enter a first and last name to search for a profile.")
        else:
            cursor.execute("""
                SELECT Firstname, LastName from Profiles
                WHERE FirstName = ?
                AND LastName = ?
                """, first, last)
            result = cursor.fetchone()
            if result is None:
                tkinter.messagebox.showinfo("Error",
                    "Username not found. Please check name and try again or create a new profile.")

            else:
                phoneOnFile=profileModule.findPhone(first, last)
                self.phone.set(phoneOnFile)
                addressOnFile=profileModule.findAddress(first, last)
                self.address.set(addressOnFile)
                aptOnFile=profileModule.findApt(first, last)
                self.apt.set(aptOnFile)
                zipCodeOnFile=profileModule.findZipCode(first, last)
                self.zipCode.set(zipCodeOnFile)
                stateOnFile=profileModule.findState(first, last)
                self.state.set(stateOnFile)
                eMailOnFile=profileModule.findEMail(first, last)
                self.eMail.set(eMailOnFile)
                rewardsStatus=profileModule.findRewards(first, last)
                self.rMemb.set(rewardsStatus)
                mailStatus=profileModule.findMailStatus(first, last)
                self.mList.set(mailStatus)
                eListStatus=profileModule.findEMailStatus(first, last)
                self.eList.set(eListStatus)


    def updateProfile(self):
        first = str(self.firstEntry.get())
        last = str(self.lastEntry.get())
        phone = str(self.phoneEntry.get())
        address = str(self.addressEntry.get())
        apt = str(self.aptEntry.get())
        zipCode = str(self.zipEntry.get())
        state = str(self.stateEntry.get())
        eMail = str(self.eMailEntry.get())
        if self.mList.get() == 0:
            mList = "N"
        else:
            mList = "Y"
        if self.eList.get() == 0:
            eList = "N"
        else:
            eList = "Y"
        if self.rMemb.get() == 0:
            rMemb = "N"
        else:
            rMemb = "Y"


        if first == "" or last == "":
            tkinter.messagebox.showinfo("Error",
                "You must enter a first and last name to search for a profile.")
        else:
            cursor.execute("""
                SELECT Firstname, LastName from Profiles
                WHERE FirstName = ?
                AND LastName = ?
                """, first, last)
            result = cursor.fetchone()
            if result is None:
                tkinter.messagebox.showinfo("Error",
                    "Username not found. Please check name and try again or create a new profile.")
            else:
                if phone != '':
                    profileModule.updatePhone(phone, first, last)
                if address != '':
                    profileModule.updateAddress(address, first, last)
                if apt != '':
                    profileModule.updateApt(apt, first, last)
                if zipCode != '':
                   profileModule.updateZip(zipCode, first, last)
                if state != '':
                    profileModule.updateState(state, first, last)
                if eMail != '':
                    profileModule.updateEMail(eMail, first, last)
                profileModule.updateRewards(rMemb, first, last)
                profileModule.updateMailList(mList, first, last)
                profileModule.updateEMailList(eList, first, last)


                tkinter.messagebox.showinfo("Message",
                    "Profile updated successfully.")


    def newProfile(self):
        first = str(self. firstEntry.get())
        last = str(self.lastEntry.get())
        phone = str(self.phoneEntry.get())
        address = str(self.addressEntry.get())
        apt = str(self.aptEntry.get())
        zipCode = str(self.zipEntry.get())
        state = str(self.stateEntry.get())
        eMail = str(self.eMailEntry.get())
        if self.mList.get() == 0:
            mList = "N"
        else:
            mList = "Y"
        if self.eList.get() == 0:
            eList = "N"
        else:
            eList = "Y"
        if self.rMemb.get() == 0:
            rMemb = "N"
        else:
            rMemb = "Y"


        if first == "" or last == "":
            tkinter.messagebox.showinfo("Error",
                "You must enter a first and last name to create a new user profile.")
        else:
            profileModule.newName(first, last)
            if phone != "":
                profileModule.updatePhone(phone, first, last)
            if address != "":
                profileModule.updateAddress(address, first, last)
            if apt != "":
                profileModule.updateApt(apt, first, last)
            if zipCode != "":
                profileModule.updateZip(zipCode, first, last)
            if state != "":
                profileModule.updateState(state, first, last)
            if eMail != "":
                profileModule.updateEMail(eMail, first, last)
            profileModule.updateRewards(rMemb, first, last)
            profileModule.updateMailList(mList, first, last)
            profileModule.updateEMailList(eList, first, last)


            tkinter.messagebox.showinfo("Message",
                "New profile created successfully.")


    def goBack(self):
        self.mainWindow.destroy()
        main.selector()


    def clearForm(self):
        clearValue = ""
        self.first.set(clearValue)
        self.last.set(clearValue)
        self.phone.set(clearValue)
        self.address.set(clearValue)
        self.apt.set(clearValue)
        self.zipCode.set(clearValue)
        self.state.set(clearValue)
        self.eMail.set(clearValue)


        buttonClear = 0
        self.rMemb.set(buttonClear)
        self.mList.set(buttonClear)
        self.eList.set(buttonClear)


if __name__ == "__main__":
    profiles = profiles()
