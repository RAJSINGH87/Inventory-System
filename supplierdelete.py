import tkinter 
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
def showsupplierdelete():
 
    t=tkinter.Tk() 
    t.geometry('700x700')
    t.title('supplier')
    r=Label(t,text='Supplier Delete Form',font=('arial',15),fg='pink',bg='green')
    r.place(x=120,y=10)
    t.config(bg='brown')
    
    a=Label(t,text='billno')
    a.place(x=50,y=100)
    e1=Entry(t,width=20)
    e1.place(x=400,y=100)
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from supplier where supplierid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,END)
    
    
       
    b1=Button(t,text='Delete',width=20,command=deletedata)
    b1.place(x=50,y=300)
    t.mainloop()