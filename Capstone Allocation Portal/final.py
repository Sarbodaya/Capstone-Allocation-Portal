
                           #Import module
from tkinter import *
import sqlite3
from tkinter import messagebox
from sqlite3 import OperationalError


                            #Student's  Login
global username
def login():
    
    def interfun():
        newUser.destroy()
        newUser1()
        
    newUser=Toplevel(main)
    newUser.title("Login Page")
    
    
    Label(newUser, text="Please enter details below to login.",
          font=("Gunplay",12),fg="orange").pack()
    Label(newUser, text="").pack()
        

    UserName = Label(newUser,text="User Name :",width=45)
    UserName.pack()
    UserNameVal= Entry(newUser,width=45)
    UserNameVal.pack(pady=5)
    Password = Label(newUser,text="Password :",width=45)
    Password.pack()
    Passwordval=Entry(newUser,show="*",width=45)
    Passwordval.pack(pady=5)
    Label(newUser,text=" ").pack()
    
    def login_now():
        global username,supera
        name=UserNameVal.get()
        password= Passwordval.get()
        if(name=='' or password==''):
            messagebox.showinfo("Missing Value","Username or password empty!")
            return
        else:
            conn = sqlite3.connect('student.db')
            try:
                content=conn.execute("SELECT NAME,PASSWORD,SUPERVISOR FROM STUDENTS");
            except OperationalError:
                conn.execute("CREATE TABLE STUDENTS(NAME VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),SUPERVISOR VARCHAR(20), MESSAGE VARCHAR(50))");                 
                content=conn.execute("SELECT NAME,PASSWORD,SUPERVISOR FROM STUDENTS");
            flag =0
            
            for row in content:
                if(row[0] ==name and row[1]==password):
                    flag=1
                    username=row[0]
                    supera= row[2]
                    break
            if(flag==1):
                conn.close()
                newUser.destroy()
                ReqSupervisor()
            else:
                messagebox.showinfo("Error","Incorrect Password or Username!")  
                
            return
    Login_Now=Button(newUser,width=45,text="Login Now",bg='BLUE',fg='BLACK',command=login_now)
    Login_Now.pack()
    Register=Button(newUser,width=45,text="NEW USER?, Register!",bg='yellow',fg='BLACK',command=interfun)
    Register.pack()
    exits = Button(newUser,text="Exit",width=45,bg='RED',fg='WHITE',command=newUser.destroy)
    exits.pack()



                #list of supervisor for student for requesting
def ReqSupervisor():
        
    global username,supera
    
    ReqSupervisor=Toplevel(main)
    ReqSupervisor.title("List of Supervisor")
    
    ls = Listbox(ReqSupervisor,width=55,bg='black',height=3,fg='white',font=("Helvetica", "20"))
    ls.insert(1,"    Hello, "+username)
    
    if(supera!=''):
        ls.insert(2,"Supervisor already selected!")
        info ="Your supervisor is "+supera
        ls.insert(3,info)
        ls.pack()
    else:
        ls.insert(2,"No Supervisor selected,Please select any of them.")
        ls.pack()
        fst= sqlite3.connect('student.db');
        try:
            supe= fst.execute("SELECT NAME,SPECIAL FROM SUPERVISORS");
        except OperationalError:
            conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))");    
            supe= fst.execute("SELECT NAME,SPECIAL FROM SUPERVISORS");
        lk = Listbox(ReqSupervisor,width=55,height=2,font=('GUNPLAY','15'))
        index=0
        for row in supe:
            info= row[0]+ " ( "+row[1]+ " )"
            lk.insert(index,info)
            index += 1
        fst.close()
        lk.pack()
        Label(ReqSupervisor, text="").pack()
        newsup =Label(ReqSupervisor,text="Name of supervisor: *",font=("TIMES NEW ROMAN",12),width=30)
        newsup.pack()
        namesup=Entry(ReqSupervisor,width=30)
        Label(ReqSupervisor, text="").pack()
        namesup.pack()
        
        def confirms(): 
            if(messagebox.askyesno("Confirm","Are You Sure?")):
                conn =sqlite3.connect('student.db')
                try:
                    sups= conn.execute("SELECT NAME FROM SUPERVISORS");
                except OperationalError:
                    conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))");
                    sups= conn.execute("SELECT NAME FROM SUPERVISORS");
                flag =0
                for row in sups:
                    if(row[0]==namesup.get()):
                        flag=1
                        break
                if(flag==1):
                    
                    #updates for next time
                    conn.execute("UPDATE STUDENTS SET SUPERVISOR=? WHERE NAME=?;",(namesup.get(),username));
                    messagebox.showinfo("Sucess","Supervisor selected")
                    ReqSupervisor.destroy()
                else:
                    messagebox.showinfo("Failure","Supervisor name not matched!")
                conn.commit()
                conn.close()
                
        Label(ReqSupervisor, text="").pack()
        confirm = Button(ReqSupervisor,text="Select supervisor",font=("Forte",10),
                         width=30,height=2,bd=3,bg="blue",relief="raised",command=confirms)
        confirm.pack()
        #if(tkMessageBox.askyesno("confirm","Are You Sure?")):
            #print "confirm"
    exits = Button(ReqSupervisor,text="Exit",width=30,height=2,font=("Forte",10),bd=3,bg='RED',fg='WHITE',command=ReqSupervisor.destroy)
    exits.pack(side=BOTTOM)



                            #Sign Up for student
