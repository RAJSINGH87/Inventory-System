import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcustomersfind():

    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('Customers')
    r=Label(t,text='Customer Find Form',font=('arial',20),fg='red',bg='white')
    r.place(x=120,y=10)
    t.config(bg='yellow')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select cname,email,phone from customers where custid=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        db.close()
    a=Label(t,text='Custid')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=400,y=50)
    b=Label(t,text='Cname')
    b.place(x=50,y=100)
    e2=Entry(t,width=20)
    e2.place(x=400,y=100)
    c=Label(t,text='Email')
    c.place(x=50,y=150)
    e3=Entry(t,width=20)
    e3.place(x=400,y=150)
    d=Label(t,text='Phone')
    d.place(x=50,y=200)
    e4=Entry(t,width=20)
    e4.place(x=400,y=200)
    bt1=Button(t,text='Find',width=20,command=finddata)
    bt1.place(x=50,y=250)
    t.mainloop()