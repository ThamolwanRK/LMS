from tkinter import *
import tkinter.messagebox
import mysql.connector
from PIL import ImageTk, Image


# function for adding books
def Add_Books():
    AB_Frame = Frame(AdminWindow, width=710, height=600, bg="black")
    AB_Frame.place(x=350, y=50)

    AddBooks_Label = Label(AB_Frame, text="Add Book", font=(None, 30, "bold"), fg="#00FFFF", bg="black")  # Aqua = #00FFFF
    AddBooks_Label.place(x=250, y=10)

    Bookid_Label = Label(AB_Frame, text="Book ID :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    Bookid_Label.place(x=50, y=100)
    Bookid_Entry = Entry(AB_Frame, font=(None, 20, "bold"), fg="white", width=40, bg="black", bd=2)
    Bookid_Entry.place(x=50, y=140)

    BookName_Label = Label(AB_Frame, text="Book Name :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    BookName_Label.place(x=50, y=190)
    BookName_Entry = Entry(AB_Frame, font=(None, 20, "bold"), fg="white", width=40, bg="black", bd=2)
    BookName_Entry.place(x=50, y=230)

    AuthorName_Label = Label(AB_Frame, text="Author Name :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    AuthorName_Label.place(x=50, y=280)
    AuthorName_Entry = Entry(AB_Frame, font=(None, 20, "bold"), fg="white", width=40, bg="black", bd=2)
    AuthorName_Entry.place(x=50, y=320)

    Cost_Label = Label(AB_Frame, text="Cost :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    Cost_Label.place(x=50, y=370)
    Cost_Entry = Entry(AB_Frame, font=(None, 20, "bold"), fg="white", width=40, bg="black", bd=2)
    Cost_Entry.place(x=50, y=405)

    Quantity_Label = Label(AB_Frame, text="Quantity :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    Quantity_Label.place(x=50, y=457)
    Quantity_Entry = Entry(AB_Frame, font=(None, 20, "bold"), fg="white", width=40, bg="black", bd=2)
    Quantity_Entry.place(x=50, y=495)

    ADD_Button = Button(AB_Frame, text="                    A  D  D                    ", fg="#00FFFF", font=(None, 14, "bold"), command=lambda: [Insert_values()], relief=RAISED, bg="Black", bd=10, activebackground="black", activeforeground="#00FFFF")
    ADD_Button.place(x=50, y=542)

    ShowData_Button = Button(AB_Frame, text="             S h o w  D a t a               ", fg="#00FFFF", font=(None, 14, "bold"), command=lambda: [displayTables()], relief=RAISED, bg="Black", bd=10, activebackground="black", activeforeground="#00FFFF")
    ShowData_Button.place(x=350, y=542)

    def displayTables():
        AdminWindow.destroy()
        import LM6_Display_Tables_Window

    def Insert_values():
        if Bookid_Entry.get() == '' or BookName_Entry.get() == '' or AuthorName_Entry.get() == '' or Cost_Entry.get() == '' or Quantity_Entry.get() == '':
            tkinter.messagebox.showerror("Error", "all field should be field")
        else:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysql80',
                port='3306',
                database='library_management'
            )
            mycursor = mydb.cursor()

            Bookid = Bookid_Entry.get()
            BookName = BookName_Entry.get()
            AuthorName = AuthorName_Entry.get()
            Cost = Cost_Entry.get()
            Quantity = Quantity_Entry.get()

            Query = "Insert into books_details values(%s,%s,%s,%s,%s)"
            val = (Bookid, BookName, AuthorName, Cost, Quantity)
            mycursor.execute(Query, val)
            mydb.commit()
            tkinter.messagebox.showinfo("Info", "Successfully recorded!")

            # Clearing the text boxes
            Bookid_Entry.delete(0, END)
            BookName_Entry.delete(0, END)
            AuthorName_Entry.delete(0, END)
            Cost_Entry.delete(0, END)
            Quantity_Entry.delete(0, END)


# **** ISSUE OF BOOKS****
def Issue_Books():
    IB_Frame = Frame(AdminWindow, width=710, height=600, bg="Black")
    IB_Frame.place(x=350, y=50)

    IssueBooks_Label = Label(IB_Frame, text="Issue Book", font=(None, 30, "bold"), fg="White", bg="Black")  # Neon Pink = #FF10F0
    IssueBooks_Label.place(x=250, y=10)

    StudentID_Label = Label(IB_Frame, text="Student ID :", font=(None, 20, "bold"), fg="White", bg="Black")
    StudentID_Label.place(x=70, y=80)
    StudentID_Entry = Entry(IB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=15, bg="Black", bd=1)
    StudentID_Entry.place(x=50, y=120)

    StudentName_Label = Label(IB_Frame, text=" Student Name :", font=(None, 20, "bold"), fg="White", bg="Black")
    StudentName_Label.place(x=430, y=80)
    StudentName_Entry = Entry(IB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=15, bg="Black", bd=1)
    StudentName_Entry.place(x=425, y=120)

    Class_Label = Label(IB_Frame, text="Class :", font=(None, 20, "bold"), fg="White", bg="Black")
    Class_Label.place(x=80, y=190)
    Class_Entry = Entry(IB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=10, bg="Black", bd=1)
    Class_Entry.place(x=50, y=230)

    Bookid_Label = Label(IB_Frame, text="Book ID :", font=(None, 20, "bold"), fg="White", bg="Black")
    Bookid_Label.place(x=285, y=195)
    Bookid_Entry = Entry(IB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=10, bg="Black", bd=1)
    Bookid_Entry.place(x=270, y=230)

    Date_Label = Label(IB_Frame, text="Date :", font=(None, 20, "bold"), fg="White", bg="Black")
    Date_Label.place(x=540, y=195)
    Date_Entry = Entry(IB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=10, bg="Black", bd=1)
    Date_Entry.place(x=500, y=230)

    BookName_Label = Label(IB_Frame, text="Book Name :", font=(None, 20, "bold"), fg="White", bg="Black")
    BookName_Label.place(x=50, y=290)
    BookName_Entry = Entry(IB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=40, bg="Black", bd=1)
    BookName_Entry.place(x=50, y=330)

    AuthorName_Label = Label(IB_Frame, text="Author Name :", font=(None, 20, "bold"), fg="White", bg="Black")
    AuthorName_Label.place(x=50, y=390)
    AuthorName_Entry = Entry(IB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=40, bg="Black", bd=1)
    AuthorName_Entry.place(x=50, y=430)

    ADD_Button = Button(IB_Frame, text="               ADD               ", fg="White", font=(None, 20, "bold"), command=lambda: [Inserting_IssuedBooks()], bg="Black", relief=RAISED, bd=10, activeforeground="White", activebackground="black")
    ADD_Button.place(x=200, y=500)

    def Inserting_IssuedBooks():
        if StudentID_Entry.get() == '' or StudentName_Entry.get() == '' or Class_Entry.get() == '' or Bookid_Entry.get() == '' or BookName_Entry.get() == '':
            tkinter.messagebox.showerror("Error", "all field should be field")
        else:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysql80',
                port='3306',
                database='library_management'
            )
            mycursor = mydb.cursor()

            StudentID = StudentID_Entry.get()
            StudentName = StudentName_Entry.get()
            Class = Class_Entry.get()
            Bookid = Bookid_Entry.get()
            BookName = BookName_Entry.get()
            AuthorName = AuthorName_Entry.get()
            date = Date_Entry.get()

            Query = "Insert into issue_book values(%s,%s,%s,%s,%s,%s,%s)"
            val = (StudentID, StudentName, Class, Bookid, BookName, AuthorName, date)
            mycursor.execute(Query, val)

            Query1 = "Update books_details set Quantity = Quantity - 1 where Book_ID=%s and Book_Name=%s"
            val1 = (Bookid, BookName)
            mycursor.execute(Query1, val1)

            mydb.commit()
            tkinter.messagebox.showinfo("Info", "Successfully recorded!")

            # Clearing the text boxes
            StudentID_Entry.delete(0, END)
            StudentName_Entry.delete(0, END)
            Class_Entry.delete(0, END)
            Bookid_Entry.delete(0, END)
            BookName_Entry.delete(0, END)
            AuthorName_Entry.delete(0, END)
            Date_Entry.delete(0, END)


# **** Return of book****
def Returned_Books():
    RB_Frame = Frame(AdminWindow, width=710, height=600, bg="black")
    RB_Frame.place(x=350, y=50)

    ReturnBooks_Label = Label(RB_Frame, text="Return Book", font=(None, 30, "bold"), fg="#00FFFF", bg="black")
    ReturnBooks_Label.place(x=250, y=10)

    StudentID_Label = Label(RB_Frame, text="Student ID :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    StudentID_Label.place(x=70, y=80)
    StudentID_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="white", width=15, bg="black", bd=1)
    StudentID_Entry.place(x=50, y=120)

    StudentName_Label = Label(RB_Frame, text=" Student Name :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    StudentName_Label.place(x=430, y=80)
    StudentName_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="white", width=15, bg="black", bd=1)
    StudentName_Entry.place(x=425, y=120)

    Class_Label = Label(RB_Frame, text="Class :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    Class_Label.place(x=80, y=190)
    Class_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="white", width=10, bg="black", bd=1)
    Class_Entry.place(x=50, y=230)

    Bookid_Label = Label(RB_Frame, text="Book ID :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    Bookid_Label.place(x=285, y=195)
    Bookid_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="white", width=10, bg="black", bd=1)
    Bookid_Entry.place(x=270, y=230)

    Date_Label = Label(RB_Frame, text="Order Date :", font=(None, 20, "bold"), fg="#00FFFF", bg="Black")
    Date_Label.place(x=493, y=195)
    Date_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="white", width=10, bg="Black", bd=1)
    Date_Entry.place(x=500, y=230)

    BookName_Label = Label(RB_Frame, text="Book Name :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    BookName_Label.place(x=50, y=290)
    BookName_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="white", width=40, bg="black", bd=1)
    BookName_Entry.place(x=50, y=330)

    AuthorName_Label = Label(RB_Frame, text="Author Name :", font=(None, 20, "bold"), fg="#00FFFF", bg="black")
    AuthorName_Label.place(x=50, y=390)
    AuthorName_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="white", width=40, bg="black", bd=1)
    AuthorName_Entry.place(x=50, y=430)

    Returned_Button = Button(RB_Frame, text="        R E T U R N E D        ", fg="#00FFFF", bg="Black", font=(None, 20, "bold"), command=lambda: [Deleting_IssuedBooks()], activebackground="black", activeforeground="#FFFF00", bd=10, relief=RAISED)
    Returned_Button.place(x=185, y=500)

    def Deleting_IssuedBooks():
        if StudentID_Entry.get() == '' or StudentName_Entry.get() == '' or Class_Entry.get() == '' or Bookid_Entry.get() == '' or BookName_Entry.get() == '' or AuthorName_Entry.get() == '':
            tkinter.messagebox.showerror("Error", "all field should be field")
        else:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysql80',
                port='3306',
                database='library_management'
            )
            mycursor = mydb.cursor()

            StudentID = StudentID_Entry.get()
            StudentName = StudentName_Entry.get()
            Class = Class_Entry.get()
            Bookid = Bookid_Entry.get()
            BookName = BookName_Entry.get()
            AuthorName = AuthorName_Entry.get()
            Date = Date_Entry.get()

            Query = "DELETE FROM issue_book where Student_ID=%s and Student_Name=%s and Class=%s and Book_ID=%s and Book_Name=%s and Author_Name=%s and Date=%s"
            val = (StudentID, StudentName, Class, Bookid, BookName, AuthorName, Date)
            mycursor.execute(Query, val)

            Query1 = "UPDATE  books_details set Quantity = Quantity + 1 where Book_ID=%s and Book_Name=%s"
            val1 = (Bookid, BookName)
            mycursor.execute(Query1, val1)
            mydb.commit()
            tkinter.messagebox.showinfo("Info", "Book Returned")

            # Clearing the text boxes
            StudentID_Entry.delete(0, END)
            StudentName_Entry.delete(0, END)
            Class_Entry.delete(0, END)
            Bookid_Entry.delete(0, END)
            BookName_Entry.delete(0, END)
            AuthorName_Entry.delete(0, END)
            Date_Entry.delete(0, END)


