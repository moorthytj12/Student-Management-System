from tkinter import *
from tkinter import ttk
import sqlite3

          #===========================================DATABASE CONNECT=================================================
c = sqlite3.connect('management.db')
curses=c.cursor()
curses.execute("CREATE TABLE IF NOT EXISTS management (ID INTEGER ,NAME VARCHAR(30),AGE INTEGER,DOB VARCHAR (30),GENDER VARCHAR(30),CITY VARCHAR(30))")
c.commit()
c.close()


#===============================================CREATING CLASS=============================================
class Student:
    def _init_(self,main):
        self.main=main
        self.T_Frame =Frame(self.main, height=50,width=1200,background="blue",bd=5 ,relief=GROOVE)
        self.T_Frame.pack()
        self.Title=Label(self.T_Frame,text="STUDENT MANAGEMENT SYSTEM",font="TimesNewRoman 20 bold", width=1200,bg="yellow")
        self.Title.pack()

        #====================================FRAME ONNU===================================================
        #===============================LABELS & ENTRIES==================================================

        self.Frame_1 = Frame(self.main,height=580 ,width=400,bd=2,relief=GROOVE,bg="orange")
        self.Frame_1.pack(side=LEFT)
        self.Frame_1.pack_propagate(0)
      #=================================================LABEL=================================================
        Label(self.Frame_1,text="STUDENT DETAILS", background="red", font="arial 12 bold ").place(x=20,y=20)
                                       #>>>>>ID<<<<<
        self.Id = Label(self.Frame_1,text="ID NUMBER",background="blue",font="arial 11 bold")
        self.Id.place(x=40,y=60)
        self.Id_Entry=Entry(self.Frame_1,width=40)
        self.Id_Entry.place(x=150,y=60)
                                    # >>>>>NAME<<<<<
        self.Name = Label(self.Frame_1, text="NAME", background="blue", font="arial 11 bold")
        self.Name.place(x=40, y=100)
        self.Name_Entry = Entry(self.Frame_1, width=40)
        self.Name_Entry.place(x=150, y=100)
                                     # >>>>>AGE<<<<<
        self.Age = Label(self.Frame_1, text="AGE", background="blue", font="arial 11 bold")
        self.Age.place(x=40, y=140)
        self.Age_Entry = Entry(self.Frame_1, width=40)
        self.Age_Entry.place(x=150, y=140)
                                      # >>>>>DOB<<<<<
        self.DOB = Label(self.Frame_1, text="DOB", background="blue", font="arial 11 bold")
        self.DOB.place(x=40, y=180)
        self.DOB_Entry = Entry(self.Frame_1, width=40)
        self.DOB_Entry.place(x=150, y=180)
                                       # >>>>>GENDER<<<<<
        self.Gender = Label(self.Frame_1, text="GENDER", background="blue", font="arial 11 bold")
        self.Gender.place(x=40, y=220)
        self.Gender_Entry = Entry(self.Frame_1, width=40)
        self.Gender_Entry.place(x=150, y=220)
                                          # >>>>>CITY<<<<<
        self.City = Label(self.Frame_1, text="CITY", background="blue", font="arial 11 bold")
        self.City_Entry = Entry(self.Frame_1, width=40)
        self.City_Entry.place(x=150, y=260)
        self.City.place(x=40, y=260)


#=======================================BUTTON====================================================

        self.Button_Frame = Frame(self.Frame_1,height=250,width=250, relief=GROOVE,bd=2,background="black")
        self.Button_Frame.place(x =80,y =300)

#==========================================ADD Button============================================
        self.Add = Button(self.Button_Frame,text="ADD",width=25,font="arial 11 bold",command=self.Add)
        self.Add.pack()

#========================================DELETE BUTTON============================================
        self.Delete = Button(self.Button_Frame,text="DELETE",width=25,font="arial 11 bold",command=self.Delete)
        self.Delete.pack()
#=========================================UPDATE BUTTON===========================================
        self.Update = Button(self.Button_Frame,text="UPDATE",width=25,font="arial 11 bold",command=self.Update)
        self.Update.pack()
