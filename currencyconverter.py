#import web scraping tools to extract relveant information from google. 
import urllib
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import ttk
import tkinter.font as tkFont
import pickle
import os.path
from tkinter import messagebox
fmoney = ''
currencypairs = {} # create an empty dicotnairy to store the currency info.

def currencyLookup(fmoney):
 headers = {
         'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
     }
 currency = fmoney.replace(" ", "+")
 URL = 'https://www.google.com/search?rlz=1C1GCEA_enGB950GB950&q=' + currency
 page = requests.get(URL, headers=headers)
 soup = BeautifulSoup(page.content, 'html.parser')
 euro = soup.find('div',class_='b1hJbf')
 currency = euro.attrs['data-exchange-rate']
 return currency

class App:
    def __init__(self, root):
     
        #setting title
        root.title("CurrencyConverter")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        # Create User interface controls
        GButton_58=tk.Button(root)
        GButton_58["bg"] = "#efefef"
        ft = tkFont.Font(family='Times',size=10)
        GButton_58["font"] = ft
        GButton_58["fg"] = "#000000"
        GButton_58["justify"] = "center"
        GButton_58["text"] = "Convert"
        GButton_58.place(x=50,y=50,width=70,height=25)
        GLabel_661=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_661["font"] = ft
        GLabel_661["fg"] = "#333333"
        GLabel_661["justify"] = "center"
        GLabel_661["text"] = "from"
        GLabel_661.place(x=130,y=50,width=70,height=25)
        GLabel_633=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_633["font"] = ft
        GLabel_633["fg"] = "#333333"
        GLabel_633["justify"] = "center"
        GLabel_633["text"] = "to"
        GLabel_633.place(x=130,y=70,width=70,height=25)
        n = tk.StringVar()  #create comboboxes for the currencys to search 
        frombox = ttk.Combobox(root, width = 27, textvariable = n)
        frombox['values'] = ['pound sterling', 'US dollar', 'india repuee', 'austarilia dollar', 'Brazilian real', 'Chilean peso', 'Chinese yuan', 'New Zealand dollar']
        frombox.grid(column = 1, row = 5)
        frombox.place(x=200, y =50)
        frombox.current()
        n1 = tk.StringVar()
        tobox = ttk.Combobox(root, width = 27, textvariable = n1)
        tobox['values'] = ['pound sterling', 'US dollar', 'india repuee', 'austarilia dollar', 'Brazilian real', 'Chilean peso', 'Chinese yuan', 'New Zealand dollar']
        tobox.grid(column = 1, row = 5)
        tobox.place(x=200, y =70)
        tobox.current()
        
        GLineEdit_829=tk.Entry(root)
        GLineEdit_829["borderwidth"] = "1px"
        ft = tkFont.Font(family='Times',size=10)
        GLineEdit_829["font"] = ft
        GLineEdit_829["fg"] = "#333333"
        GLineEdit_829["justify"] = "center"
        GLineEdit_829["text"] = "Entry"
        GLineEdit_829.place(x=140,y=100,width=70,height=25)
        GLabel_65=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_65["font"] = ft
        GLabel_65["fg"] = "#333333"
        GLabel_65["justify"] = "center"
        GLabel_65["text"] = "Amount:"
        GLabel_65.place(x=60,y=100,width=70,height=25)
        GLabel_66=tk.Label(root)
        ft = tkFont.Font(family='Times',size=10)
        GLabel_66["font"] = ft
        GLabel_66["fg"] = "#333333"
        GLabel_66["justify"] = "center"
        GLabel_66["text"] = "Output"
        GLabel_66.place(x=227,y=100,width=120,height=30)
        def currencycal(fromvalue, tovalue, dollar):
         money = fromvalue + " to " + tovalue
         value = currencyLookup(money)      
         cal = float(dollar) * float(value)
         GLabel_66['text'] = tovalue + " :" + str("{:.2f}".format(cal))
         return cal
                  
        GButton_58["command"] = lambda : print(currencycal(frombox.get(), tobox.get(), GLineEdit_829.get()))
    
    
        
        
if __name__ == "__main__":
 root = tk.Tk()
 app = App(root)
 root.mainloop()





