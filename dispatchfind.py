import tkinter
from tkinter import*
import pymysql
from tkinter import messagebox
def showdispatchfind():
    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('My Screen ')
    r=Label(t,text='Dispatch Find Form',font=('arial',20),fg='black',bg='pink')
    r.place(x=120,y=10)
    t.config(bg='teal')
    def finddata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="select orderno,dispatchdate from dispatch where billno=%d"%(xa)
        cur.execute(sql)
        data=cur.fetchone()
        e2.insert(0,data[0])
        e3.insert(0,data[1])
        db.close()  
    def close():
        t.destroy()
    a=Label(t,text='bill no')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=300,y=50)
    bt=Button(t,text='find',width=10,command=finddata)
    bt.place(x=50,y=100)
    a=Label(t,text='order no')
    a.place(x=50,y=150)
    e2=Entry(t,width=20)
    e2.place(x=300,y=150)
    a=Label(t,text='dispatchdate')
    a.place(x=50,y=200)
    e3=Entry(t,width=20)
    e3.place(x=300,y=200)
    bt=Button(t,text='close',width=10,command=close)
    bt.place(x=300,y=250)
    
    t.mainloop()