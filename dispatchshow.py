import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
def showdispatchshow():
    
    t=tkinter.Tk()
    t.geometry('700x700')
    t.title('dispatch')
    r=Label(t,text='Dispatch Show Form',font=('arial',20),fg='orange',bg='brown')
    r.place(x=120,y=10)
    t.config(bg='teal')
    
    ta=Text(t,width=70,height=20)
    ta.place(x=100,y=50)
    def showdata():
        db=pymysql.connect(host='localhost',user='root',password='root',database='ims')
        cur=db.cursor()
        msg=""
        sql="select * from dispatch"
        cur.execute(sql)
        data=cur.fetchall()
        for r in data:
            msg=msg+"\n"+str(r[0])
            msg=msg+"\t"+r[1]
            msg=msg+"\t"+r[2]
        db.close()
        ta.insert(END,msg)
    showdata()
    t.mainloop()
    
