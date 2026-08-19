import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showstockindelete():

    t=tkinter.Tk()
    t.geometry ('700x700')
    t.title('stockin')
    r=Label(t,text='Stockin Delete Form',font=('arial',15),fg='black',bg='yellow')
    r.place(x=120,y=10)
    t.config(bg='navy')
    
    def deletedata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        xa=int(e1.get())
        sql="delete from stockin where staockid=%d"%(xa)
        cur.execute(sql)
        db.commit()
        db.close()
        messagebox.showinfo('Hi','deleted')
        e1.delete(0,END)        
    a=Label(t,text='stoackid')
    a.place(x=50,y=50)
    e1=Entry(t,width=20)
    e1.place(x=300,y=50)
    bt=Button(t,text='delete',width=10,command=deletedata)
    bt.place(x=100,y=100)
    t.mainloop()
