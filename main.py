from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
import os
import tkinter
from student_details import Student
from train import Train
from face_recognition import Face_Recognition
from attendance_details import Attendance
from developer import Developer
from help import Help

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")
        
        #centre img
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
        title_lbl=Label(b_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1530,height=45)

        #student button
        img1=Image.open(r"images\face.jpg")
        img1=img1.resize((1530,710),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        b1=Button(b_img,image=self.photoimg1,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_1=Button(b_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b1_1.place(x=200,y=300,width=220,height=40)

        #Detect Face button
        img2=Image.open(r"images\face.jpg")
        img2=img2.resize((1530,710),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        b2=Button(b_img,image=self.photoimg1,cursor="hand2",command=self.face_data)
        b2.place(x=500,y=100,width=220,height=220)

        b2_1=Button(b_img,text="Face detector",cursor="hand2",command=self.face_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b2_1.place(x=500,y=300,width=220,height=40)


        #Attendance button
        img3=Image.open(r"images\face.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        b3=Button(b_img,image=self.photoimg1,cursor="hand2",command=self.attendance_data)
        b3.place(x=800,y=100,width=220,height=220)

        b3_1=Button(b_img,text="Attendance",cursor="hand2",command=self.attendance_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b3_1.place(x=800,y=300,width=220,height=40)


        #Help button
        img4=Image.open(r"images\face.jpg")
        img4=img4.resize((1530,710),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b4=Button(b_img,image=self.photoimg1,cursor="hand2",command=self.help_data)
        b4.place(x=1100,y=100,width=220,height=220)

        b4_1=Button(b_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b4_1.place(x=1100,y=300,width=220,height=40)

        #Train button
        img5=Image.open(r"images\face.jpg")
        img5=img5.resize((1530,710),Image.ANTIALIAS)
        self.photoimg5=ImageTk.PhotoImage(img5)

        b5=Button(b_img,image=self.photoimg1,cursor="hand2",command=self.train_data)
        b5.place(x=200,y=380,width=220,height=220)

        b5_1=Button(b_img,text="Train Data",cursor="hand2",command=self.train_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b5_1.place(x=200,y=580,width=220,height=40)

        #Photos button
        img6=Image.open(r"images\face.jpg")
        img6=img6.resize((1530,710),Image.ANTIALIAS)
        self.photoimg6=ImageTk.PhotoImage(img6)

        b6=Button(b_img,image=self.photoimg1,cursor="hand2",command=self.open_img)
        b6.place(x=500,y=380,width=220,height=220)

        b6_1=Button(b_img,text="Photos",cursor="hand2",command=self.open_img,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b6_1.place(x=500,y=580,width=220,height=40)

        #Developer button
        img7=Image.open(r"images\face.jpg")
        img7=img7.resize((1530,710),Image.ANTIALIAS)
        self.photoimg7=ImageTk.PhotoImage(img7)

        b7=Button(b_img,image=self.photoimg1,cursor="hand2",command=self.developer_data)
        b7.place(x=800,y=380,width=220,height=220)

        b7_1=Button(b_img,text="Developer",cursor="hand2",command=self.developer_data,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b7_1.place(x=800,y=580,width=220,height=40)


        #Exit button
        img8=Image.open(r"images\face.jpg")
        img8=img5.resize((1530,710),Image.ANTIALIAS)
        self.photoimg8=ImageTk.PhotoImage(img8)

        b8=Button(b_img,image=self.photoimg1,cursor="hand2",command=self.iExit)
        b8.place(x=1100,y=380,width=220,height=220)

        b8_1=Button(b_img,text="Exit",cursor="hand2",command=self.iExit,font=("times new roman",15,"bold"),bg="darkblue",fg="white")
        b8_1.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data") 

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesno("Face recognition","are u sure exit this project",parent=self.root)
        if self.iExit >0:
            self.root.destroy()
        else:
            return







    #==========functions button

    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)


    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)

    def developer_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()