def newUser1():
    newUser=Toplevel(main)
    newUser.title("New User Student")
    Name = Label(newUser,text="Name",width=45)
    Name.pack()
    NameVal= Entry(newUser,width=45)
    NameVal.pack()
    RegNo = Label(newUser,text="Reg. No",width=45)
    RegNo.pack()
    RegNoval=Entry(newUser,width=45)
    RegNoval.pack()
    Password = Label(newUser,text="Password",width=45)
    Password.pack()
    PassVal=Entry(newUser,show="*",width=45)
    PassVal.pack()
    Specialization = Label(newUser,text="Project Name",width=45)
    Specialization.pack()
    Sepcval=Entry(newUser,width=45)
    Sepcval.pack()
    MobileNo = Label(newUser,text="Mobile No",width=45)
    MobileNo.pack()
    MobVal=Entry(newUser,width=45)
    MobVal.pack()
    EmailId = Label(newUser,text="Email Id",width=45)
    EmailId.pack()
    EmailVal=Entry(newUser,width=45)
    EmailVal.pack()
    
                            #register function for sign up for student
    def regis():
        name = NameVal.get()
        regno= RegNoval.get()
        project= Sepcval.get()
        Mobi = MobVal.get()
        email= EmailVal.get()
        passval=PassVal.get()
        if(name=='' or regno=='' or project=='' or Mobi=='' or email=='' or passval==''):
            messagebox.showinfo("Missing Value","Enter valid information")
            return
        else:
            conn=sqlite3.connect('student.db');
            #VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),MESSAGE
            try:
                conn.execute("INSERT INTO STUDENTS VALUES (?,?,?,?,?,?,?,?);",(name,regno,project,Mobi,email,passval,'',''));
            except OperationalError:
                conn.execute("CREATE TABLE STUDENTS(NAME VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),SUPERVISOR VARCHAR(20), MESSAGE VARCHAR(50))"); 
                conn.execute("INSERT INTO STUDENTS VALUES (?,?,?,?,?,?,?,?);",(name,regno,project,Mobi,email,passval,'',''));  
            conn.commit()
           # data = conn.execute("SELECT NAME,REG_NO,PROJECT,MOBILE,EMAIL,PASSWORD  from STUDENTS")
            messagebox.showinfo("Success ","Student New User Account Created!")
            newUser.destroy()
            return
    Register=Button(newUser,text="Register",width=45,height=1,bd=3,bg='BLUE',fg='BLACK' ,command=regis)
    Register.pack(pady=12)
    exits = Button(newUser,text="Exit",width=45,height=1,bd=3,bg='RED',fg='WHITE',command=newUser.destroy)
    exits.pack()

    


                            #SuperVisor page
