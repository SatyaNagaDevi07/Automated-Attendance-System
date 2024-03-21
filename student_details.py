from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #===========variables
        self.var_dep=StringVar()
        self.var_stream=StringVar()
        self.var_year=StringVar()
        self.var_semster=StringVar()
        self.var_stid=StringVar()
        self.var_stdname=StringVar()
        self.var_div=StringVar()
        self.var_roll=StringVar()
        self.var_gender=StringVar()
        self.var_dob=StringVar()
        self.var_email=StringVar()
        self.var_phone=StringVar()
        self.var_address=StringVar()
        self.var_teacher=StringVar()


        #centre img--student details
        img=Image.open(r"D:\Face_recognition_system\images\hero-facial-recognition.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #background img
        bimg=Image.open(r"D:\Face_recognition_system\images\th.jpeg")
        bimg=bimg.resize((1530,710),Image.ANTIALIAS)
        self.photobimg=ImageTk.PhotoImage(bimg)

        b_img=Label(self.root,image=self.photobimg)
        b_img.place(x=0,y=130,width=1530,height=710)

        #main label
        title_lbl=Label(b_img,text="Student Details",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        main_frame=Frame(b_img,bd=2,bg="white")
        main_frame.place(x=10,y=55,width=1500,height=600)

        #left label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=740,height=580)

        img_left=Image.open(r"D:\Face_recognition_system\images\hero-facial-recognition.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg)
        f_lbl.place(x=5,y=0,width=720,height=130)


        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=720,height=110)

        #Department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"))
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,textvariable=self.var_dep,font=("times new roman",12,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","CSE","CSD","CSM","IT","ECE")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10)

        #programme
        stream_label=Label(current_course_frame,text="Stream",font=("times new roman",13,"bold"),bg="white")
        stream_label.grid(row=0,column=2,padx=10,sticky=W)

        stream_combo=ttk.Combobox(current_course_frame,textvariable=self.var_stream,font=("times new roman",13,"bold"),state="readonly",width=20)
        stream_combo["values"]=("Select Stream","B.Tech","M.tech")
        stream_combo.current(0)
        stream_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,textvariable=self.var_year,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","1","2","3","4")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semster
        sem_label=Label(current_course_frame,text="Semster",font=("times new roman",13,"bold"),bg="white")
        sem_label.grid(row=1,column=2,padx=10,sticky=W)

        sem_combo=ttk.Combobox(current_course_frame,textvariable=self.var_semster,font=("times new roman",13,"bold"),state="readonly",width=20)
        sem_combo["values"]=("Select Year","1","2","3","4","5","6","7","8")
        sem_combo.current(0)
        sem_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=720,height=300)
        

        #student id label
        id_label=Label(class_student_frame,text="Student ID:",font=("times new roman",13,"bold"),bg="white")
        id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        id_entry=ttk.Entry(class_student_frame,textvariable=self.var_stid,width=20,font=("times new roman",13,"bold"))
        id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        name_label=Label(class_student_frame,text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        name_entry=ttk.Entry(class_student_frame,textvariable=self.var_stdname,width=20,font=("times new roman",13,"bold"))
        name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        div_label=Label(class_student_frame,text="Student class:",font=("times new roman",13,"bold"),bg="white")
        div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        div_combo=ttk.Combobox(class_student_frame,textvariable=self.var_div,font=("times new roman",13,"bold"),state="readonly",width=18)
        div_combo["values"]=("A","B","C","D")
        div_combo.current(0)
        div_combo.grid(row=1,column=1,padx=2,pady=5,sticky=W)

        #roll no
        roll_label=Label(class_student_frame,text="Roll no:",font=("times new roman",13,"bold"),bg="white")
        roll_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_entry=ttk.Entry(class_student_frame,textvariable=self.var_roll,width=20,font=("times new roman",13,"bold"))
        roll_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gen_label=Label(class_student_frame,text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gen_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_combo=ttk.Combobox(class_student_frame,textvariable=self.var_gender,font=("times new roman",13,"bold"),state="readonly",width=18)
        gender_combo["values"]=("Male","Female","Other")
        gender_combo.current(0)
        gender_combo.grid(row=2,column=1,padx=2,pady=5,sticky=W)

        #dob label
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",13,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_entry=ttk.Entry(class_student_frame,textvariable=self.var_dob,width=20,font=("times new roman",13,"bold"))
        dob_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        mail_label=Label(class_student_frame,text="Email:",font=("times new roman",13,"bold"),bg="white")
        mail_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        mail_entry=ttk.Entry(class_student_frame,textvariable=self.var_email,width=20,font=("times new roman",13,"bold"))
        mail_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone
        phone_label=Label(class_student_frame,text="Phone:",font=("times new roman",13,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_entry=ttk.Entry(class_student_frame,textvariable=self.var_phone,width=20,font=("times new roman",13,"bold"))
        phone_entry.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #address
        add_label=Label(class_student_frame,text="Address:",font=("times new roman",13,"bold"),bg="white")
        add_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        add_entry=ttk.Entry(class_student_frame,textvariable=self.var_address,width=20,font=("times new roman",13,"bold"))
        add_entry.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher
        tea_label=Label(class_student_frame,text="Teacher:",font=("times new roman",13,"bold"),bg="white")
        tea_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        tea_entry=ttk.Entry(class_student_frame,textvariable=self.var_teacher,width=20,font=("times new roman",13,"bold"))
        tea_entry.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio buttons
        self.var_radio1=StringVar()
        radiob1=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="take photo sample",value="Yes")
        radiob1.grid(row=6,column=0)

        radiob2=ttk.Radiobutton(class_student_frame,variable=self.var_radio1,text="no photo sample",value="No")
        radiob2.grid(row=6,column=1)

        #buttons frame
        bt_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        bt_frame.place(x=0,y=200,width=715,height=35)

        save_btn=Button(bt_frame,text="save",command=self.add_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(bt_frame,text="Update",command=self.update_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(bt_frame,text="Delete",command=self.delete_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(bt_frame,text="Reset",command=self.reset_data,width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)


        bt_frame1=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        bt_frame1.place(x=0,y=235,width=715,height=35)

        take_ph_btn=Button(bt_frame1,command=self.generate_dataset,text="Take Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_ph_btn.grid(row=0,column=0)

        update_ph_btn=Button(bt_frame1,text="Update Photo Sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_ph_btn.grid(row=0,column=1)

        


        #right label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        right_frame.place(x=760,y=10,width=730,height=580)

        img_right=Image.open(r"D:\Face_recognition_system\images\hero-facial-recognition.jpg")
        img_right=img_right.resize((720,130),Image.ANTIALIAS)
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(right_frame,image=self.photoimg)
        f_lbl.place(x=5,y=0,width=720,height=130)

        # ==========search sytem=============
        search_frame=LabelFrame(right_frame,bd=2,bg="white",relief=RIDGE,text="Search information",font=("times new roman",12,"bold"))
        search_frame.place(x=5,y=135,width=710,height=70)

        search_label=Label(search_frame,text="Search By:",font=("times new roman",15,"bold"),bg="blue",fg="white")
        search_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        search_combo=ttk.Combobox(search_frame,font=("times new roman",13,"bold"),state="readonly",width=15)
        search_combo["values"]=("Select","roll no","phone no")
        search_combo.current(0)
        search_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        search_entry=ttk.Entry(search_frame,width=15,font=("times new roman",13,"bold"))
        search_entry.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        search_btn=Button(search_frame,text="Search",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        search_btn.grid(row=0,column=3,padx=4)

        showAll_btn=Button(search_frame,text="Show All",width=12,font=("times new roman",12,"bold"),bg="blue",fg="white")
        showAll_btn.grid(row=0,column=4,padx=4)

        # ================table frame
        table_frame=Frame(right_frame,bd=2,bg="white",relief=RIDGE)
        table_frame.place(x=5,y=210,width=710,height=350)

        scroll_x=Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_frame,orient=VERTICAL)

        self.student_table=ttk.Treeview(table_frame,column=("dep","stream","year","sem","id","name","div","roll","gender","dob","email","phone","address","teacher","photo"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        self.student_table.heading("dep",text="Dep")
        self.student_table.heading("stream",text="Stream")
        self.student_table.heading("year",text="Year")
        self.student_table.heading("sem",text="Semster")
        self.student_table.heading("id",text="Student_id")
        self.student_table.heading("name",text="Name")
        self.student_table.heading("div",text="Division")
        self.student_table.heading("roll",text="Roll")
        self.student_table.heading("gender",text="Gender")
        self.student_table.heading("dob",text="DOB")
        self.student_table.heading("email",text="Email")
        self.student_table.heading("phone",text="Phone")
        self.student_table.heading("address",text="Address")
        self.student_table.heading("teacher",text="Teacher")
        self.student_table.heading("photo",text="PhotoSampleStatus")
        self.student_table["show"]="headings"

        self.student_table.column("dep",width=100)
        self.student_table.column("stream",width=100)
        self.student_table.column("year",width=100)
        self.student_table.column("sem",width=100)
        self.student_table.column("id",width=100)
        self.student_table.column("name",width=100)
        self.student_table.column("div",width=100)
        self.student_table.column("roll",width=100)
        self.student_table.column("gender",width=100)
        self.student_table.column("dob",width=100)
        self.student_table.column("email",width=100)
        self.student_table.column("phone",width=100)
        self.student_table.column("address",width=100)
        self.student_table.column("teacher",width=100)
        self.student_table.column("photo",width=150)
       
        self.student_table.pack(fill=BOTH,expand=1)
        self.student_table.bind("<ButtonRelease>",self.get_cursor)

        self.fetch_data()


    #======================function declaration
    
    def add_data(self):
        if self.var_dep.get()=="select Department" or self.var_stdname.get()=="" or self.var_stid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Satya1369@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("insert into student values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(

                                                                                          self.var_dep.get(),
                                                                                          self.var_stream.get(),
                                                                                          self.var_year.get(),
                                                                                          self.var_semster.get(),
                                                                                          self.var_stid.get(),
                                                                                          self.var_stdname.get(),
                                                                                          self.var_div.get(),
                                                                                          self.var_roll.get(),
                                                                                          self.var_gender.get(),
                                                                                          self.var_dob.get(),
                                                                                          self.var_email.get(),
                                                                                          self.var_phone.get(),
                                                                                          self.var_address.get(),
                                                                                          self.var_teacher.get(),
                                                                                          self.var_radio1.get()


                 
                                                                                        ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("success","student details has been added succesfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)

                
            



    #==========fetch data
    def fetch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="Satya1369@",database="face_recognizer")
        my_cursor=conn.cursor()
        my_cursor.execute("select * from student")
        data=my_cursor.fetchall()

        if len(data)!=0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("",END,values=i)

            conn.commit()
        conn.close()

    #=================get cursor
    def get_cursor(self,event=""):
        cursor_focus=self.student_table.focus()
        content=self.student_table.item(cursor_focus)
        data=content["values"]

        self.var_dep.set(data[0]), 
        self.var_stream.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semster.set(data[3]),
        self.var_stid.set(data[4]),
        self.var_stdname.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]), 
        self.var_radio1.set(data[14])  

    #================updtae fn
    def update_data(self):
        if self.var_dep.get()=="select Department" or self.var_stdname.get()=="" or self.var_stid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                Upadate=messagebox.askyesno("Update","Do u want to update this student details",parent=self.root)
                if Upadate>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Satya1369@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update student set Dep=%s,Stream=%s,Year=%s,Semster=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where Student_id=%s",(

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_stream.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semster.get(),
                                                                                                                                                                            self.var_stdname.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_stid.get(),                                                        

                                                                                                                                                                            ))
                else:
                    if not Upadate:
                        return
                messagebox.showinfo("success","student details updted",parent=self.root)  
                conn.commit()
                self.fetch_data()
                conn.close()
            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #===========delete fn
    def delete_data(self):
        if self.var_stid.get()=="":
            messagebox.showerror("Error","Student id must be required",parent=self.root)

        else:
            try:
                delete=messagebox.askyesno("Student delete page","Do u wan",parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host="localhost",username="root",password="Satya1369@",database="face_recognizer")
                    my_cursor=conn.cursor()
                    sql="delete from student where Student_id=%s"
                    val=(self.var_stid.get(),)
                    my_cursor.execute(sql,val)
                else:
                    if not delete:
                        return
                
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete","Suceesfully deleted",parent=self.root)


            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)

    #=========reset data
    def reset_data(self):
        self.var_dep.set("Select Department")
        self.var_stream.set("Select Stream")
        self.var_year.set("Select Year")
        self.var_semster.set("Select Semster")
        self.var_stid.set("")
        self.var_stdname.set("")
        self.var_div.set("Select Division")
        self.var_roll.set("")
        self.var_gender.set("f")
        self.var_dob.set("")
        self.var_email.set("")
        self.var_phone.set("")
        self.var_address.set("")
        self.var_teacher.set("")
        self.var_radio1.set("")


    #===========generate data set ot take photo samples
    def generate_dataset(self):
        if self.var_dep.get()=="select Department" or self.var_stdname.get()=="" or self.var_stid.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        else:
            try:
                conn=mysql.connector.connect(host="localhost",username="root",password="Satya1369@",database="face_recognizer")
                my_cursor=conn.cursor()
                my_cursor.execute("select * from student")
                myresult=my_cursor.fetchall()
                id=0
                for x in myresult:
                    id+=1
                my_cursor.execute("update student set Dep=%s,Stream=%s,Year=%s,Semster=%s,Name=%s,Division=%s,Roll=%s,Gender=%s,DOB=%s,Email=%s,Phone=%s,Address=%s,Teacher=%s,PhotoSampleStatus=%s where Student_id=%s",(

                                                                                                                                                                            self.var_dep.get(),
                                                                                                                                                                            self.var_stream.get(),
                                                                                                                                                                            self.var_year.get(),
                                                                                                                                                                            self.var_semster.get(),
                                                                                                                                                                            self.var_stdname.get(),
                                                                                                                                                                            self.var_div.get(),
                                                                                                                                                                            self.var_roll.get(),
                                                                                                                                                                            self.var_gender.get(),
                                                                                                                                                                            self.var_dob.get(),
                                                                                                                                                                            self.var_email.get(),
                                                                                                                                                                            self.var_phone.get(),
                                                                                                                                                                            self.var_address.get(),
                                                                                                                                                                            self.var_teacher.get(),
                                                                                                                                                                            self.var_radio1.get(),
                                                                                                                                                                            self.var_stid.get()==id+1,                                                 

                                                                                                                                                                            ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()

                #============load predefined data on face frontals from opencv

                face_classifier=cv2.CascadeClassifier("D:\Face_recognition_system\haarcascade_frontalface_default.xml")

                def face_cropped(img):
                    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
                    faces=face_classifier.detectMultiScale(gray,1.3,5)
                    #scaling factor=1.3
                    #minimum neighbor=5


                    for (x,y,w,h) in faces:
                        face_cropped=img[y:y+h,x:x+w]
                        return face_cropped
                    
                cap=cv2.VideoCapture(0)
                img_id=0
                while True:
                    ret,my_frame=cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face=cv2.resize(face_cropped(my_frame),(450,450))
                        face=cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                        file_name_path="data/user."+str(id)+"."+str(img_id)+".jpg"
                        cv2.imwrite(file_name_path,face)
                        cv2.putText(face,str(img_id),(50,50),cv2.FONT_HERSHEY_COMPLEX,2,(0,255,0),2)
                        cv2.imshow("Cropped face",face)

                    if cv2.waitKey(1)==13 or int(img_id)==100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result","Generating data sets completeed")

            except Exception as es:
                messagebox.showerror("Error",f"Due To:{str(es)}",parent=self.root)  










 



if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop()