from tkinter import *
from PIL import ImageTk, Image


def Admin():t
    root.destroy()
    import LM2_LOGIN_Admin

def Student():
    root.destroy()
    import LM3_LOGIN_Student

root = Tk()
root.geometry("950x550+250+100")
root.maxsize(950, 550)
root.configure(background='Black')
root.title("OUR LIBRARY") 

# Window icon
p1 = PhotoImage(file="icon.PNG")
root.iconphoto(False, p1)

# *** inserting image ***
Symbol = (Image.open("Symbol.PNG"))
resizing_Image = Symbol.resize((300, 300))
New_Symbolimage = ImageTk.PhotoImage(resizing_Image)


# first frame
First_Frame = Frame(root, width=400, height=450, bg="white")
First_Frame.place(x=70, y=50)

Image_Label = Label(First_Frame, image=New_Symbolimage, bd=0)
Image_Label.place(x=50, y=140)

heading1_label = Label(First_Frame, text=" Welcome To Our", font=("arial", 30, "italic", "bold"), bg="white")
heading1_label.place(x=35, y=20)
heading2_label = Label(First_Frame, text=" Library ", font=("arial", 30, "italic", "bold"), bg="white")
heading2_label.place(x=110, y=80)

# Second frame
Second_frame = Frame(root, width=400, height=450, bg="#EADDCA")   # Colour Almond = #EADDCA
Second_frame.place(x=471, y=50)

IMG = (Image.open("FirstFrame image.PNG"))
resizing_Image = IMG.resize((400, 450))
New_IMG = ImageTk.PhotoImage(resizing_Image)

Image_label1 = Label(Second_frame, image=New_IMG, bd=0)
Image_label1.place(x=0, y=0)

Admin_Image = (Image.open("Admin.PNG"))    # image
resizing_Image = Admin_Image.resize((150, 150))
New_AdminIMG = ImageTk.PhotoImage(resizing_Image)

Admin_button = Button(Image_label1, width=150, height=150, image=New_AdminIMG, bd=0, command=Admin)
Admin_button.place(x=10, y=10)

Student_Image = (Image.open("Student.PNG"))    # image
resizing_Image = Student_Image.resize((130, 130))
New_StudentIMG = ImageTk.PhotoImage(resizing_Image)

Student_Button = Button(Image_label1, width=130, height=130, image=New_StudentIMG, bd=0, command=Student)
Student_Button.place(x=250, y=310)

root.mainloop()
