from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image

#****** To verify the username and password entered by the user ********
def verification():
    if EnterUserName.get() == '' and EnterPassword.get() == '':
        tkinter.messagebox.showerror("ERROR", "All the fields should be filled")
    else:
        # *** Connecting to mysql database ***
        mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            password='mysql80',
            port='3306',
            database='library_management'
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM student_login WHERE USERNAME=%s and PASSWORD=%s", (EnterUserName.get(), EnterPassword.get()))
        row = mycursor.fetchone()
        if row is None:
            tkinter.messagebox.showerror("ERROR", "USERNAME and PASSWORD  not matched ")
        else:
            StudentWindow()


# *** joining  two python files ***
def StudentWindow():
    root.destroy()
    import LM7_Student_Window

def RegisterWindow():
    root.destroy()
    import LM4_Register


# *** Login window ***
root = Tk()
root.geometry("950x550+250+100")
root.maxsize(950, 550)
root.configure(background='Black')   # for background colour
root.title("OUR LIBRARY")

# Window icon
p1 = PhotoImage(file="icon.PNG")
root.iconphoto(False, p1)

# *** inserting image ***
Bookimage = (Image.open("Books.PNG"))
resizing_Image = Bookimage.resize((400, 450))
New_Bookimage = ImageTk.PhotoImage(resizing_Image)

Image_Frame = Frame(root, width=400, height=450, bg="black")
Image_Frame.place(x=70, y=50)

Image_Label = Label(Image_Frame, image=New_Bookimage)
Image_Label.place(x=0, y=0)




# *** Frame for login form ***
Login_frame = Frame(root, width=400, height=450, bg="#EADDCA")   # Colour Almond = #EADDCA
Login_frame.place(x=470, y=50)

Login = Label(Login_frame, text="WELCOME", font=(None, 30, "bold"), fg="#A95C68", bg="#EADDCA", )  # Colour Puce = #A95C68
Login.place(x=100, y=10)

UserName = Label(Login_frame, text="USER NAME  ", font=(None, 20, "bold"), bg="#EADDCA", fg="#A95C68")
UserName.place(x=50, y=100)
Password = Label(Login_frame, text="PASSWORD  ", font=(None, 20, "bold"), bg="#EADDCA", fg="#A95C68")
Password.place(x=50, y=200)

EnterUserName = Entry(Login_frame, bg="#EADDCA", fg="#814141", bd=2, width=20, font=(None, 20))
EnterPassword = Entry(Login_frame, bg="#EADDCA", fg="#814141", bd=2, width=20, font=(None, 20))
EnterUserName.place(x=55, y=150)
EnterPassword.place(x=55, y=250)

LogIn = Button(Login_frame, text="LOG IN ", font=(None, 30, "bold"), command=verification, bg="#EADDCA", fg="#A95C68", bd=0, activebackground="#EADDCA")
LogIn.place(x=110, y=320)

R_button = Button(Login_frame, text="Not Registered?  Register Now!",  bg="#EADDCA", fg="#A95C68", bd=0, activebackground="#EADDCA", command=RegisterWindow)
R_button.place(x=112, y=380)

root.mainloop()