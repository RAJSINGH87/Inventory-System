import tkinter 
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import pymysql
from Inventorysystem import*
t=tkinter.Tk() 
t.geometry('700x700')
t.title('login')
r=Label(t,text='Login',font=('arial',25),fg='white',bg='black')
r.place(x=120,y=10)
t.config(bg='red')

def check():
    xa=e1.get()
    xb=e2.get()
    if xa=='raj0729' and xb=='rs0729':
        showdashboard()
    else:
        messagebox.showinfo('Hi','login failed')
        
a=Label(t,text='User id')
a.place(x=80,y=80)
e1=Entry(t,width=30)
e1.place(x=320,y=80)
b=Label(t,text='Password')
b.place(x=80,y=120)
e2=Entry(t,width=30,show='*')
e2.place(x=320,y=120)
bt=Button(t,text='Login',command=check)
bt.place(x=250,y=250) 
bt1=Button(t,text='Cancel')
bt1.place(x=350,y=250)
bt2=Button(t,text='Forgate Password')
bt2.place(x=300,y=300)
t.mainloop()






t.mainloop()




