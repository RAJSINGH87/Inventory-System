import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql 
def showcustomerssave():

    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('Customers')
    r=Label(t,text='Customer Save Form',font=('arial',20),fg='green',bg='white')
    r.place(x=120,y=10)
    t.config(bg='yellow')
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0 or len(e4.get())==0:
            messagebox.showinfo('Hi','Please fill all')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            xa=int(e1.get())
            xb=e2.get()
            xc=e3.get()
            xd=e4.get()
            sql="insert into customers values (%d,'%s','%s','%s')" % (xa,xb,xc,xd)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Hello','Saved')
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
            e4.delete(0,END)
    def close():
        t.destroy()
    def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            xa=int(e1.get())
            sql="select count(*) from customers where custid=%d"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hi','ok goahead')
            else:
                messagebox.showinfo('hi','Alreday Token')
                db.close()    
    
    a=Label(t,text='Customerid')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=400,y=50)
    btf=Button(t,text='Check',command=checkdata)
    btf.place(x=550,y=50)
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
    bt1=Button(t,text='Save',width=20,command=savedata)
    bt1.place(x=50,y=250)
    t.mainloop()