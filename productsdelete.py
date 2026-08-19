import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql 
def showproductsdelete():
    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('products')
    r=Label(t,text='product Delete Form',font=('arial',15),fg='yellow',bg='red')
    r.place(x=120,y=10)
    t.config(bg='blue')
    a=Label(t,text='Prodid')
    a.place(x=50,y=100)
    e1=Entry(t,width=20)
    e1.place(x=400,y=100)
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from products where prodid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,END)
    
    
       
    b1=Button(t,text='Delete',width=20,command=deletedata)
    b1.place(x=50,y=300)
    t.mainloop()