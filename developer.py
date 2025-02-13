from tkinter import*
from tkinter import ttk
from train import Train
from PIL import Image,ImageTk
from student import Student
from train import Train
from face_recognition import Face_Recognition
from attendance import Attendance
import os

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1366x768+0+0")
        self.root.title("Developer")

        # Background
        self.bg=ImageTk.PhotoImage(Image.open("Images_GUI/dashboard_bg.png"))
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        # Title
        title = Label(self.root,text="Developer",
                     font=("Segoe UI",35,"bold"),fg="white",bg="#1A1A1A")
        title.place(x=0,y=0,relwidth=1,height=70)

        # Main Frame
        main_frame = Frame(self.root,bg="#1A1A1A")
        main_frame.place(x=0,y=70,relwidth=1,relheight=1)

        # Developer Card
        dev_card = Frame(main_frame,bg="#2D2D2D")
        dev_card.place(x=483,y=100,width=400,height=500)

        # Developer Image
        try:
            img = Image.open("Images_GUI/ayaan.png")
        except:
            # Create a default avatar if image doesn't exist
            img = Image.new('RGB', (200, 200), '#2D2D2D')
        img = img.resize((200,200),Image.Resampling.LANCZOS)
        self.photoimg = ImageTk.PhotoImage(img)
        
        img_lbl = Label(dev_card,image=self.photoimg,bg="#2D2D2D")
        img_lbl.place(x=100,y=30,width=200,height=200)

        # Developer Info
        name_lbl = Label(dev_card,text="Ayaan Akkalkot",
                        font=("Segoe UI",20,"bold"),fg="white",bg="#2D2D2D")
        name_lbl.place(x=0,y=250,relwidth=1)

        role_lbl = Label(dev_card,text="Lead Developer",
                        font=("Segoe UI",15),fg="#CCCCCC",bg="#2D2D2D")
        role_lbl.place(x=0,y=290,relwidth=1)

        desc_lbl = Label(dev_card,text="Computer Science Student\nSpecialized in AI & Machine Learning",
                        font=("Segoe UI",12),fg="#CCCCCC",bg="#2D2D2D",justify=CENTER)
        desc_lbl.place(x=0,y=330,relwidth=1)

if __name__ == "__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()