# **** Deleting exiting books ***
def Delete_Books():
    DB_Frame = Frame(AdminWindow, width=710, height=600, bg="black")
    DB_Frame.place(x=350, y=50)

    DeleteBook_Label = Label(DB_Frame, text="DELETE BOOK", font=(None, 30, "bold"), fg="White", bg="black")
    DeleteBook_Label.place(x=240, y=10)

    Bookid_Label = Label(DB_Frame, text="Book ID :", font=(None, 20, "bold"), fg="White", bg="black")
    Bookid_Label.place(x=50, y=120)
    Bookid_Entry = Entry(DB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=40, bg="black", bd=1)
    Bookid_Entry.place(x=50, y=160)

    BookName_Label = Label(DB_Frame, text="Book Name :", font=(None, 20, "bold"), fg="White", bg="black")
    BookName_Label.place(x=50, y=240)
    BookName_Entry = Entry(DB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=40, bg="black", bd=1)
    BookName_Entry.place(x=50, y=280)

    AuthorName_Label = Label(DB_Frame, text="Author Name :", font=(None, 20, "bold"), fg="White", bg="black")
    AuthorName_Label.place(x=50, y=360)
    AuthorName_Entry = Entry(DB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=40, bg="black", bd=1)
    AuthorName_Entry.place(x=50, y=400)

    ADD_Button = Button(DB_Frame, text="          D E L E T E        ", fg="White", bg="black", font=(None, 20, "bold"),
                        command=lambda: [Deleting_ExistingBooks()], activeforeground="White", activebackground="Black",
                        bd=10, relief=RAISED)
    ADD_Button.place(x=200, y=500)

    def Deleting_ExistingBooks():
        if Bookid_Entry.get() == '' or BookName_Entry.get() == '' or AuthorName_Entry.get() == '':
            tkinter.messagebox.showerror("Error", "all field should be field")
        else:
            mydb = mysql.connector.connect(
                host='localhost',
                user='root',
                password='mysql80',
                port='3306',
                database='library_management'
            )
            mycursor = mydb.cursor()

            Bookid = Bookid_Entry.get()
            BookName = BookName_Entry.get()
            AuthorName = AuthorName_Entry.get()

            Query = "DELETE FROM books_details where Book_ID=%s and Book_Name=%s and Author_Name=%s "
            val = (Bookid, BookName, AuthorName)

            mycursor.execute(Query, val)
            mydb.commit()
            tkinter.messagebox.showinfo("Info", "Book Delete")

            # Clearing the text boxes

            Bookid_Entry.delete(0, END)
            BookName_Entry.delete(0, END)
            AuthorName_Entry.delete(0, END)


