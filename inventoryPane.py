import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import collections

import pyodbc

import main
import inventoryModule


cnxn=pyodbc.connect("""DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};
                    Dbq=C:videoStore.accdb;UID=admin;PWD=""")


cursor=cnxn.cursor()


cnxn.setdecoding(pyodbc.SQL_CHAR, encoding = "utf-8")
cnxn.setdecoding(pyodbc.SQL_WCHAR, encoding = "utf-8")
cnxn.setencoding(encoding = "utf-8")


W = 375
H = 375


class inventory:
    def __init__(self):
        self.mainWindow=tk.Tk()
        self.mainWindow.title("Inventory")
        self.mainWindow.resizable(width=False, height=False)
        self.mainWindow.geometry('{}x{}'.format(W, H))
        ws = self.mainWindow.winfo_screenwidth()
        hs = self.mainWindow.winfo_screenheight()
        x = (ws/2) - (W/2)
        y = (hs/2) - (H/1.5)
        self.mainWindow.geometry('%dx%d+%d+%d' % (W, H, x, y))


        self.title = tk.StringVar()
        self.category = tk.StringVar()
        self.sku = tk.StringVar()
        self.msrp = tk.StringVar()
        self.qoh = tk.StringVar()
        self.skuFind = tk.StringVar()
        self.productFind = tk.StringVar()


        self.labelTitle=tk.Label(text = "Title")
        self.labelTitle.grid(row = 1, column = 2, columnspan = 2,
                             sticky = "W" + "E", 
                             padx = (0, 30), pady = (30, 0))
        self.labelCategory=tk.Label(text = "Category")
        self.labelCategory.grid(row = 1, column = 5,
                                sticky = "W",
                                padx = (0, 50), pady = (30, 0))
        
        self.titleEntry=tk.Entry(textvariable = self.title,
                                 width = 25)
        self.titleEntry.grid(row = 2, column = 1, columnspan = 4,
                             sticky = "W",
                             padx = (30, 20))
        self.categoryEntry=tk.Entry(textvariable = self.category,
                                    width = 15)
        self.categoryEntry.grid(row = 2, column = 4, columnspan = 2,
                                sticky = "E",
                                padx = (0, 30))

        
        self.labelSKU=tk.Label(text = "SKU")
        self.labelSKU.grid(row = 3, column = 1,
                           padx = (15, 0), pady = (15, 0))
        self.labelMSRP=tk.Label(text = "MSRP")
        self.labelMSRP.grid(row = 3, column = 4,
                            pady = (15, 0))
        self.labelQOH=tk.Label(text = "QOH")
        self.labelQOH.grid(row = 3, column = 5,
                           sticky = "W",
                           padx = (20, 0), pady = (15, 0))

        
        self.skuEntry=tk.Entry(textvariable = self.sku,
                               width = 10)
        self.skuEntry.grid(row = 4, column = 1,
                           sticky = "W",
                           padx = (30, 0))
        self.msrpEntry=tk.Entry(textvariable = self.msrp,
                                width = 10)
        self.msrpEntry.grid(row = 4, column = 4,
                            sticky = "W")
        self.qohEntry=tk.Entry(textvariable = self.qoh,
                               width = 10)
        self.qohEntry.grid(row = 4, column = 5,
                           sticky = "W",
                           padx = (10, 0))

        
        self.skuFindEntry=tk.Entry(textvariable = self.skuFind,
                                   width = 15)
        self.skuFindEntry.grid(row = 5, column = 3, columnspan = 2,
                               padx = (0, 40), pady = (35, 0))
        self.buttonFSKU=tk.Button(text = "Search By SKU",
                                  command=self.findBySKU)
        self.buttonFSKU.grid(row = 5, column = 4, columnspan = 2,
                             padx = (0, 5), pady = (35, 0))

        
        self.orChooseLabel=tk.Label(text = "or")
        self.orChooseLabel.grid(row = 6, column = 1, columnspan = 30,
                                sticky = "W" + "E")


        self.productEntry=tk.Entry(textvariable = self.productFind,
                                   width = 25)
        self.productEntry.grid(row = 7, column = 1, columnspan = 4,
                               padx = (0, 30))
        self.buttonFProd=tk.Button(text = "Search By Product Name",
                                   command=self.findByName)
        self.buttonFProd.grid(row = 7, column = 2, columnspan = 4,
                              padx = (100, 0))

        
        self.buttonUpdate=tk.Button(text = "Update Item",
                                    command=self.updateItem)
        self.buttonUpdate.grid(row = 8, column = 2, columnspan = 2,
                               pady =(35, 0))
        self.buttonNew=tkinter.Button(text = "Create New Product",
                                      command=self.newProduct)
        self.buttonNew.grid(row = 8, column = 4, columnspan = 2,
                            padx = (0, 20), pady = (35, 0))

        
        self.buttonBack=tk.Button(text = "Back",
                                  command=self.goBack)
        self.buttonBack.grid(row = 10, column = 3,
                             pady = (10, 0))
        self.buttonClear=tk.Button(text = "Clear Form",
                                   command=self.clearForm)
        self.buttonClear.grid(row = 10, column = 4,
                              padx = (0, 0), pady = (10, 0))
        self.quitButton=tk.Button(text = "Quit",
                                  command=self.mainWindow.destroy)
        self.quitButton.grid(row = 10, column = 5, columnspan = 2,
                             padx = (0, 50), pady = (10, 0))        


        tk.mainloop()



    def findBySKU(self):
        skuFind = str(self.skuFindEntry.get())


        if skuFind == "":
            tkinter.messagebox.showinfo("Error",
                "You must enter a sku to search for a product.")
        else:
            resultName = inventoryModule.findProductBySKU(skuFind)[0]
            if resultName == " ":
                tkinter.messagebox.showinfo("Error",
                    "Product not found. Please check SKU and try again or log a new product.")
            else:
                results = inventoryModule.populateScreenFromSKU(skuFind)


                self.title.set(resultName)
                self.category.set(results.Category)
                self.sku.set(skuFind)
                self.msrp.set(results.MSRP)
                self.qoh.set(results.QOH)
                self.productFind.set("")                


    def findByName(self):
        productFind = str(self.productEntry.get())


        if productFind == "":
            tkinter.messagebox.showinfo("Error",
                "You must enter a product name to search for a product.")
        else:
            resultName = inventoryModule.findProductByName(productFind)[0]
            if resultName == " ":
                tkinter.messagebox.showinfo("Error",
                    "Product not found. Please check product name and try again or log a new product.")
            else:
                results = inventoryModule.populateScreenFromTitle(productFind)

                
                self.title.set(resultName)
                self.category.set(results.Category)
                self.sku.set(results.SKU)
                self.msrp.set(results.MSRP)
                self.qoh.set(results.QOH)
                self.skuFind.set("")


    def updateItem(self):
        title = str(self.titleEntry.get())
        category = str(self.categoryEntry.get())
        sku = str(self.skuEntry.get())
        msrp = str(self.msrpEntry.get())
        qoh = str(self.qohEntry.get())
        
        # validate that user has entered a name
        if title == "":
            tkinter.messagebox.showinfo("Error",
                "You must enter a product name to update a product.")
        else:
            cursor.execute("""
                SELECT Title from Stock
                WHERE Title = ?
                """ , title)
            result = cursor.fetchone()
            if result is None:
                tkinter.messagebox.showinfo("Error",
                    "Product not found. Please check title and try again or create a new product.")
            else:
                if category != "": 
                    inventoryModule.updateCategory(category, title)
                if sku != "": 
                    inventoryModule.updateSKU(sku, title)
                if msrp != "": 
                    inventoryModule.updateMSRP(msrp, title)
                if qoh != "": 
                   inventoryModule.updateQOH(qoh, title)


                tkinter.messagebox.showinfo("Message",
                    "Product updated successfully.")


    def newProduct(self):
        title = str(self.titleEntry.get())
        category = str(self.categoryEntry.get())
        sku = str(self.skuEntry.get())
        msrp = str(self.msrpEntry.get())
        qoh = str(self.qohEntry.get())


        if title == "":
            tkinter.messagebox.showinfo("Error",
                "You must enter a title to create a new product.")
        else:
            inventoryModule.newTitle(title)
            if category != "":
                inventoryModule.updateCategory(category, title)
            if sku != "":
                inventoryModule.updateSKU(sku, title)
            if msrp != "":
                inventoryModule.updateMSRP(msrp, title)
            if qoh != "":
               inventoryModule.updateQOH(qoh, title)


            tkinter.messagebox.showinfo("Message",
                "New product created successfully.")
    


    def goBack(self):
        self.mainWindow.destroy()
        main.selector()


    def clearForm(self):
        clearValue = ""
        self.title.set(clearValue)
        self.category.set(clearValue)
        self.sku.set(clearValue)
        self.msrp.set(clearValue)
        self.qoh.set(clearValue)
        self.skuFind.set(clearValue)
        self.productFind.set(clearValue)


if __name__ == "__main__":
    inventory = inventory()
