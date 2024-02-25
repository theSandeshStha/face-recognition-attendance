import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from tkinter import messagebox
import mysql.connector
import cv2
import numpy as np



class Train:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Train Data")

        title_lbl = Label(self.root, text = "Train Dataset", font = ("Montserrat", 35, "bold"), bg = "white", fg="black")
        title_lbl.place(x = 0, y = 0, width = 1530, height = 45)

        # img_top = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        # img_top = img_top.resize((1530, 325), Image.ANTIALIAS)
        # self.photoimg_top = ImageTk.PhotoImage(img_top)

        # f_lbl = Label(self.root, image = self.photoimg_top)
        # f_lbl.place(x = 0, y = 55, width = 1530, height = 325)

        # =============== Button ==================
        b1_1 = Button(self.root, command = self.train_classifier, text = "Train Data", cursor = "hand2", font = ("Montserrat", 15, "bold"))
        b1_1.place(x = 0, y = 380, width = 1530, height = 60)

        img_bottom = Image.open(os.path.expanduser("~/Desktop/project/Attendance/Images/college_logo.png"))
        img_bottom = img_bottom.resize((1530, 325), Image.ANTIALIAS)
        self.photoimg_bottom = ImageTk.PhotoImage(img_bottom)

        f_lbl = Label(self.root, image = self.photoimg_bottom)
        f_lbl.place(x = 0, y = 440, width = 1530, height = 325)

    def train_classifier(self):
        data_dir = ("data")
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]

        faces = []
        ids = []

        for image in path:
            img = Image.open(image).convert('L')   # Converting into Grayscale image
            imageNp = np.array(img, 'uint8')
            id = int(os.path.split(image)[1].split('.')[1])

            faces.append(imageNp)
            ids.append(id)
            cv2.imshow("Training...", imageNp)
            cv2.waitKey(1) == 13

        ids = np.array(ids)


        # ===================== Train the classifier ====================

        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.train(faces, ids)
        clf.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets Complete!", parent = self.root)







if __name__ == "__main__":
    root = tk.Tk()
    obj = Train(root)
    root.mainloop()