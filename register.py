from tkinter import*
from PIL import Image,ImageTk #pip install pillow
from tkinter import ttk,messagebox
# import pymysql # pip install pymysql
import sqlite3
import os
class Register:
    def __init__(self,root):
        self.root=root 
        self.root.title("Registration Window")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #==Bg Images==
        self.bg=ImageTk.PhotoImage(file="images/b2.jpg")
        bg=Label(self.root,image=self.bg).place(x=250,y=0,relwidth=1,relheight=1)

        #===LEFT Images=====
        self.left=ImageTk.PhotoImage(file="images/side.png")
        left=Label(self.root,image=self.left).place(x=80,y=100,width=400,height=500)

        #====Register Frame=====
        frame1=Frame(self.root,bg="white")
        frame1.place(x=480,y=100,width=700,height=500)

        title=Label(frame1,text="REGISTER HERE",font=("times new roman",20,"bold"),bg="white",fg="green").place(x=50,y=30)

        #--left_side_entries======
        # self.var_fname=StringVar()
        f_name=Label(frame1,text="First Name",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=50,y=100)
        self.txt_fname=Entry(frame1,font=("times new roman",15),bg="lightgrey",)
        self.txt_fname.place(x=50,y=140,width=250)

        Contact_no=Label(frame1,text="Contact No.",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=50,y=180)
        self.txt_contact_no=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_contact_no.place(x=50,y=220,width=250)

        Security_Q=Label(frame1,text="Select Security Question",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=50,y=260)
        self.cmb_quest=ttk.Combobox(frame1,font=("times new roman",13),state='readonly',justify='center')
        self.cmb_quest['values']=("select","Your First Pet Name","Your Birth Place","Your Best Friend Name")
        self.cmb_quest.place(x=50,y=300,width=250)
        self.cmb_quest.current(0)

        Password=Label(frame1,text="Password",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=50,y=340)
        self.txt_password=Entry(frame1,font=("times new roman",15),bg="lightgrey")        
        self.txt_password.place(x=50,y=380,width=250)


        #--right_side_entries=======
        l_name=Label(frame1,text="Last Name",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=370,y=100)
        self.txt_lname=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_lname.place(x=370,y=140,width=250)


        email=Label(frame1,text="email",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=370,y=180)
        self.txt_email=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_email.place(x=370,y=220,width=250)

        Security_ans=Label(frame1,text="Security Answer",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=370,y=260)
        self.txt_answer=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_answer.place(x=370,y=300,width=250)


        Confirm_pwd=Label(frame1,text="Confirm Password",font=("times new roman",20,"bold"),bg="White",fg="grey").place(x=370,y=340)
        self.txt_confirm_pwd=Entry(frame1,font=("times new roman",15),bg="lightgrey")
        self.txt_confirm_pwd.place(x=370,y=380,width=250)

        #---terms-------
        self.var_chk=IntVar()
        chk=Checkbutton(frame1,text="I Agree The Terms & Conditions",variable=self.var_chk,onvalue=1,offvalue=0,bg='white',font=("times new roman",12)).place(x=50,y=420)

        self.btn_img=ImageTk.PhotoImage(file="images/register.png")
        btn_register=Button(frame1,image=self.btn_img,bd=0,cursor='hand2',command=self.register_data).place(x=50,y=450)
        btn_login=Button(self.root,text='Sign In',font=('times new roman',20),bd=0,cursor='hand2',command=self.login_window).place(x=200,y=500,width=180)


    def clear(self):
        self.txt_fname.delete(0,END)
        self.txt_lname.delete(0,END)
        self.txt_contact_no.delete(0,END)
        self.txt_email.delete(0,END)
        self.cmb_quest.current(0)
        self.txt_answer.delete(0,END)
        self.txt_password.delete(0,END)
        self.txt_confirm_pwd.delete(0,END)

    def login_window(self):
        self.root.destroy()
        os.system("python login.py")


    def register_data(self):
        if self.txt_fname.get()=="" or self.txt_email.get()=="" or self.txt_contact_no.get()=="" or self.cmb_quest.get()=="Select" or self.txt_answer.get()=="" or self.txt_password.get()=="" or self.txt_confirm_pwd.get()=="":
            messagebox.showerror("Error","All Fields Are Required",parent=self.root)

        elif self.txt_password.get()!=self.txt_confirm_pwd.get(): 
            messagebox.showerror("Error","Password And Confirm Password Should Be Same",parent=self.root)
        elif self.var_chk.get()==0:
            messagebox.showerror("Error","Please Agree Our Terms & Conditions",parent=self.root)

        else:
            try:
                con=sqlite3.connect(database="SRMS.db")
                cur=con.cursor()
                cur.execute("select*from employee where email=?",(self.txt_email.get(),))
                row=cur.fetchone()
                print(row)
                if row!=None:
                    messagebox.showerror("Error","User Already Exist,please try with another email",parent=self.root)
                else:    
                    cur.execute("insert into employee(f_name,l_name,contact,email,question,answer,password) values(?,?,?,?,?,?,?)",
                                
                            (   self.txt_fname.get(),
                                self.txt_lname.get(),
                                self.txt_email.get(),
                                self.cmb_quest.get(),
                                self.txt_answer.get(),
                                self.txt_password.get(),
                                self.txt_confirm_pwd.get()
                            ))
                con.commit()
                con.close()
                messagebox.showinfo("Success","Register Successfully",parent=self.root)   
                self.clear()
                self.login_window() 
            except Exception as es:
                messagebox.showerror("Error",f"Error Due to: {str(es)}",parent=self.root)



        
root=Tk()
obj=Register(root)
root.mainloop()     