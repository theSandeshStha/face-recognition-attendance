import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2
import csv
from tkinter import filedialog


mydata =[]

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Attendance Details")



        # =============== Variables ================

        self.var_attend_id = StringVar()
        self.var_attend_roll = StringVar()
        self.var_attend_name = StringVar()
        self.var_attend_dep = StringVar()
        self.var_attend_time = StringVar()
        self.var_attend_date = StringVar()
        self.var_attend_attendance = StringVar()


         # First Image
        img = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img = img.resize((800,200), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image = self.photoimg)
        f_lbl.place(x = 0, y = 0, width = 800, height = 200)

        #Second Image
        img1 = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img1 = img1.resize((800,200), Image.Resampling.LANCZOS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl = Label(self.root, image = self.photoimg1)
        f_lbl.place(x = 800, y = 0, width = 800, height = 200)

        title_lbl = Label(self.root, text = "Attendance Management", font = ("Montserrat", 35, "bold"), bg = "white", fg="black")
        title_lbl.place(x = 0, y = 201, width = 1530, height = 45)

        # Frame-------
        # Main Frame / Background division
        main_frame = Frame(self.root, bd = 2, bg = "lightgrey")
        main_frame.place(x = 10, y = 248, width = 1480, height = 600)

        # Left division
        Left_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = "Attendance Details", font = ("Montserrat", 12, "bold"))
        Left_frame.place(x = 10, y = 10, width = 760, height = 580)

        img_left = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img_left = img_left.resize((720,130), Image.Resampling.LANCZOS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)

        f_lbl = Label(Left_frame, image = self.photoimg_left)
        f_lbl.place(x = 5, y = 0, width = 720, height = 130)


        # Left Inner Frame
        left_inside_frame = Frame(Left_frame, bd = 2, relief = RIDGE, bg = "lightgrey")
        left_inside_frame.place(x = 0, y = 135, width = 725, height = 370)


        # ============== Labels and Entry Fields ===================

        # Attendance ID
        attendanceId_label = Label(left_inside_frame, text = "Attendance ID:", font = ("Montserrat", 12, "bold"))
        attendanceId_label.grid(row = 0, column = 0, padx = 10, pady = 5, sticky = W)

        # Input Field
        attendanceID_entry = ttk.Entry(left_inside_frame, textvariable = self.var_attend_id, width = 20, font = ("Montserrat", 12, "bold"))
        attendanceID_entry.grid(row = 0, column = 1, padx = 10, pady = 5, sticky = W)

        # Roll
        rollLabel = Label(left_inside_frame, text = "Roll.No: ", bg = "white", font = "comicsans 11 bold")
        rollLabel.grid(row = 0, column = 2, padx = 4, pady = 8)

        atten_roll = ttk.Entry(left_inside_frame, textvariable = self.var_attend_roll, width = 22, font = "comicsans 11 bold")
        atten_roll.grid(row = 0, column = 3, pady = 8)

        # Name
        nameLabel = Label(left_inside_frame, text = "Name: ", bg = "white", font = "comicsans 11 bold")
        nameLabel.grid(row = 1, column = 0)

        atten_name = ttk.Entry(left_inside_frame, textvariable = self.var_attend_name, width = 22, font = "comicsans 11 bold")
        atten_name.grid(row = 1, column = 1, pady = 8)

        # Department
        depLabel = Label(left_inside_frame, text = "Department: ", bg = "white", font = "comicsans 11 bold")
        depLabel.grid(row = 1, column = 2)

        atten_dep = ttk.Entry(left_inside_frame, textvariable = self.var_attend_dep, width = 22, font = "comicsans 11 bold")
        atten_dep.grid(row = 1, column = 3, pady = 8)

        # Time
        timeLabel = Label(left_inside_frame, text = "Time: ", bg = "white", font = "comicsans 11 bold")
        timeLabel.grid(row = 2, column = 0)

        atten_time = ttk.Entry(left_inside_frame, textvariable = self.var_attend_time, width = 22, font = "comicsans 11 bold")
        atten_time.grid(row = 2, column = 1, pady = 8)

        # Date
        dateLabel = Label(left_inside_frame, text = "Date: ", bg = "white", font = "comicsans 11 bold")
        dateLabel.grid(row = 2, column = 2)

        atten_date = ttk.Entry(left_inside_frame, width = 22, textvariable = self.var_attend_date, font = "comicsans 11 bold")
        atten_date.grid(row = 2, column = 3, pady = 8)

        # Attendance
        attendanceLabel = Label(left_inside_frame, text = "Attendance Status: ", bg = "white", font = "comicsans 11 bold")
        attendanceLabel.grid(row = 3, column = 0)

        self.atten_status = ttk.Combobox(left_inside_frame, textvariable = self.var_attend_attendance, width = 20, font = "comicsans 11 bold", state = "readonly")
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.grid(row = 3, column = 1, pady = 8)
        self.atten_status.current(0)

        # Button Frame
        btn_frame = Frame(left_inside_frame, bd = 2, relief = RIDGE)
        btn_frame.place( x = 0, y = 300, width = 715, height = 35)

        save_btn = Button(btn_frame, text = "Import CSV", command = self.importCsv, width = 15, font = ("Montserrat", 12, "bold"))
        save_btn.grid( row = 0, column = 0 )

        update_btn = Button(btn_frame, text = "Export CSV", command = self.exportCsv, width = 15, font = ("Montserrat", 12, "bold"))
        update_btn.grid( row = 0, column = 1 )

        delete_btn = Button(btn_frame, text = "Update", width = 15, font = ("Montserrat", 12, "bold"))
        delete_btn.grid( row = 0, column = 2 )

        reset_btn = Button(btn_frame, text = "Reset", command = self.reset_data, width = 15, font = ("Montserrat", 12, "bold"))
        reset_btn.grid( row = 0, column = 3 )


        # Right division
        Right_frame = LabelFrame(main_frame, bd = 2, relief = RIDGE, text = "Attendance Details", font = ("Montserrat", 12, "bold"))
        Right_frame.place(x = 750, y = 10, width = 720, height = 580)

        table_frame = Frame(Right_frame, bd = 2, relief = RIDGE)
        table_frame.place( x = 5, y = 5, width = 700, height = 445)

        # ============== Scroll bar table ================

        scroll_x = ttk.Scrollbar(table_frame, orient = HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient = VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, columns = ("id", "roll", "name", "department", "time", "date", "attendance"), xscrollcommand = scroll_x.set, yscrollcommand = scroll_y.set)

        scroll_x.pack(side = BOTTOM, fill = X)
        scroll_y.pack(side = RIGHT, fill = Y)

        scroll_x.config(command = self.AttendanceReportTable.xview)
        scroll_y.config(command = self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text = "Attendance ID")
        self.AttendanceReportTable.heading("roll", text = "Roll No")
        self.AttendanceReportTable.heading("name", text = "Name")
        self.AttendanceReportTable.heading("department", text = "Department")
        self.AttendanceReportTable.heading("time", text = "Time")
        self.AttendanceReportTable.heading("date", text = "Date")
        self.AttendanceReportTable.heading("attendance", text = "Attendance")

        self.AttendanceReportTable["show"] = "headings"
        self.AttendanceReportTable.column("id", width = 100)
        self.AttendanceReportTable.column("roll", width = 100)
        self.AttendanceReportTable.column("name", width = 100)
        self.AttendanceReportTable.column("department", width = 100)
        self.AttendanceReportTable.column("time", width = 100)
        self.AttendanceReportTable.column("date", width = 100)
        self.AttendanceReportTable.column("attendance", width = 100)

        self.AttendanceReportTable.pack(fill = BOTH, expand = 1)

        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

     # ======================= Fetch data ========================
    
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values = i)
            
    # ======================= Import data ========================
    def importCsv(self):
        global mydata
        mydata.clear()
        fln = filedialog.askopenfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV File", "*.csv"), ("All File", "*.*")), parent = self.root)
        with open(fln) as myfile:
            csvread = csv.reader(myfile, delimiter = ",")
            for i in csvread:
                mydata.append(i)
            self.fetchData(mydata)

    # ======================= Export data ========================
            
    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent = self.root)
                return False
            fln = filedialog.asksaveasfilename(initialdir = os.getcwd(), title = "Open CSV", filetypes = (("CSV File", "*.csv"), ("All File", "*.*")), parent = self.root)
            with open(fln, mode = "w", newline = "") as myfile:
                exp_write = csv.writer(myfile, delimiter = ",")
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Exported", "Your data was exported to " + os.path.basename(fln) + " succesfully.")
        except Exception as es:
            messagebox.showerror("Error", f"Due to: {str(es)}", parent = self.root)



    def get_cursor(self, event = ""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content['values']
        self.var_attend_id.set(rows[0])
        self.var_attend_roll.set(rows[1])
        self.var_attend_name.set(rows[2])
        self.var_attend_dep.set(rows[3])
        self.var_attend_time.set(rows[4])
        self.var_attend_date.set(rows[5])
        self.var_attend_attendance.set(rows[6])

    

    def reset_data(self):
        self.var_attend_id.set("")
        self.var_attend_roll.set("")
        self.var_attend_name.set("")
        self.var_attend_dep.set("")
        self.var_attend_time.set("")
        self.var_attend_date.set("")
        self.var_attend_attendance.set("")


if __name__ == "__main__":
    root = tk.Tk()
    obj = Attendance(root)
    root.mainloop()