def LogOut():
    AdminWindow.destroy()


# **** Window which only the Admin can access ***
AdminWindow = Tk()

AdminWindow.geometry("1100x680+150+10")
AdminWindow.configure(bg="Black")
AdminWindow.maxsize(1100, 680)
AdminWindow.minsize(1100, 680)
AdminWindow.title("OUR LIBRARY")

# Window icon
p1 = PhotoImage(file="icon.PNG")
AdminWindow.iconphoto(False, p1)

# **** IMAGES ****
AD_CImage = (Image.open("AD_Canvas1.PNG"))  # AD_Canvas Image
Resizing_AD_CImage = AD_CImage.resize((300, 600))
New_AD_CImage = ImageTk.PhotoImage(Resizing_AD_CImage)

# **** Creating a Canvas *****
AD_Canvas = Canvas(AdminWindow, width=300, height=600, bg="Black", highlightthickness=0)
AD_Canvas.place(x=50, y=50)

AD_Canvas.create_image(150, 300, image=New_AD_CImage)

AddBook_Button = Button(AD_Canvas, text="       Add Book      ", font=(None, 17, "bold"), command=Add_Books, bg="#E6E6FA", fg="Black", activebackground="Black", activeforeground="#F2D2BD", bd=1, relief=RAISED)  # lavender= #E6E6FA (colour)
AddBook_Button.place(x=55, y=20)