#=========================================CLEAR BUTTON===========================================
        self.Clear = Button(self.Button_Frame,text="CLEAR",width=25,font="arial 11 bold",command=self.Clear)
        self.Clear.pack()



             #=============================================FRAME RENDU==================================================
        self.Frame_2 = Frame(self.main,height=580 ,width=800,bd=2,relief=GROOVE,bg="white")
        self.Frame_2.pack(side=RIGHT)

             #===========================================CREATING COLUMNS===============================================
        self.tree = ttk.Treeview(self.Frame_2, columns=("c1", "c2", "c3", "c4", "c5", "c6"), show='headings', height = 25)
        # >>>>>ID<<<<<
        self.tree.column("#1", anchor = CENTER, width=40)
        self.tree.heading("#1", text="ID")
        # >>>>>NAME<<<<<
        self.tree.column("#2", anchor=CENTER)
        self.tree.heading("#2", text="NAME")
        # >>>>>DOB<<<<<
        self.tree.column("#3", anchor=CENTER, width=115)
        self.tree.heading("#3", text="DOB")
        # >>>>>AGE<<<<<
        self.tree.column("#4", anchor=CENTER, width=110)
        self.tree.heading("#4", text="AGE")
        # >>>>>GENDER<<<<<
        self.tree.column("#5", anchor=CENTER, width=110)
        self.tree.heading("#5", text="GENDER")
        # >>>>>CITY<<<<<
        self.tree.column("#6", anchor=CENTER)
        self.tree.heading("#6", text="CITY")
        self.tree.pack()
         #===========================ADDING  FUNCTIONS FOR BUTTON=====================================================
                    #==============================ADD BUTTON===============================
    def Add(self):
         id    =self.Id_Entry.get()
         name  =self.Name_Entry.get()
         age   =self.Age_Entry.get()
         dob   =self.DOB_Entry.get()
         gender=self.Gender_Entry.get()
         city  =self.City_Entry.get()

         c = sqlite3.connect("management.db")
         curses = c.cursor()
         curses.execute("INSERT INTO management(ID,NAME,AGE,DOB,GENDER,CITY)VALUES(?,?,?,?,?,?)",(id,name,age,dob,gender,city))
         c.commit()
         c.close()
         print("value Inserted")
         self.tree.insert("", index=0, values=(id,name, age, dob, gender, city))

                        #=============================DELETE BUTTON==============================
    def Delete(self):
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item,)['values'][0]
        print(selected_item)
        c = sqlite3.connect("management.db")
        curses = c.cursor()
        curses.execute("DELETE FROM management WHERE ID={}".format(selected_item))
        print("DELETED")
        c.commit()
        c.close()
        self.tree.delete(item)

                        #============================>UPDATE BUTTON<==============================
    def Update(self):
        id = self.Id_Entry.get()
        name = self.Name_Entry.get()
        age = self.Age_Entry.get()
        dob = self.DOB_Entry.get()
        gender = self.Gender_Entry.get()
        city = self.City_Entry.get()
        item = self.tree.selection()[0]
        selected_item = self.tree.item(item)['values'][0]
        c = sqlite3.connect("management.db")
        curses = c.cursor()
        curses.execute("UPDATE management SET ID=?,NAME=?,AGE=?,DOB=?,GENDER=?,CITY=? WHERE ID=?",(selected_item,name,age,dob,gender,city,selected_item))
        c.commit()
        c.close()
        print("VALUES UPDATED")

        self.tree.item(item,values=(id,name, age, dob, gender, city))

                        #===========================>CLEAR BUTTON<================================
    def Clear(self):
        self.Id_Entry.delete(0,END )
        self.Name_Entry.delete(0 ,END)
        self.Age_Entry.delete(0 ,END)
        self.DOB_Entry.delete(0 ,END)
        self.Gender_Entry.delete(0 ,END)
        self.City_Entry.delete(0  ,END)


main =Tk()
main.title("Student Management System")
main.resizable(False, False)
main.geometry("1200x600")

Student(main)
main.mainloop()
