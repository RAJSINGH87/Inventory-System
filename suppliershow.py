import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showsuppliershow():

    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('store')
    r=Label(t,text='Supplier Show Form',font=('arial',20),fg='blue',bg='black')
    r.place(x=120,y=10)
    t.config(bg='brown')
    
    ta=Text(t,width=70,height=20)
    ta.place(x=100,y=50)
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        msg=""
        sql="select * from supplier"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            msg=msg+"\n"+str(r[0])
            msg=msg+"\t"+r[1]
            msg=msg+"\t"+r[2]
            msg=msg+"\t"+str(r[3])
            msg=msg+"\t"+r[4]
        db.close()
        ta.insert(END,msg)
    showdata()
    t.mainloop()
