import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcategoryfind():
    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('Category')
    r=Label(t,text='Category Find Form',font=('arial',20),fg='black',bg='white')
    r.place(x=120,y=10)
    t.config(bg='pink')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select catname,description from category where catid='%s'"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()
    a=Label(t,text='Catid')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=400,y=50)
    b=Label(t,text='Catname')
    b.place(x=50,y=100)
    e2=Entry(t,width=20)
    e2.place(x=400,y=100)
    c=Label(t,text='Description')
    c.place(x=50,y=150)
    e3=Entry(t,width=20)
    e3.place(x=400,y=150)
    bt1=Button(t,text='Find',width=20,command=finddata)
    bt1.place(x=50,y=200)
    t.mainloop()