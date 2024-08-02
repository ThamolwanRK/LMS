from tkinter import *
import mysql.connector
import tkinter.messagebox
from PIL import ImageTk, Image

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='mysql80',
    port='3306',
    database='library_management'
)


# ****** To verify the username and password entered by the user ********
def Registering():
    if EnterUserName.get() == '' and EnterPassword.get() == '':
        tkinter.messagebox.showerror("ERROR", "All the fields should be filled")
    else:

        try:
            # *** Connecting to mysql database ***

            UN = EnterUserName.get()
            P = EnterPassword.get()

            mycursor = mydb.cursor()
            mycursor.execute("Insert into student_login values(%s,%s)", (UN, P))

            mydb.commit()
            tkinter.messagebox.showinfo("Info", "WELCOME TO THE LIBRARY")

            # Clearing the text boxes

            EnterUserName.delete(0, END)
            EnterPassword.delete(0, END)

            root.destroy()

            import LM7_Student_Window

        except:

            mydb.rollback()
            tkinter.messagebox.showerror("ERROR", "Something went wrong. \n PLEASE TRY AGAIN")



# Goo back
def GOBack():
    root.destroy()
    import LM3_LOGIN_Student




# *** Register Window ***
root = Tk()
root.geometry("950x550+250+100")
root.maxsize(950, 550)
root.configure(background='Black')  # for background colour
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

Image_Label = Label(Image_Frame, image=New_Bookimage, bd=0)
Image_Label.place(x=0, y=0)

# *** Frame for Registration ***
Registration_frame = Frame(root, width=400, height=450, bg="#EADDCA")  # Colour Almond = #EADDCA
Registration_frame.place(x=470, y=50)

Register = Label(Registration_frame, text="Register to Our Library", font=(None, 25, "bold", "italic", "underline"), fg="#A95C68", bg="#EADDCA", )  # Colour Puce = #A95C68
Register.place(x=20, y=10)

UserName = Label(Registration_frame, text="USER NAME  ", font=(None, 20, "bold"), bg="#EADDCA", fg="#A95C68")
UserName.place(x=50, y=100)
Password = Label(Registration_frame, text="PASSWORD  ", font=(None, 20, "bold"), bg="#EADDCA", fg="#A95C68")
Password.place(x=50, y=200)

EnterUserName = Entry(Registration_frame, bg="#EADDCA", fg="#814141", bd=2, width=20, font=(None, 20))
EnterPassword = Entry(Registration_frame, bg="#EADDCA", fg="#814141", bd=2, width=20, font=(None, 20))
EnterUserName.place(x=55, y=150)
EnterPassword.place(x=55, y=250)

LogIn = Button(Registration_frame, text=" Done! ", font=(None, 30, "bold"), command=Registering, bg="#EADDCA",
               fg="#A95C68", bd=0)
LogIn.place(x=110, y=320)

GoBack_button = Button(Registration_frame, text="Go back", command=GOBack, bg="#EADDCA", fg="#A95C68", bd=0)
GoBack_button.place(x=0, y=430)

root.mainloop()