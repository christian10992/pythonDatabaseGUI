import pyodbc


cnxn=pyodbc.connect("""DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};
                    Dbq=C:videoStore.accdb;UID=admin;PWD=""")


cursor=cnxn.cursor()


cnxn.setdecoding(pyodbc.SQL_CHAR, encoding = "utf-8")
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding = "utf-8")
cnxn.setencoding(encoding = "utf-8")


def findPhone(first, last):
    cursor.execute("""
        SELECT Phone from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue is None:
        resultValue = ""
    return resultValue


def findAddress(first, last):
    cursor.execute("""
        SELECT Address from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue is None:
        resultValue = ""
    return resultValue


def findApt(first, last):
    cursor.execute("""
        SELECT Apt from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue is None:
        resultValue = ""
    return resultValue


def findZipCode(first, last):
    cursor.execute("""
        SELECT ZIP from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue is None:
        resultValue = ""
    return resultValue


def findState(first, last):
    cursor.execute("""
        SELECT State from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue is None:
        resultValue = "--"
    return resultValue


def findEMail(first, last):
    cursor.execute("""
        SELECT [E-Mail] from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue is None:
        resultValue = ""
    return resultValue


def findRewards(first, last):
    cursor.execute("""
        SELECT Rewards from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue == "Y":
        resultValue = 1
    else:
        resultValue = 0
    return resultValue


def findMailStatus(first, last):
    cursor.execute("""
        SELECT MList from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue == "Y":
        resultValue = 1
    else:
        resultValue = 0
    return resultValue


def findEMailStatus(first, last):
    cursor.execute("""
        SELECT EList from Profiles
        WHERE FirstName = ?
        AND LastName = ?
        """, first, last)
    result = cursor.fetchone()
    resultValue = result[0]
    if resultValue == "Y":
        resultValue = 1
    else:
        resultValue = 0
    return resultValue


def newName(first, last):
    cursor.execute("""
    INSERT INTO Profiles(FirstName, LastName)
    VALUES (? , ?)
    """, first, last)


def updatePhone(phone, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET Phone = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, phone, first, last)
    cnxn.commit()


def updateAddress(address, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET Address = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, address, first, last)
    cnxn.commit()


def updateApt(apt, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET Apt = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, apt, first, last)
    cnxn.commit()


def updateZip(zipCode, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET ZIP = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, zipCode, first, last)
    cnxn.commit()


def updateState(state, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET State = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, state, first, last)
    cnxn.commit()


def updateEMail(eMail, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET [E-Mail] = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, eMail, first, last)
    cnxn.commit()


def updateRewards(rMemb, first, last):
    cursor.execute("""
        SELECT Rewards, FirstName, LastName from Profiles
        WHERE Rewards = ?
        AND FirstName = ?
        AND LastName = ?
        """, rMemb, first, last)
    result = cursor.fetchone()
    if result is None:
        changeRewards(rMemb, first, last)


def changeRewards(rMemb, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET Rewards = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, rMemb, first, last)
    cnxn.commit()


def updateMailList(mList, first, last):
    cursor.execute("""
        SELECT MList, FirstName, LastName from Profiles
        WHERE MList = ?
        AND FirstName = ?
        AND LastName = ?
        """, mList, first, last)
    result = cursor.fetchone()
    if result is None:
        changeMList(mList, first, last)


def changeMList(mList, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET MList = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, mList, first, last)
    cnxn.commit()


def updateEMailList(eList, first, last):
    cursor.execute("""
        SELECT EList, FirstName, LastName from Profiles
        WHERE EList = ?
        AND FirstName = ?
        AND LastName = ?
        """, eList, first, last)
    result = cursor.fetchone()
    if result is None:
        changeEList(eList, first, last)


def changeEList(eList, first, last):
    cursor.execute("""
        UPDATE Profiles
        SET EList = ?
        WHERE FirstName = ?
        AND LastName = ?
        """, eList, first, last)
    cnxn.commit()
