import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showordersfind():

    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('order')
    r=Label(t,text='Order Find Form',font=('arial',20),fg='white',bg='black')
    r.place(x=120,y=10)
    t.config(bg='purple')
    
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select custid,prodid,qty from orders where orderno=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        e4.insert(0,data[2])
        db.close()  
    def close():
        t.destroy()
    a=Label(t,text='orderno')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=300,y=50)
    c=Label(t,text='custid')
    c.place(x=50,y=150)
    e2=Entry(t,width=20)
    e2.place(x=400,y=150)
    d=Label(t,text='prodid')
    d.place(x=50,y=200)
    e3=Entry(t,width=20)
    e3.place(x=400,y=200)
    f=Label(t,text='qty')
    f.place(x=50,y=250)
    e4=Entry(t,width=20)
    e4.place(x=400,y=250)
    bt1=Button(t,text='find',width=20,command=finddata)
    bt1.place(x=50,y=350)
    t.mainloop()