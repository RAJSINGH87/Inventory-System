import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showcategorysave():
    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('Category')
    r=Label(t,text='Category Save Form',font=('arial',20),fg='green',bg='white')
    r.place(x=120,y=10)
    t.config(bg='pink')
    def savedata():
        if len(e1.get())==0 or len(e2.get())==0 or len(e3.get())==0:
            messagebox.showinfo('Hi','Please fill all')
        else:
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            xa=e1.get()
            xb=e2.get()
            xc=e3.get()
            sql="insert into category values ('%s','%s','%s')" % (xa,xb,xc)
            cur.execute(sql)
            db.commit()
            messagebox.showinfo('Hello','Saved')
            e1.delete(0,END)
            e2.delete(0,END)
            e3.delete(0,END)
    def close():
        t.destroy()
    def checkdata():
            db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
            cur=db.cursor()
            xa=int(e1.get())
            sql="select count(*) from category where catid='%s'"%(xa)
            cur.execute(sql)
            data=cur.fetchone()
            if data[0]==0:
                messagebox.showinfo('hi','ok goahead')
            else:
                messagebox.showinfo('hi','Alreday Token')
                db.close()    
    a=Label(t,text='Catid')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=400,y=50)
    btf=Button(t,text='Check',command=checkdata)
    btf.place(x=550,y=50)
    b=Label(t,text='Catname')
    b.place(x=50,y=100)
    e2=Entry(t,width=20)
    e2.place(x=400,y=100)
    c=Label(t,text='Description')
    c.place(x=50,y=150)
    e3=Entry(t,width=20)
    e3.place(x=400,y=150)
    bt1=Button(t,text='Save',width=20,command=savedata)
    bt1.place(x=50,y=200)
    t.mainloop()