def Supervisors_page():
    Supervisors_page= Toplevel(main)
    Supervisors_page.title("Supervisor")
    Supervisors_page.minsize(400,100)
    frame=Frame(Supervisors_page)
    frame.pack()
    login = Button(frame,fg='black',width=45,bd=5,bg='yellow',text='Login',height=2,command=Supervisor_login)
    login.pack(pady=12)
    New_user=Button(frame,fg='black',width=45,bd=5,bg='green',text='New User',height=2,command=New_Supervisor)
    New_user.pack(pady=12)
    exits = Button(Supervisors_page,text="Exit",bg='RED',fg='WHITE',width=45,height=2,bd=3,command=Supervisors_page.destroy)
    exits.pack(pady=12)



                            #Sign in for supervisor
def Supervisor_login():
    Supervisor_login=Toplevel(main)
    Supervisor_login.title("Login Supervisor")
    frame=Frame(Supervisor_login,width=45)
    frame.pack()
    UserName = Label(Supervisor_login,text="User Name",width=45)
    UserName.pack()
    UserNameVal= Entry(Supervisor_login,width=45)
    UserNameVal.pack()
    Password = Label(Supervisor_login,text="Password",width=45)
    Password.pack()
    Passwordval=Entry(Supervisor_login,show="*",width=45)
    Passwordval.pack()
    def sign_in():
        global username
        name=UserNameVal.get()
        password= Passwordval.get()
        if(name=='' or password==''):
            messagebox.showinfo("Missing Value","Username or password empty!")
            return
        else:
            conn = sqlite3.connect('student.db')
            try:
                content=conn.execute("SELECT NAME,PASSWORD FROM SUPERVISORS");
            except OperationalError:
                conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))"); 
                content=conn.execute("SELECT NAME,PASSWORD FROM SUPERVISORS");
            flag =0
            for row in content:
                if(row[0] ==name and row[1]==password):
                    flag=1
                    username=row[0]
                    break
            if(flag==1):
                Supervisor_login.destroy()
                select_student()
            else:
                messagebox.showinfo("Error","Incorrect Password or username!")        
            return
        
    Login_Now=Button(Supervisor_login,width=45,bd=3,height=1,text="Login Now",bg='BLUE',fg='BLACK' ,command=sign_in)
    Login_Now.pack(pady=12)
    exits = Button(Supervisor_login,text="Exit",width=45,bd=3,height=1,bg='RED',fg='WHITE',command=Supervisor_login.destroy)
    exits.pack()
    

                                                #SELECT STUDENT
def select_student():
    global username
    select_students=Toplevel(main)
    select_students.title("Students who selected you")
    ls = Listbox(select_students,width=45)
    ls.insert(1,"Supervisor name: "+username)
    lst= sqlite3.connect('student.db')
    supe= lst.execute("SELECT NAME,PROJECT,SUPERVISOR FROM STUDENTS");
    flag=0
    ls.insert(2,"name (project name)")
    index=3
    for row in supe:
        if(row[2]==username):
            flag=1
            index +=1
            info = row[0]+" ("+row[1]+ " )"
            ls.insert(index,info)
    if(flag==0):
        ls.insert(2,"No item found!")
    ls.pack()
    lst.close()
    exits = Button(select_students,text="Exit",width=22,bg='RED',fg='WHITE',command=select_students.destroy)
    exits.pack()



                        #sign up for new SuperVisor
