import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Details")


         # First Image
        img = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img = img.resize((800,200), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 800, height = 200)

        #Second Image
        img1 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img1 = img1.resize((800,200), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x = 800, y = 0, width = 800, height = 200)

        title_lbl = Label(self.root, text = "Student Management", font = ("Montserrat", 35, "bold"), bg = "white", fg="black")
        title_lbl.place(x = 0, y = 201, width = 1530, height = 45)

        # Frame-------
        # Main Frame / Background division
        main_frame = Frame(self.root, bd = 2, bg = "lightgrey")
        main_frame.place(x = 10, y = 248, width = 1480, height = 600)

        # Left division
        Left_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = "Attendance Details", font = ("Montserrat", 12, "bold"))
        Left_frame.place(x = 10, y = 10, width = 760, height = 580)

        img_left = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img_left = img_left.resize((720,130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image = self.photoimg_left)
        f_lbl.place(x = 5, y = 0, width = 720, height = 130)

        # Right division
        Right_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = "Attendance Details", font = ("Montserrat", 12, "bold"))
        Right_frame.place(x = 780, y = 10, width = 670, height = 580)

        # Left Inner Frame
        left_inside_frame = Frame(Left_frame, bd = 2, relief = RIDGE, bg = "lightgrey")
        left_inside_frame.place(x = 0, y = 135, width = 725, height = 400)


        # ============== Labels and Entry Fields ===================

        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text = "Attendance ID:", font = ("Montserrat", 12, "bold"))
        attendanceId_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

        # Input Field
        attendanceID_entry = ttk.Entry(left_inside_frame,  width = 20, font = ("Montserrat", 12, "bold"))
        attendanceID_entry.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)


        



if __name__ == "__main__":
    root = tk.Tk()
    obj = Attendance(root)
    root.mainloop()