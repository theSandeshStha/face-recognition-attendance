import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2

class Student:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Student Details")



        # ======================= Variables for database =======================
        self.var_department = StringVar()
        self.var_level = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_std_id = StringVar()
        self.var_std_name = StringVar()
        self.var_div = StringVar()
        self.var_roll = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_teacher = StringVar()



        # First Image
        img = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img = img.resize((500,100), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 500, height = 100)

        #Second Image
        img1 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img1 = img1.resize((500,100), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x = 500, y = 0, width = 500, height = 100)
        
        #Third Image
        img2 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img2 = img2.resize((500,100), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl = Label(self.root, image = self.photoimg2)
        f_lbl.place(x = 1000, y = 0, width = 500, height = 100)


        #Background Image
        img3 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/purple.jpeg"))
        img3 = img3.resize((1530,710), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image = self.photoimg3)
        bg_img.place(x = 0, y = 130, width = 1530, height = 710)

        title_lbl = Label(bg_img, text = "Student Management", font = ("Montserrat", 35, "bold"), bg = "white", fg="black")
        title_lbl.place(x = 0, y = 0, width = 1530, height = 45)

        # Frame-------
        # Main Frame / Background division
        main_frame = Frame(bg_img, bd = 2, bg = "lightgrey")
        main_frame.place(x = 20, y = 55, width = 1500, height = 600)

        # Left division
        Left_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = "Student Details", font = ("Montserrat", 12, "bold"))
        Left_frame.place(x = 10, y = 10, width = 760, height = 580)

        img_left = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img_left = img_left.resize((720,130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image = self.photoimg_left)
        f_lbl.place(x = 5, y = 0, width = 720, height = 130)

        # Course Information
        current_course_frame = LabelFrame(Left_frame, bd = 2, relief = RIDGE, text = "Course Information", font = ("Montserrat", 12, "bold"))
        current_course_frame.place(x = 5, y = 135, width = 720, height = 150)

        # Department
        dep_label = Label(current_course_frame, text = "Department", font = ("Montserrat", 12, "bold"))
        dep_label.grid(row = 0, column = 0, padx = 10, sticky = W)

        # Dropdown selector
        dep_combo = ttk.Combobox(current_course_frame, textvariable = self.var_department, font = ("Montserrat", 12, "bold"), width = 17, state = "readonly")
        dep_combo['values'] = ("--Select Department--", "CSIT (Computer Science)", "CA (Computer Application)", "IM (Information Management)")
        dep_combo.current(0)
        dep_combo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        # level
        level_label = Label(current_course_frame, text = "Level", font = ("Montserrat", 12, "bold"))
        level_label.grid(row = 0, column = 2, padx = 10, sticky = W)

        # Dropdown selector
        level_combo = ttk.Combobox(current_course_frame, textvariable = self.var_level, font = ("Montserrat", 12, "bold"), width = 17, state = "readonly")
        level_combo['values'] = ("--Select Level--", "Bachelors", "Masters", "Ph.D")
        level_combo.current(0)
        level_combo.grid(row = 0, column = 3, padx = 2, pady = 10, sticky = W)

        # Year
        year_label = Label(current_course_frame, text = "Year", font = ("Montserrat", 12, "bold"))
        year_label.grid(row = 1, column = 0, padx = 10, sticky = W)

        # Dropdown selector
        year_combo = ttk.Combobox(current_course_frame, textvariable = self.var_year, font = ("Montserrat", 12, "bold"), width = 17, state = "readonly")
        year_combo['values'] = ("--Select Year--", "First / 1st", "Second / 2nd", "Third / 3rd", "Fourth / 4th")
        year_combo.current(0)
        year_combo.grid(row = 1, column = 1, padx = 2, pady = 10, sticky = W)

        # Semester
        semester_label = Label(current_course_frame, text = "Semester", font = ("Montserrat", 12, "bold"))
        semester_label.grid(row = 1, column = 2, padx = 10, sticky = W)

        # Dropdown selector
        semester_combo = ttk.Combobox(current_course_frame, textvariable = self.var_semester, font = ("Montserrat", 12, "bold"), width = 17, state = "readonly")
        semester_combo['values'] = ("--Select Semester--", "First / 1st", "Second / 2nd", "Third / 3rd", "Fourth / 4th", "Fifth / 5th", "Sixth / 6th", "Seventh / 7th", "Eight / 8th")
        semester_combo.current(0)
        semester_combo.grid(row = 1, column = 3, padx = 2, pady = 10, sticky = W)

        # Class Student Information
        class_Student_frame = LabelFrame(Left_frame, bd = 2, relief = RIDGE, text = "Student Information", font = ("Montserrat", 12, "bold"))
        class_Student_frame.place(x = 5, y = 250, width = 720, height = 300)

        # Student ID
        studentId_label = Label(class_Student_frame, text = "Student ID:", font = ("Montserrat", 12, "bold"))
        studentId_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

        # Input Field
        studentID_entry = ttk.Entry(class_Student_frame, textvariable = self.var_std_id, width = 20, font = ("Montserrat", 12, "bold"))
        studentID_entry.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

        # Student Name
        studentName_label = Label(class_Student_frame, text = "Student Name:", font = ("Montserrat", 12, "bold"))
        studentName_label.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)

        # Input Field
        studentName_entry = ttk.Entry(class_Student_frame, textvariable = self.var_std_name, width = 20, font = ("Montserrat", 12, "bold"))
        studentName_entry.grid(row = 0, column = 3, padx = 10, pady = 5, sticky = W)

        # Class Division
        class_div_label = Label(class_Student_frame, text = "Class Division:", font = ("Montserrat", 12, "bold"))
        class_div_label.grid(row = 1, column = 0, padx = 10, pady = 5, sticky = W)

        # Input Field
        # class_div_entry = ttk.Entry(class_Student_frame, textvariable = self.var_div, width = 20, font = ("Montserrat", 12, "bold"))
        # class_div_entry.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

        division_combo = ttk.Combobox(class_Student_frame, textvariable = self.var_div, font = ("Montserrat", 12, "bold"), width = 19, state = "readonly")
        division_combo['values'] = ("--Select Division--", "A", "B", "C")
        division_combo.current(0)
        division_combo.grid(row = 1, column = 1, padx = 10, pady = 5, sticky = W)

        # Roll Number
        roll_no_label = Label(class_Student_frame, text = "Roll No:", font = ("Montserrat", 12, "bold"))
        roll_no_label.grid(row = 1, column = 2, padx = 10, pady = 5, sticky = W)

        # Input Field
        roll_no_entry = ttk.Entry(class_Student_frame, textvariable = self.var_roll, width = 20, font = ("Montserrat", 12, "bold"))
        roll_no_entry.grid(row = 1, column = 3, padx = 10, pady = 5, sticky = W)

        # Gender
        gender_label = Label(class_Student_frame, text = "Gender:", font = ("Montserrat", 12, "bold"))
        gender_label.grid(row = 2, column = 0, padx = 10, pady = 5, sticky = W)

        gender_combo = ttk.Combobox(class_Student_frame, textvariable = self.var_gender, font = ("Montserrat", 12, "bold"), width = 19, state = "readonly")
        gender_combo['values'] = ("--Select Gender--", "Male", "Female", "Other")
        gender_combo.current(0)
        gender_combo.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

        # Input Field
        # gender_entry = ttk.Entry(class_Student_frame, textvariable = self.var_gender, width = 20, font = ("Montserrat", 12, "bold"))
        # gender_entry.grid(row = 2, column = 1, padx = 10, pady = 5, sticky = W)

        # DOB
        dob_label = Label(class_Student_frame, text = "DOB:", font = ("Montserrat", 12, "bold"))
        dob_label.grid(row = 2, column = 2, padx = 10, pady = 5, sticky = W)

        # Input Field
        dob_entry = ttk.Entry(class_Student_frame, textvariable = self.var_dob, width = 20, font = ("Montserrat", 12, "bold"))
        dob_entry.grid(row = 2, column = 3, padx = 10, pady = 5, sticky = W)

        # Email
        email_label = Label(class_Student_frame, text = "Email:", font = ("Montserrat", 12, "bold"))
        email_label.grid(row = 3, column = 0, padx = 10, pady = 5, sticky = W)

        # Input Field
        email_entry = ttk.Entry(class_Student_frame, textvariable = self.var_email, width = 20, font = ("Montserrat", 12, "bold"))
        email_entry.grid(row = 3, column = 1, padx = 10, pady = 5, sticky = W)

        # Phone Number
        phone_no_label = Label(class_Student_frame, text = "Phone No:", font = ("Montserrat", 12, "bold"))
        phone_no_label.grid(row = 3, column = 2, padx = 10, pady = 5, sticky = W)

        # Input Field
        phone_no_entry = ttk.Entry(class_Student_frame, textvariable = self.var_phone, width = 20, font = ("Montserrat", 12, "bold"))
        phone_no_entry.grid(row = 3, column = 3, padx = 10, pady = 5, sticky = W)

        # Address
        address_label = Label(class_Student_frame, text = "Address:", font = ("Montserrat", 12, "bold"))
        address_label.grid(row = 4, column = 0, padx = 10, pady = 5, sticky = W)

        # Input Field
        address_entry = ttk.Entry(class_Student_frame, textvariable = self.var_address, width = 20, font = ("Montserrat", 12, "bold"))
        address_entry.grid(row = 4, column = 1, padx = 10, pady = 5, sticky = W)

        # Teacher Name
        teacher_label = Label(class_Student_frame, text = "Teacher's Name:", font = ("Montserrat", 12, "bold"))
        teacher_label.grid(row = 4, column = 2, padx = 10, pady = 5, sticky = W)

        # Input Field
        teacher_entry = ttk.Entry(class_Student_frame, textvariable = self.var_teacher, width = 20, font = ("Montserrat", 12, "bold"))
        teacher_entry.grid(row = 4, column = 3, padx = 10, pady = 5, sticky = W)

        # Radio Buttons for image input
        self.var_radio1 = StringVar()
        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable = self.var_radio1, text = "Take photo sample", value = "Yes")
        radiobtn1.grid( row = 6, column = 0 )

        radiobtn1 = ttk.Radiobutton(class_Student_frame, variable = self.var_radio1, text = "No photo sample", value = "No")
        radiobtn1.grid( row = 6, column = 1 )

        # Button Frame
        btn_frame = Frame(class_Student_frame, bd = 2, relief = RIDGE)
        btn_frame.place( x = 0, y = 200, width = 715, height = 35)

        save_btn = Button(btn_frame, text = "Save", command = self.add_data, width = 15, font = ("Montserrat", 12, "bold"))
        save_btn.grid( row = 0, column = 0 )

        update_btn = Button(btn_frame, text = "Update", command = self.update_data, width = 15, font = ("Montserrat", 12, "bold"))
        update_btn.grid( row = 0, column = 1 )

        delete_btn = Button(btn_frame, text = "Delete", command = self.delete_data, width = 15, font = ("Montserrat", 12, "bold"))
        delete_btn.grid( row = 0, column = 2 )

        reset_btn = Button(btn_frame, text = "Reset", command = self.reset_data, width = 15, font = ("Montserrat", 12, "bold"))
        reset_btn.grid( row = 0, column = 3 )

        btn_frame2 = Frame(class_Student_frame, bd = 2, relief = RIDGE)
        btn_frame2.place( x = 0, y = 235, width = 715, height = 35)

        take_photo_btn = Button(btn_frame2, command = self.generate_dataset, text = "Take Photo Sample", width = 35, font = ("Montserrat", 12, "bold"))
        take_photo_btn.grid( row = 0, column = 0 )

        update_photo_btn = Button(btn_frame2, text = "Update Photo Sample", width = 35, font = ("Montserrat", 12, "bold"))
        update_photo_btn.grid( row = 0, column = 1 )



        # Right division
        Right_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = "Student Details", font = ("Montserrat", 12, "bold"))
        Right_frame.place(x = 780, y = 10, width = 670, height = 580)

        img_right = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img_right = img_right.resize((720,130), Image.ANTIALIAS)
        self.photoimg_right = ImageTk.PhotoImage(img_right)

        f_lbl = Label(Right_frame, image = self.photoimg_right)
        f_lbl.place(x = 5, y = 0, width = 650, height = 130)

        # -------------- THE SEARCHING SYSTEM -------------- 

        search_frame = LabelFrame(Right_frame, text = "Search System", bd = 2, relief = RIDGE)
        search_frame.place( x = 5, y = 135, width = 650, height = 70 )

        search_label = Label(search_frame, text = "Search By:", font = ("Montserrat", 12, "bold"))
        search_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)
        self.var_searchTX=StringVar()

        search_combo = ttk.Combobox(search_frame, font = ("Montserrat", 12, "bold"), width = 15, state = "readonly")
        search_combo['values'] = ("--Select Attribute--", "Roll_No", "Phone_No")
        search_combo.current(0)
        search_combo.grid(row = 0, column = 1, padx = 2, pady = 10, sticky = W)

        self.var_search=StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.var_search, width = 15, font = ("Montserrat", 12, "bold"))
        search_entry.grid(row = 0, column = 2, padx = 10, pady = 5, sticky = W)

        search_btn = Button(search_frame, command = self.search_data, text = "Search", width = 8, font = ("Montserrat", 12, "bold"))
        search_btn.grid( row = 0, column = 3, padx = 2)

        showAll_btn = Button(search_frame, command = self.fetch_data, text = "Show All", width = 8, font = ("Montserrat", 12, "bold"))
        showAll_btn.grid( row = 0, column = 4, padx = 2)


        




        # Table Frame
        table_frame = Frame(Right_frame, bd = 2, relief = RIDGE)
        table_frame.place( x = 5, y = 210, width = 650, height = 350 )

        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.student_table = ttk.Treeview(table_frame, column = ("Department", "Level", "Year", "Sem", "ID", "Name", "Div", "Roll No", "Gender", "DOB", "Email", "Phone", "Address", "Teacher", "Photo"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)
        scroll_x.config(command = self.student_table.xview)
        scroll_y.config(command = self.student_table.yview)

        self.student_table.heading("Department", text = "Department")
        self.student_table.heading("Level", text = "Level")
        self.student_table.heading("Year", text = "Year")
        self.student_table.heading("Sem", text = "Semester")
        self.student_table.heading("ID", text = "ID")
        self.student_table.heading("Name", text = "Name")
        self.student_table.heading("Div", text = "Div")
        self.student_table.heading("Roll No", text = "Roll No")
        self.student_table.heading("Gender", text = "Gender")
        self.student_table.heading("DOB", text = "DOB")
        self.student_table.heading("Email", text = "Email")
        self.student_table.heading("Phone", text = "Phone")
        self.student_table.heading("Address", text = "Address")
        self.student_table.heading("Teacher", text = "Teacher")
        self.student_table.heading("Photo", text = "Photo Sample Status")
        self.student_table["show"] = "headings"

        self.student_table.column("Department", width = 100)
        self.student_table.column("Level", width = 100)
        self.student_table.column("Year", width = 100)
        self.student_table.column("Sem", width = 100)
        self.student_table.column("ID", width = 100)
        self.student_table.column("Name", width = 100)
        self.student_table.column("Div", width = 100)
        self.student_table.column("Roll No", width = 100)
        self.student_table.column("Gender", width = 100)
        self.student_table.column("DOB", width = 100)
        self.student_table.column("Email", width = 100)
        self.student_table.column("Phone", width = 100)
        self.student_table.column("Address", width = 100)
        self.student_table.column("Teacher", width = 100)
        self.student_table.column("Photo", width = 150)

        self.student_table.pack(fill = BOTH, expand = 1)

        self.student_table.bind("<ButtonRelease>", self.get_cursor)

        self.fetch_data()


    # ---------------------- Functions ----------------------

    # Database
    def add_data(self):
        if self.var_department.get() == "--Select Department--" or self.var_std_name.get() == "" or self.var_std_id.get() == "": 
            messagebox.showerror("Error","All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect( host = "localhost", username = "root", password = "cheeseball", database = "face-recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into student values(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_department.get(),
                    self.var_level.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_id.get(),
                    self.var_std_name.get(),
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
                messagebox.showinfo("Success", "Student Detaiils have been added sucessfully.", parent = self.root)
            
            except Exception as es:
                messagebox.showerror("Error!", f"Due to :{str(es)}", parent = self.root)


    #-------------------------- Fetching data from database ---------------------------
    def fetch_data(self):
        conn = mysql.connector.connect( host = "localhost", username = "root", password = "cheeseball", database = "face-recognition")
        my_cursor = conn.cursor()
        my_cursor.execute("Select * from student")
        data = my_cursor.fetchall()

        if len(data) != 0:
            self.student_table.delete(*self.student_table.get_children())
            for i in data:
                self.student_table.insert("", END, values = i )
            conn.commit()
        conn.close()



    # ===================== Searching =====================

    def search_data(self):
        if self.var_search.get()=="" or self.var_searchTX.get()=="--Select Attribute--":
            messagebox.showerror("Error","Select search option and don't leave the entry box empty",parent=self.root)
        else:
            if self.var_searchTX.get()=="Roll_No":
                try:
                    conn = mysql.connector.connect(username='root', password='cheeseball',host='localhost',database='face-recognition')
                    my_cursor = conn.cursor()
                    sql = "SELECT * FROM student where Roll='" +str(self.var_search.get()) + "'" 
                    my_cursor.execute(sql)
                    # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                    rows=my_cursor.fetchall()        
                    if len(rows)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in rows:
                            self.student_table.insert("",END,values=i)
                        if rows==None:
                            messagebox.showerror("Error","Data Not Found",parent=self.root)
                            conn.commit()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(username='root', password='cheeseball',host='localhost',database='face-recognition')
                    my_cursor = conn.cursor()
                    sql = "SELECT * FROM student where Phone='" +str(self.var_search.get()) + "'" 
                    my_cursor.execute(sql)
                    # my_cursor.execute("select * from student where Roll_No= " +str(self.var_search.get())+" "+str(self.var_searchTX.get())+"")
                    rows=my_cursor.fetchall()        
                    if len(rows)!=0:
                        self.student_table.delete(*self.student_table.get_children())
                        for i in rows:
                            self.student_table.insert("",END,values=i)
                        if rows==None:
                            messagebox.showerror("Error","Data Not Found",parent=self.root)
                            conn.commit()
                    conn.close()
                except Exception as es:
                    messagebox.showerror("Error",f"Due To :{str(es)}",parent=self.root)




    # -------------------------- Get cursor ------------------------------

    def get_cursor(self, event = ""):
        cursor_focus = self.student_table.focus()
        content = self.student_table.item(cursor_focus)
        data = content["values"]

        self.var_department.set(data[0]),
        self.var_level.set(data[1]),
        self.var_year.set(data[2]),
        self.var_semester.set(data[3]),
        self.var_std_id.set(data[4]),
        self.var_std_name.set(data[5]),
        self.var_div.set(data[6]),
        self.var_roll.set(data[7]),
        self.var_gender.set(data[8]),
        self.var_dob.set(data[9]),
        self.var_email.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_address.set(data[12]),
        self.var_teacher.set(data[13]),
        self.var_radio1.set(data[14])




    # ---------------------------- Update Data -------------------------------

    def update_data(self):
        if self.var_department.get() == "--Select Department--" or self.var_std_name.get() == "" or self.var_std_id.get() == "": 
            messagebox.showerror("Error","All Fields are required", parent = self.root)
        else:
            try:
                Update = messagebox.askyesno("Update", "Are you sure you want to update the details?", parent = self.root)
                if Update > 0:
                    conn = mysql.connector.connect( host = "localhost", username = "root", password = "cheeseball", database = "face-recognition")
                    my_cursor = conn.cursor()
                    my_cursor.execute("update student set Dep=%s, Level=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                    self.var_department.get(),
                    self.var_level.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get()
                    ))
                
                else:
                    if not Update:
                        return
                messagebox.showinfo("Success", "Student details were successfully updated.", parent = self.root)
                conn.commit()
                self.fetch_data()
                conn.close()

            except Exception as es:
                messagebox.showerror("Error!", f"Due to :{str(es)}", parent = self.root)




    # ------------------------- Delete Data ---------------------------

    def delete_data(self):
        if self.var_std_id.get() == "":
            messagebox.showerror("Error!", "Student ID is required!", parent = self.root)
        else:
            try:
                delete = messagebox.askyesno("Delete", "Do you really want to delete?", parent = self.root)
                if delete > 0:
                    conn = mysql.connector.connect( host = "localhost", username = "root", password = "cheeseball", database = "face-recognition")
                    my_cursor = conn.cursor()
                    sql = "delete from student where Student_id=%s"
                    val = (self.var_std_id.get(),)
                    my_cursor.execute(sql, val)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Delete", "Successfully deleted!", parent = self.root)
            except Exception as es:
                messagebox.showerror("Error!", f"Due to :{str(es)}", parent = self.root)




    # ----------------------------- Reset --------------------------------

    def reset_data(self):
        self.var_department.set("--Select Department--"),
        self.var_level.set("--Select Level--"),
        self.var_year.set("--Select Year--"),
        self.var_semester.set("--Select Semester--"),
        self.var_std_id.set(""),
        self.var_std_name.set(""),
        self.var_div.set("A"),
        self.var_roll.set(""),
        self.var_gender.set("Male"),
        self.var_dob.set(""),
        self.var_email.set(""),
        self.var_phone.set(""),
        self.var_address.set(""),
        self.var_teacher.set(""),
        self.var_radio1.set("")


# ============================= Generate dataset and Take photo sample ============================

    def generate_dataset(self):
        if self.var_department.get() == "--Select Department--" or self.var_std_name.get() == "" or self.var_std_id.get() == "": 
                messagebox.showerror("Error","All Fields are required", parent = self.root)
        else:
            try:
                conn = mysql.connector.connect( host = "localhost", username = "root", password = "cheeseball", database = "face-recognition")
                my_cursor = conn.cursor()
                my_cursor.execute("select * from student")
                my_result = my_cursor.fetchall()
                id = 0
                for x in my_result:
                    id+=1
                my_cursor.execute("update student set Dep=%s, Level=%s, Year=%s, Semester=%s, Name=%s, Division=%s, Roll=%s, Gender=%s, Dob=%s, Email=%s, Phone=%s, Address=%s, Teacher=%s, PhotoSample=%s where Student_id=%s", (
                    self.var_department.get(),
                    self.var_level.get(),
                    self.var_year.get(),
                    self.var_semester.get(),
                    self.var_std_name.get(),
                    self.var_div.get(),
                    self.var_roll.get(),
                    self.var_gender.get(),
                    self.var_dob.get(),
                    self.var_email.get(),
                    self.var_phone.get(),
                    self.var_address.get(),
                    self.var_teacher.get(),
                    self.var_radio1.get(),
                    self.var_std_id.get() == id + 1
                        ))
                conn.commit()
                self.fetch_data()
                self.reset_data()
                conn.close()


                # =================== Loading predefined data on frontal face from opencv ===================
                face_classifier = cv2.CascadeClassifier(os.path.expanduser("~/Desktop/project/Attendance/haarcascade_frontalface_default.xml"))
                def face_cropped(img):
                    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # 1.3 is scaling factor
                    # 5 is minimum neighbour
                

                    for(x,y,w,h) in faces:
                        face_cropped = img[y:y+h, x:x+w]
                        return face_cropped
                
                cap = cv2.VideoCapture(0)
                img_id = 0
                while True:
                    ret, my_frame = cap.read()
                    if face_cropped(my_frame) is not None:
                        img_id+=1
                        face = cv2.resize(face_cropped(my_frame), (450, 450))
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)
                        file_name_path = os.path.expanduser("~/Desktop/project/Attendance/data/user.") + str(id) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 100:
                        break
                cap.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Result", "Generation of dataset complete!")
            except Exception as es:
                messagebox.showerror("Error",f"Due to: {str(es)}",parent=self.root) 




if __name__ == "__main__":
    root = tk.Tk()
    obj = Student(root)
    root.mainloop()