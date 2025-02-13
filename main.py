from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
from developer import Developer
import os
from helpsupport import Helpsupport

class Face_Recognition_System:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Face Recognition Attendance System")

        # Background
        self.bg=ImageTk.PhotoImage(Image.open("Images_GUI/dashboard_bg.png"))
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # Title
        title = Label(self.root,text="Face Recognition Attendance System",
                     font=("Segoe UI",35,"bold"),fg="white",bg="#1A1A1A")
        title.place(x=0,y=0,relwidth=1,height=70)

        # Main Frame
        main_frame = Frame(self.root,bg="#1A1A1A")
        main_frame.place(x=0,y=70,relwidth=1,relheight=1)

        # Cards Frame
        cards_frame = Frame(main_frame,bg="#1A1A1A")
        cards_frame.place(x=50,y=50,width=1266,height=600)

        # Student Card
        student_card = Frame(cards_frame,bg="#2D2D2D")
        student_card.place(x=0,y=0,width=300,height=280)
        
        student_btn = Button(student_card,command=self.student_pannels,
                           text="Student Management",font=("Segoe UI",15,"bold"),
                           fg="white",bg="#007ACC",bd=0,cursor="hand2")
        student_btn.place(x=20,y=200,width=260,height=45)

        # Face Detection Card
        detect_card = Frame(cards_frame,bg="#2D2D2D")
        detect_card.place(x=320,y=0,width=300,height=280)
        
        detect_btn = Button(detect_card,command=self.face_rec,
                          text="Face Recognition",font=("Segoe UI",15,"bold"),
                          fg="white",bg="#007ACC",bd=0,cursor="hand2")
        detect_btn.place(x=20,y=200,width=260,height=45)

        # Attendance Card
        attendance_card = Frame(cards_frame,bg="#2D2D2D")
        attendance_card.place(x=640,y=0,width=300,height=280)
        
        attendance_btn = Button(attendance_card,command=self.attendance_pannel,
                              text="Attendance",font=("Segoe UI",15,"bold"),
                              fg="white",bg="#007ACC",bd=0,cursor="hand2")
        attendance_btn.place(x=20,y=200,width=260,height=45)

        # Train Data Card
        train_card = Frame(cards_frame,bg="#2D2D2D")
        train_card.place(x=960,y=0,width=300,height=280)
        
        train_btn = Button(train_card,command=self.train_pannels,
                          text="Train Data",font=("Segoe UI",15,"bold"),
                          fg="white",bg="#007ACC",bd=0,cursor="hand2")
        train_btn.place(x=20,y=200,width=260,height=45)

        # Photos Card
        photos_card = Frame(cards_frame,bg="#2D2D2D")
        photos_card.place(x=0,y=300,width=300,height=280)
        
        photos_btn = Button(photos_card,command=self.open_img,
                          text="Photos",font=("Segoe UI",15,"bold"),
                          fg="white",bg="#007ACC",bd=0,cursor="hand2")
        photos_btn.place(x=20,y=200,width=260,height=45)

        # Developer Card
        dev_card = Frame(cards_frame,bg="#2D2D2D")
        dev_card.place(x=320,y=300,width=300,height=280)
        
        dev_btn = Button(dev_card,command=self.developr,
                        text="Developer",font=("Segoe UI",15,"bold"),
                        fg="white",bg="#007ACC",bd=0,cursor="hand2")
        dev_btn.place(x=20,y=200,width=260,height=45)

        # Exit Card
        exit_card = Frame(cards_frame,bg="#2D2D2D")
        exit_card.place(x=640,y=300,width=300,height=280)
        
        exit_btn = Button(exit_card,command=self.Close,
                         text="Exit",font=("Segoe UI",15,"bold"),
                         fg="white",bg="#007ACC",bd=0,cursor="hand2")
        exit_btn.place(x=20,y=200,width=260,height=45)

# ==================Funtion for Open Images Folder==================
    def open_img(self):
        os.startfile("dataset")
# ==================Functions Buttons=====================
    def student_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_pannels(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
    
    def face_rec(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)
    
    def attendance_pannel(self):
        self.new_window=Toplevel(self.root)
        self.app=Attendance(self.new_window)
    
    def developr(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)
    
    def helpSupport(self):
        self.new_window=Toplevel(self.root)
        self.app=Helpsupport(self.new_window)

    def Close(self):
        root.destroy()
    
    





if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition_System(root)
    root.mainloop()
