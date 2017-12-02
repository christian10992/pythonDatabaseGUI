import tkinter
import collections

import pyodbc


cnxn=pyodbc.connect("""DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};
                    Dbq=C:videoStore.accdb;UID=admin;PWD=""")


cursor=cnxn.cursor()


cnxn.setdecoding(pyodbc.SQL_CHAR, encoding = "utf-8")
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding = "utf-8")
cnxn.setencoding(encoding = "utf-8")


def findProductBySKU(skuFind):
    cursor.execute("""
        SELECT Title from Stock
        WHERE SKU = ?
        """, skuFind)
    result = cursor.fetchone()
    if result is None:
        result = (" ")
    return result


def populateScreenFromSKU(skuFind):
    cursor.execute("""
        SELECT Category from Stock
        WHERE SKU = ?
        """, skuFind)
    result = cursor.fetchone()
    resultCategory = result[0]
    cursor.execute("""
        SELECT MSRP from Stock
        WHERE SKU = ?
        """, skuFind)
    result = cursor.fetchone()
    resultMSRP = result[0]
    cursor.execute("""
        SELECT QOH from Stock
        WHERE SKU = ?
        """, skuFind)
    result = cursor.fetchone()
    resultQOH = result[0]
    if resultQOH <= 3:
        tkinter.messagebox.showinfo("Alert",
            "Inventory low. Please add to next order")
    r = collections.namedtuple('results', ['Category', 'MSRP', 'QOH'])
    results = r(resultCategory, resultMSRP, resultQOH)
    return results


def findProductByName(productFind):
    cursor.execute("""
        SELECT Title from Stock
        WHERE Title = ?
        """, productFind)
    result=cursor.fetchone()
    if result is None:
        result = (" ")
    return result


def populateScreenFromTitle(productFind):
    cursor.execute("""
        SELECT Category from Stock
        WHERE Title = ?
        """, productFind)
    result = cursor.fetchone()
    resultCategory = result[0]
    cursor.execute("""
        SELECT SKU from Stock
        WHERE Title = ?
        """, productFind)
    result = cursor.fetchone()
    resultSKU = result[0]
    cursor.execute("""
        SELECT MSRP from Stock
        WHERE Title = ?
        """, productFind)
    result = cursor.fetchone()
    resultMSRP = result[0]
    cursor.execute("""
        SELECT QOH from Stock
        WHERE Title = ?
        """, productFind)
    result = cursor.fetchone()
    resultQOH = result[0]
    if resultQOH <= 3:
        tkinter.messagebox.showinfo("Alert",
            "Inventory low. Please add to next order")
    r = collections.namedtuple("results", ["Category", "SKU", "MSRP", "QOH"])
    results = r(resultCategory, resultSKU, resultMSRP, resultQOH)
    return results


def newTitle(title):
    cursor.execute("""
        insert into Stock (Title) VALUES (?)
        """, title)


def updateCategory(category, title):
    cursor.execute("""
        UPDATE Stock
        SET Category = ?
        WHERE Title = ?
        """, category, title)
    cnxn.commit()


def updateSKU(sku, title):
    cursor.execute("""
        UPDATE Stock
        SET SKU = ?
        WHERE Title = ?
        """, sku, title)
    cnxn.commit()


def updateMSRP(msrp, title):
    cursor.execute("""
        UPDATE Stock
        SET MSRP = ?
        WHERE Title = ?
        """, msrp, title)
    cnxn.commit()


def updateQOH(qoh, title):
    cursor.execute("""
        UPDATE Stock
        SET QOH = ?
        WHERE Title = ?
        """, qoh, title)
    cnxn.commit()