def New_Supervisor():
    newUser=Toplevel(main)
    newUser.title("New User Supervisor")
    newUser.minsize(400,600)
    newUser.maxsize(400,600)
    Name = Label(newUser,text="Name",width=45)
    Name.pack()
    NameVal= Entry(newUser,width=45)
    NameVal.pack()
    UID = Label(newUser,text="UID",width=45)
    UID.pack()
    UIDval=Entry(newUser,width=45)
    UIDval.pack()
    Password = Label(newUser,text="Password",width=45)
    Password.pack()
    PassVal=Entry(newUser,show="*",width=45)
    PassVal.pack()
    Specialization = Label(newUser,text="Specialization",width=45)
    Specialization.pack()
    Sepcval=Entry(newUser,width=45)
    Sepcval.pack()
    MobileNo = Label(newUser,text="Mobile No",width=45)
    MobileNo.pack()
    MobVal=Entry(newUser,width=45)
    MobVal.pack()
    EmailId = Label(newUser,text="Email Id",width=45)
    EmailId.pack()
    EmailVal=Entry(newUser,width=45)
    EmailVal.pack()
    Label(newUser,text="").pack()
                                            #IMPORTING DATA TO SUPERVISORS
    def regisT():
        name = NameVal.get()
        uid= UIDval.get()
        passw= PassVal.get()
        Speci = Sepcval.get()
        Mobi= MobVal.get()
        Emails=EmailVal.get()
        if(name=='' or uid=='' or passw=='' or Mobi=='' or Emails=='' or Speci==''):
            messagebox.showinfo("Missing Value","Enter valid information")
            return
        else:
            conn=sqlite3.connect('student.db');
            #NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE 
            try:
                conn.execute("INSERT INTO SUPERVISORS VALUES (?,?,?,?,?,?,?);",(name,uid,passw,Speci,Mobi,Emails,''));
            except OperationalError:
                conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))"); 
                conn.execute("INSERT INTO SUPERVISORS VALUES (?,?,?,?,?,?,?);",(name,uid,passw,Speci,Mobi,Emails,''));
            conn.commit()
            messagebox.showinfo("Success ","Supervisor account created!")
            newUser.destroy()
            return
    
    Label(newUser, text="").pack()
    Register=Button(newUser,text="Register",width=45,height=2,bd=5,bg='BLUE',fg='BLACK',command = regisT)
    Register.pack(pady=12)
    #(NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30))
    exits = Button(newUser,text="Exit",bg='RED',width=45,height=2,bd=5,fg='WHITE',command=newUser.destroy)
    exits.pack()

    
                            #reset funtion
def reset():
    conn=sqlite3.connect('student.db');    
    if(messagebox.askyesno("Delete Student's data",'Are you sure? ')):
        try:
            conn.execute("DELETE  FROM STUDENTS");
        except OperationalError:
            conn.execute("CREATE TABLE STUDENTS(NAME VARCHAR(30),REG_NO VARCHAR(20),PROJECT VARCHAR(30),MOBILE VARCHAR(15), EMAIL VARCHAR(30),PASSWORD VARCHAR(30),SUPERVISOR VARCHAR(20), MESSAGE VARCHAR(50))"); 
        conn.commit()
        messagebox.showinfo("Students Table reset","Your data is now empty")
    if(messagebox.askyesno("Delete Supervisor's data","Are you sure?")):
        try:
            conn.execute("DELETE  FROM SUPERVISORS");
        except OperationalError:
            conn.execute("CREATE TABLE SUPERVISORS (NAME VARCHAR(30),UID VARCHAR(15),PASSWORD VARCHAR(25),SPECIAL VARCHAR(30),MOBILE VARCHAR(15),EMAIL VARCHAR(30),MESSAGE VARCHAR(50))");    
        conn.commit()
        messagebox.showinfo("Supervisor's Table reset","Your data is now empty")
    else:
        messagebox.showinfo("Failed to reset","Your data isn't erased!")        
    conn.close()
    return


                            #main Function
main= Tk()
main.title("Student Homepage")
main.geometry("1400x700")

Label(text=" ").pack()
Label(text=" ").pack()

#TITLE

Label(text="Capstone  Allocation  Portal  for  LPU  students",
      font=("Bernard MT Condensed",40),
      borderwidth=4,bg="yellow").pack()

Label(text=" ").pack()
Label(text=" ").pack()
Label(text=" ").pack()

#PHOTO

photo=PhotoImage(file="lpu_logo.png")
pix=Label(image=photo)
pix.pack()

Label(text=" ").pack()
Label(text=" ").pack()
Label(text=" ").pack()

frame=Frame(main)
frame.pack()

login = Button(frame,fg='black',width=10,height=2,bd=5,bg='white',text='Login',command =login)
login.pack(pady=20)
New_user=Button(frame,fg='black',width=13,height=2,bd=5,bg='white',text='New User',command=newUser1)
New_user.pack(pady=15)
Supervisor=Button(frame,fg='black',bd=5,bg='white',width=20,height=2,text='Supervisor Area',command=Supervisors_page)
Supervisor.pack(pady=15)
reset = Button(frame,fg='black',width=13,height=2,bd=5,bg='white',text='Reset',command =reset)
reset.pack(pady=15)

main.mainloop()