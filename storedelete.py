import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql 
def showstoredelete():
    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('Store')
    r=Label(t,text='Store Delete Form',font=('arial',15),fg='orange',bg='black')
    r.place(x=120,y=10)
    t.config(bg='red')
    a=Label(t,text='Store id')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=400,y=50)
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from store where storeid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,END)
    
    
    bt1=Button(t,text='Delete',width=20,command=deletedata)
    bt1.place(x=50,y=350)
    t.mainloop()