IssueOfBooks_button = Button(AD_Canvas, text="  Issue Of Books ", font=(None, 17, "bold"), command=Issue_Books, bg="#E6E6FA", fg="Black", activebackground="Black", activeforeground="#F2D2BD", bd=1, relief=RAISED)
IssueOfBooks_button.place(x=55, y=70)

ReturnOfBooks_button = Button(AD_Canvas, text="Return Of Books", font=(None, 17, "bold"), command=Returned_Books, bg="#E6E6FA", fg="Black", activebackground="Black", activeforeground="#F2D2BD", bd=1, relief=RAISED)
ReturnOfBooks_button.place(x=55, y=120)

DeleteBook_button = Button(AD_Canvas, text="   Delete Books   ", font=(None, 17, "bold"), command=Delete_Books, bg="#E6E6FA", fg="Black", activebackground="Black", activeforeground="#F2D2BD", bd=1, relief=RAISED)
DeleteBook_button.place(x=55, y=170)

Logout_button = Button(AD_Canvas, text="Log Out", font=(None, 10, "bold"), command=LogOut, bd=0, bg="#36454F", fg="#7DF9FF", activebackground="#36454F", activeforeground="#7DF9FF")  # Electric Blue = #7DF9FF , 	Charcoal = #36454F
Logout_button.place(x=240, y=575)

AdminWindow.mainloop()


