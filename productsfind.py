import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showproductsfind():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('products')
    r=Label(t,text='product Find Form',font=('arial',20),fg='green',bg='white')
    r.place(x=120,y=10)
    t.config(bg='blue')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select pname,catid,priceqty from products where prodid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        db.close()
    a=Label(t,text='Prodid')
    a.place(x=50,y=100)
    e1=Entry(t,width=20)
    e1.place(x=400,y=100)
    c=Label(t,text='Pname')
    c.place(x=50,y=140)
    e2=Entry(t,width=20)
    e2.place(x=400,y=140)
    e=Label(t,text='Catid')
    e.place(x=50,y=180)
    e3=Entry(t,width=20)
    e3.place(x=400,y=180)
    g=Label(t,text='Priceqty')
    g.place(x=50,y=220)
    e4=Entry(t,width=20)
    e4.place(x=400,y=220)    
    b1=Button(t,text='Find',width=20,command=finddata)
    b1.place(x=50,y=300)
    t.mainloop()