# Import required libraries
from sys import path
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
import mysql.connector
import cv2
import numpy as np
from tkinter import messagebox
from time import strftime
from datetime import datetime


class Face_Recognition:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Panel")
        
        # Add a set to track present students
        self.present_students = set()

        # Setting the header image
        img = Image.open(
            r"C:\Users\Ayaan Akkalkot\Python-FYP-Face-Recognition-Attendence-System\Images_GUI\banner.jpg")
        img = img.resize((1366, 130), Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lb1 = Label(self.root, image=self.photoimg)
        f_lb1.place(x=0, y=0, width=1366, height=130)

        # Background image
        bg1 = Image.open(r"Images_GUI\bg2.jpg")
        bg1 = bg1.resize((1366, 768), Image.Resampling.LANCZOS)
        self.photobg1 = ImageTk.PhotoImage(bg1)
        bg_img = Label(self.root, image=self.photobg1)
        bg_img.place(x=0, y=130, width=1366, height=768)

        # Title label
        title_lb1 = Label(bg_img, text="Welcome to Face Recognition Panel", font=(
            "verdana", 30, "bold"), bg="white", fg="navyblue")
        title_lb1.place(x=0, y=0, width=1366, height=45)

        # Face Detector button
        std_img_btn = Image.open(r"Images_GUI\f_det.jpg")
        std_img_btn = std_img_btn.resize((180, 180), Image.Resampling.LANCZOS)
        self.std_img1 = ImageTk.PhotoImage(std_img_btn)
        std_b1 = Button(bg_img, command=self.face_recog,
                        image=self.std_img1, cursor="hand2")
        std_b1.place(x=600, y=170, width=180, height=180)
        std_b1_1 = Button(bg_img, command=self.face_recog, text="Face Detector", cursor="hand2", font=(
            "tahoma", 15, "bold"), bg="white", fg="navyblue")
        std_b1_1.place(x=600, y=350, width=180, height=45)

    # =====================Attendance===================

    def mark_attendance(self, i, r, n):
        with open("attendance.csv", "r+", newline="\n") as f:
            myDatalist = f.readlines()
            name_list = []
            for line in myDatalist:
                entry = line.split(",")
                name_list.append(entry[0])

            if((i not in name_list)) and ((r not in name_list)) and ((n not in name_list)):
                now = datetime.now()
                d1 = now.strftime("%d/%m/%Y")
                dtString = now.strftime("%H:%M:%S")
                f.writelines(f"\n{i}, {r}, {n}, {dtString}, {d1}, Present")
                # Add to present students set
                self.present_students.add(i)

    def mark_absent_students(self):
        try:
            # Connect to database
            conn = mysql.connector.connect(
                username='root',
                password='ayaan786',
                host='localhost',
                database='face_recognition',
                port=3306
            )
            cursor = conn.cursor()

            # Get all students
            cursor.execute("SELECT Student_ID, Roll_No, Name FROM student")
            all_students = cursor.fetchall()

            now = datetime.now()
            d1 = now.strftime("%d/%m/%Y")
            dtString = now.strftime("%H:%M:%S")

            # Open attendance file in append mode
            with open("attendance.csv", "a", newline="\n") as f:
                # For each student not in present_students, mark as absent
                for student in all_students:
                    student_id = student[0]
                    if student_id not in self.present_students:
                        f.writelines(f"\n{student[0]}, {student[1]}, {student[2]}, {dtString}, {d1}, Absent")

            conn.close()
            messagebox.showinfo("Success", "Attendance marked successfully! Absent students have been recorded.")
        except Exception as e:
            messagebox.showerror("Error", f"Error marking absent students: {str(e)}")

    # ====================Face Recognition==================

    def face_recog(self):
        def draw_boundary(img, classifier, scaleFactor, minNeighbors, color, text, clf):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scaleFactor, minNeighbors)

            coord = []

            for (x, y, w, h) in features:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                id, predict = clf.predict(
                    gray_image[y:y + h, x:x + w])

                confidence = int((100 * (1 - predict / 300)))

                # Database connection
                with mysql.connector.connect(
                    username='root',
                    password='ayaan786',
                    host='localhost',
                    database='face_recognition',
                    port=3306
                ) as conn:
                    cursor = conn.cursor()

                    # Fetch Name
                    cursor.execute(
                        f"SELECT Name FROM student WHERE Student_ID = {id}")
                    n = cursor.fetchone()
                    n = "+".join(n) if n else "Unknown"

                    # Fetch Roll_No
                    cursor.execute(
                        f"SELECT Roll_No FROM student WHERE Student_ID = {id}")
                    r = cursor.fetchone()
                    r = "+".join(r) if r else "Unknown"

                    # Fetch Student_ID
                    cursor.execute(
                        f"SELECT Student_ID FROM student WHERE Student_ID = {id}")
                    i = cursor.fetchone()
                    i = "+".join(i) if i else "Unknown"

                if confidence > 77:
                    cv2.putText(img, f"Student_ID: {i}", (x, y - 80),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Name: {n}", (x, y - 55),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    cv2.putText(img, f"Roll-No: {r}", (x, y - 30),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (64, 15, 223), 2)
                    self.mark_attendance(i, r, n)
                else:
                    cv2.rectangle(
                        img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(img, "Unknown Face", (x, y - 5),
                                cv2.FONT_HERSHEY_COMPLEX, 0.8, (255, 255, 0), 3)

                coord = [x, y, w, h]

            return coord

        def recognize(img, clf, faceCascade):
            coord = draw_boundary(img, faceCascade, 1.1,
                                  10, (255, 25, 255), "Face", clf)
            return img

        # Load face cascade and recognizer
        faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        clf.read("clf.xml")

        # Clear present students set at start of new session
        self.present_students.clear()

        # Start video capture
        videoCap = cv2.VideoCapture(0)

        # Add text to show instructions
        instruction_shown = False

        while True:
            ret, img = videoCap.read()
            if not ret:
                print("Failed to capture image from camera.")
                break

            img = recognize(img, clf, faceCascade)
            
            # Add instruction text
            if not instruction_shown:
                cv2.putText(img, "Press 'Enter' to finish and mark absent students", 
                           (10, 30), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
                instruction_shown = True

            cv2.imshow("Face Detector", img)

            # Exit conditions
            if cv2.waitKey(1) == 13:  # Press 'Enter' to exit
                break
            if cv2.getWindowProperty("Face Detector", cv2.WND_PROP_VISIBLE) < 1:  # Manual close
                break

        videoCap.release()
        cv2.destroyAllWindows()

        # After closing camera, mark absent students
        self.mark_absent_students()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Recognition(root)
    root.mainloop()