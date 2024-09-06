from tkinter import*
from PIL import Image, ImageTk #pip install pillow
from course import CourseClass
from student import studentClass
from result import resultClass
from report import reportClass
from tkinter import messagebox
import os
import pymysql
from tkinter import*
from PIL import Image,ImageTk,ImageDraw  #pip install pillow
from datetime import*
import time
from math import*
from tkinter import messagebox
import sqlite3
import os
class SRMS:
    def __init__(self,root):
        self.root=root
        self.root.title("Student Result Management System")
        # self.root.geometry("1350x700+0+0")
        self.root.geometry("1350x700+0+0")
        self.root.config(bg="white")
        #==icons====
        self.logo_dash = Image.open("images/logo_p.png")
        self.logo_dash = ImageTk.PhotoImage(self.logo_dash)
        #===title=====
        title=Label(self.root,text="Student Result Management Syatem",padx=10,compound=LEFT,image=self.logo_dash,font=("goudy old style",20,"bold"),bg="#033054",fg="white").place(x=0,y=0,relwidth=1,height=50)
        #==menu===
        M_Frame=LabelFrame(self.root,text="Menu",font=("times new roman",15),bg="white")
        M_Frame.place(x=10,y=70,width=1900,height=80)

        btn_course = Button(M_Frame,text="Course",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor='hand2',command=self.add_course).place(x=20,y=5,width = 200,height = 40)
        btn_student = Button(M_Frame,text="Student",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor='hand2',command=self.add_student).place(x=240,y=5,width = 200,height = 40)
        btn_result = Button(M_Frame,text="Result",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor='hand2',command=self.add_result).place(x=460,y=5,width = 200,height = 40)
        btn_view = Button(M_Frame,text="View",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor='hand2',command=self.add_report  ).place(x=680,y=5,width = 200,height = 40)
        btn_logout = Button(M_Frame,text="Logout",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor='hand2',command=self.log_out).place(x=900,y=5,width = 200,height = 40)
        btn_exit = Button(M_Frame,text="Exit",font=("goudy old style",15,"bold"),bg="#0b5377",fg="white",cursor='hand2',command=self.exit_).place(x=1120,y=5,width = 200,height = 40)

        #====content_window====
        # self.bg_img=Image.open("images/bg.png")
        # self.bg_img=self.bg_img.resize((920,350),Image.ANTIALIAS)
        # self.bg_img=ImageTk.PhotoImage(self.bg_img)

        self.bg_img = Image.open("images/bg.png")
        self.bg_img = self.bg_img.resize((920, 350), Image.ANTIALIAS)
        self.bg_img = ImageTk.PhotoImage(self.bg_img)

        self.lbl_bg = Label(self.root, image=self.bg_img)
        self.lbl_bg.place(x=400, y=180, width=920, height=350)
        
        #==update_details====
        self.lbl_course=Label(self.root,text='Total Courses\n[0]',font=('goudy old style',20),bd=10,relief=RIDGE,bg='#e43b06',fg='white')
        self.lbl_course.place(x=400,y=530,width=300,height=100)

        self.lbl_students=Label(self.root,text='Total Students\n[0]',font=('goudy old style',20),bd=10,relief=RIDGE,bg='#0676ad',fg='white')
        self.lbl_students.place(x=710,y=530,width=300,height=100)

        self.lbl_results=Label(self.root,text='Total Results\n[0]',font=('goudy old style',20),bd=10,relief=RIDGE,bg='#038074',fg='white')
        self.lbl_results.place(x=1020,y=530,width=300,height=100)

        # self.lbl_bg=Label(self.root,image=self.bg_img).place(x=400,y=180,width=920,height=350)

        #===Clock====
        self.lbl=Label(self.root,text="\nClock",font=("Book Antiqus",50,"bold"),compound=BOTTOM,fg="white",bg="#081923",bd=0)
        self.lbl.place(x=10,y=180,height=450,width=350)

        self.working()

        #====footer=====
        # footer=Label(self.root,text="SRMS-Student Result Management Syatem\ncontact us for any Technical issue: 7082804025",font=("goudy old style",12),bg="#262626",fg="white").pack(side=BOTTOM,fill=x)
        footer=Label(self.root,text='SRMS-Student Result Management System\n contact us for any Technical issue: 7082804025',font=('goudy old style',12),bg="#262626",fg="white")
        footer.pack(side=BOTTOM,fill="x")
        self.update_details()

        #==============================================================================



    def update_details(self):
        con=sqlite3.connect(database="SRMS.db")
        cur=con.cursor()
        try:
            cur.execute("select * from course")
            cr=cur.fetchall()
            self.lbl_course.config(text=f"Total Courses\n[{str(len(cr))}]")
            

            cur.execute("select * from student")
            cr=cur.fetchall()
            self.lbl_students.config(text=f"Total Students\n[{str(len(cr))}]")
            

            cur.execute("select * from result1")
            cr=cur.fetchall()
            self.lbl_results.config(text=f"Total Results\n[{str(len(cr))}]")
            self.lbl_results.after(200,self.update_details)

        except Exception as ex:
            messagebox.showerror("Error",f"Error due to {str(ex)}")
    
    
    def add_course(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=CourseClass(self.new_win)

    def add_student(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=studentClass(self.new_win)

    def add_result(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=resultClass(self.new_win) 

    def add_report(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=reportClass(self.new_win)  

    def log_out(self):
        op=messagebox.askyesno("Confirm","Dou you really want to logout ?",parent=self.root)
        if op==True:
            self.root.destroy()
            os.system("python login.py")


    def exit_(self):
        op=messagebox.askyesno("Confirm","Dou you really want to exit ?",parent=self.root)
        if op==True:
            self.root.destroy()
            




    def add_students(self):
        con=pymysql.connect(host="localhost",user="root",password="",database="SMS")  

    def clock_image(self,hr,min_ ,sec_):
        clock=Image.new("RGB",(400,400),(8,25,35))
        draw=ImageDraw.Draw(clock)
        clock.save("clock_new.png")

        bg=Image.open("images/c.png")
        bg=bg.resize((300,300),Image.ANTIALIAS)
        clock.paste(bg,(50,50))

        # Formula To Rotate The AntiClock
        # angle_in_radians = angle_in_degrees*math.pi/180
        # line_length=100
        # center_x=250
        # center_y=250
        # end_x=center_x+ line_length* math.cos(angle_in_radians)
        # end_y = center_y + linr length * math.sin(angle_in_radians)

        #=====Hour Line Image====
        #    x1,y1,x2,y2
        origin=200,200
        draw.line((origin,200+50*sin(radians(hr)),200-50*cos(radians(hr))),fill="#DF005E",width=4)
        #====Minute line====
        draw.line((origin,200+80*sin(radians(min_)),200-80*cos(radians(min_))),fill="white",width=3)
        #==Second line====
        draw.line((origin,200+100*sin(radians(sec_)),200-100*cos(radians(sec_))),fill="Yellow",width=2)
        draw.ellipse((origin,210,210),fill="#1AD5D5")
        clock.save("images/clock_new.png")
    


    




    def working(self):
        h=datetime.now().time().hour
        m=datetime.now().time().minute
        s=datetime.now().time().second
        
        hr=(h/12)*360
        min_=(m/60)*360
        sec_=(s/60)*360
        self.clock_image(hr,min_,sec_)
        self.img=ImageTk.PhotoImage(file="images/clock_new.png")
        self.lbl.config(image=self.img)
        self.lbl.after(200,self.working)





    
if __name__=="__main__":   
    root = Tk()
    app = SRMS(root)
    root.mainloop()     
