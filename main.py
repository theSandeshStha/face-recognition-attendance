import tkinter as tk
from tkinter import *
from tkinter import ttk
from time import strftime
from datetime import datetime
from PIL import Image, ImageTk
import os
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from mail import Mail
from tkinter import messagebox

class Face_Recognition_System:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # First Image
        img = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img = img.resize((500,100), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 500, height = 100)

        #Second Image
        img1 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img1 = img1.resize((500,100), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x = 500, y = 0, width = 500, height = 100)
        
        #Third Image
        img2 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img2 = img2.resize((500,100), Image.Resampling.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x = 1000, y = 0, width = 500, height = 100)


        #Background Image
        img3 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/purple.jpeg"))
        img3 = img3.resize((1530,710), Image.Resampling.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)

        title_lbl = Label(bg_img, text = "Facial Recognition Attendance System", font = ("Montserrat", 35, "bold"))
        title_lbl.place(x = 0, y = 0, width = 1530, height = 45)


        #Student Button
        img4 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/StudentInfo.jpeg"))
        img4 = img4.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, command = self.student_details, image = self.photoimg4, cursor = "hand2")
        b1.place(x = 200, y = 100, width = 220, height = 220)

        b1_1 = Button(bg_img, command = self.student_details, text = "Student Details", cursor = "hand2", font = ("Montserrat", 15, "bold"))
        b1_1.place(x = 200, y = 300, width = 220, height = 40)

        #Detect Face Button
        img5 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/detect_face.jpeg"))
        img5 = img5.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b1 = Button(bg_img, command = self.face_data, image = self.photoimg5, cursor = "hand2")
        b1.place(x = 500, y = 100, width = 220, height = 220)

        b1_1 = Button(bg_img, command = self.face_data, text = "Face Detector", cursor = "hand2", font = ("Montserrat", 15, "bold"))
        b1_1.place(x = 500, y = 300, width = 220, height = 40)

        #Attendance Button
        img6 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/attendance.jpeg"))
        img6 = img6.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b1 = Button(bg_img, command = self.attendance_data, image = self.photoimg6, cursor = "hand2")
        b1.place(x = 800, y = 100, width = 220, height = 220)

        b1_1 = Button(bg_img, command = self.attendance_data, text = "Attendance", cursor = "hand2", font = ("Montserrat", 15, "bold"))
        b1_1.place(x = 800, y = 300, width = 220, height = 40)

        #Train Button
        img7 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/train.jpeg"))
        img7 = img7.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b1 = Button(bg_img, image = self.photoimg7, cursor = "hand2", command = self.train_data)
        b1.place(x = 200, y = 400, width = 220, height = 220)

        b1_1 = Button(bg_img, text = "Train Face", cursor = "hand2", command = self.train_data, font = ("Montserrat", 15, "bold"))
        b1_1.place(x = 200, y = 600, width = 220, height = 40)

        #Send Attendance Button
        img8 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/mail.jpeg"))
        img8 = img8.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b1 = Button(bg_img, command = self.send_attendance, image = self.photoimg8, cursor = "hand2")
        b1.place(x = 500, y = 400, width = 220, height = 220)

        b1_1 = Button(bg_img, command = self.send_attendance, text = "Mail Attendance", cursor = "hand2", font = ("Montserrat", 15, "bold"))
        b1_1.place(x = 500, y = 600, width = 220, height = 40)

        #Exit Button
        img9 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/exit.jpeg"))
        img9 = img9.resize((220,220), Image.Resampling.LANCZOS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b1 = Button(bg_img, command = self.iExit, image = self.photoimg9, cursor = "hand2")
        b1.place(x = 800, y = 400, width = 220, height = 220)

        b1_1 = Button(bg_img, command = self.iExit, text = "Exit", cursor = "hand2", font = ("Montserrat", 15, "bold"))
        b1_1.place(x = 800, y = 600, width = 220, height = 40)


        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)

        lbl = Label(title_lbl, font = ('times new roman', 14, 'bold'), background = 'white', foreground = 'blue')
        lbl.place(x = 0, y = 0, width = 110, height = 50)
        time()

    def iExit(self):
        self.iExit = tk.messagebox.askyesno("Exit", "Are you sure you want to exit?", parent = self.root)
        if self.iExit > 0:
            self.root.destroy()
        else:
            return
    

    

    # --------------------- Button Functions ---------------------
    def student_details(self):
        self.new_window = Toplevel(self.root)
        self.app = Student(self.new_window)


    def train_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Train(self.new_window)


    def face_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Face_Recognition(self.new_window)

    def attendance_data(self):
        self.new_window = Toplevel(self.root)
        self.app = Attendance(self.new_window)

    def send_attendance(self):
        self.new_window = Toplevel(self.root)
        self.app = Mail(self.new_window)



# Creating a window
if __name__ == "__main__":
    root = tk.Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()


