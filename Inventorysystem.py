import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql

from storesave import *
from storefind import *
from storeupdate import *
from storeshow import *
from storedelete import *
from categorysave import *
from categoryfind import *
from categoryupdate import * 
from categoryshow import *
from categorydelete import *
from productssave import *
from productsfind import *
from productsupdate import *
from productsshow import *
from productsdelete import *
from suppliersave import *
from supplierfind import *
from supplierupdate import *
from suppliershow import * 
from supplierdelete import *
from stockinsave import *
from stockinfind import *
from stockinupdate import *
from stockinshow import *
from stockindelete import *
from customerssave import *
from customersfind import *
from customersupdate import *
from customersshow import *
from customersdelete import *
from orderssave import *
from ordersfind import *
from ordersupdate import *
from ordersshow import *
from ordersdelete import *
from billgenratesave import *
from billgenratefind import *
from billgenrateupdate import *
from billgenrateshow import *
from billgenratedelete import *
from dispatchsave import *
from dispatchfind import *
from dispatchupdate import *
from dispatchshow import *
from dispatchdelete import *

def showdashboard():
    t=tkinter.Tk()
    t.geometry('900x900')
    t.title('Inventory system')
    r=Label(t,text='Inventory System',font=('arial',20),fg='white',bg='black')
    r.place(x=120,y=10)
    t.config(bg='blue')
    
    
    a=Label(t,text='store',bg='white')
    a.place(x=50,y=50)
    
    
    b1=Button(t,text='find',bg='pink',command=showstorefind)
    b1.place(x=50,y=150)
    
    b2=Button(t,text='show',bg='pink',command=showstoreshow)
    b2.place(x=50,y=250)
    
    b3=Button(t,text='save',bg='pink',command=showstoresave)
    b3.place(x=50,y=350)
    
    b4=Button(t,text='update',bg='pink',command=showstoreupdate)
    b4.place(x=50,y=450)
    
    b5=Button(t,text='delete',bg='pink',command=showstoredelete)
    b5.place(x=50,y=550)
    
    
    
    b=Label(t,text='Category',bg='white')
    b.place(x=100,y=50)
    
    b6=Button(t,text='find',bg='red',command=showcategoryfind)
    b6.place(x=100,y=150)
    
    b7=Button(t,text='show',bg='red',command=showcategoryshow)
    b7.place(x=100,y=250)
    
    b8=Button(t,text='save',bg='red',command=showcategorysave)
    b8.place(x=100,y=350)
    
    b9=Button(t,text='update',bg='red',command=showcategoryupdate)
    b9.place(x=100,y=450)
    
    b10=Button(t,text='delete',bg='red',command=showcategorydelete)
    b10.place(x=100,y=550)
    
    
    
    c=Label(t,text='Products',bg='white')
    c.place(x=160,y=50)
    
    b11=Button(t,text='find',bg='orange',command=showproductsfind)
    b11.place(x=160,y=150)
    
    b12=Button(t,text='show',bg='orange',command=showproductsshow)
    b12.place(x=160,y=250)
    
    b13=Button(t,text='save',bg='orange',command=showproductssave)
    b13.place(x=160,y=350)
    
    b14=Button(t,text='update',bg='orange',command=showproductsupdate)
    b14.place(x=160,y=450)
    
    b15=Button(t,text='delete',bg='orange',command=showproductsdelete)
    b15.place(x=160,y=550)
    
    
    
    
    d=Label(t,text='supplier',bg='white')
    d.place(x=220,y=50)
    
    b16=Button(t,text='find',bg='brown',command=showsupplierfind)
    b16.place(x=220,y=150)
    
    b17=Button(t,text='show',bg='brown',command=showsuppliershow)
    b17.place(x=220,y=250)
    
    b18=Button(t,text='save',bg='brown',command=showsuppliersave)
    b18.place(x=220,y=350)
    
    b19=Button(t,text='update',bg='brown',command=showsupplierupdate)
    b19.place(x=220,y=450)
    
    b20=Button(t,text='delete',bg='brown',command=showsupplierdelete)
    b20.place(x=220,y=550)
    
    
    
    
    e=Label(t,text='stockin',bg='white')
    e.place(x=280,y=50)
    
    b21=Button(t,text='find',bg='purple',command=showstockinfind)
    b21.place(x=280,y=150)
    
    b22=Button(t,text='show',bg='purple',command=showstockinshow)
    b22.place(x=280,y=250)
    
    b23=Button(t,text='save',bg='purple',command=showstockinsave)
    b23.place(x=280,y=350)
    
    b24=Button(t,text='update',bg='purple',command=showstockinupdate)
    b24.place(x=280,y=450)
    
    b25=Button(t,text='delete',bg='purple',command=showstockindelete)
    b25.place(x=280,y=550)
    
    
    
    
    f=Label(t,text='customer',bg='white')
    f.place(x=350,y=50)
    
    b26=Button(t,text='find',bg='yellow',command=showcustomerfind)
    b26.place(x=350,y=150)
    
    b27=Button(t,text='show',bg='yellow',command=showcustomershow)
    b27.place(x=350,y=250)
    
    b28=Button(t,text='save',bg='yellow',command=showcustomersave)
    b28.place(x=350,y=350)
    
    b29=Button(t,text='update',bg='yellow',command=showcustomerupdate)
    b29.place(x=350,y=450)
    
    b30=Button(t,text='delete',bg='yellow',command=showcustomerdelete)
    b30.place(x=350,y=550)
    
    
    
    g=Label(t,text='orders',bg='white')
    g.place(x=420,y=50)
    
    b31=Button(t,text='find',bg='green',command=showordersfind)
    b31.place(x=420,y=150)
    
    b32=Button(t,text='show',bg='green',command=showordersshow)
    b32.place(x=420,y=250)
    
    b33=Button(t,text='save',bg='green',command=showorderssave)
    b33.place(x=420,y=350)
    
    b34=Button(t,text='update',bg='green',command=showordersupdate)
    b34.place(x=420,y=450)
    
    b35=Button(t,text='delete',bg='green',command=showordersdelete)
    b35.place(x=420,y=550)
    
    
    
    
    h=Label(t,text='billgenerate',bg='white')
    h.place(x=510,y=50)
    
    b36=Button(t,text='find',bg='skyblue',command=showbillgeneratefind)
    b36.place(x=510,y=150)
    
    b37=Button(t,text='show',bg='skyblue',command=showbillgenerateshow)
    b37.place(x=510,y=250)
    
    b38=Button(t,text='save',bg='skyblue',command=showbillgeneratesave)
    b38.place(x=510,y=350)
    
    b39=Button(t,text='update',bg='skyblue',command=showbillgenerateupdate)
    b39.place(x=510,y=450)
    
    b40=Button(t,text='delete',bg='skyblue',command=showbillgeneratedelete)
    b40.place(x=510,y=550)
    
    
    
    
    i=Label(t,text='dispatch',bg='white')
    i.place(x=600,y=50)
    
    b41=Button(t,text='find',bg='gold',command=showdispatchfind)
    b41.place(x=600,y=150)
    
    b42=Button(t,text='show',bg='gold',command=showdispatchshow)
    b42.place(x=600,y=250)
    
    b43=Button(t,text='save',bg='gold',command=showdispatchsave)
    b43.place(x=600,y=350)
    
    b44=Button(t,text='update',bg='gold',command=showdispatchupdate)
    b44.place(x=600,y=450)
    
    b45=Button(t,text='delete',bg='gold',command=showdispatchdelete)
    b45.place(x=600,y=550)
    
    t.mainloop()