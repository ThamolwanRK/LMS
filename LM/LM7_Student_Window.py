from tkinter import *
from PIL import ImageTk, Image
import mysql.connector
from tkinter import ttk
import tkinter.messagebox




def Place_Order():
    PO_Frame = Frame(StudentWindow, width=1050, height=600, bg="black")
    PO_Frame.place(x=279, y=50)


    StudentName_Label = Label(PO_Frame, text=" Student Name :", font=(None, 15, "bold"), fg="#D27D2D", bg="black")  # Cinnamon = #D27D2D
    StudentName_Label.place(x=50, y=5)
    StudentName_Entry = Entry(PO_Frame, font=(None, 13, "bold"), fg="#00FFFF", width=25, bg="Black", bd=1)
    StudentName_Entry.place(x=12, y=35)

    Class_Label = Label(PO_Frame, text="Class :", font=(None, 15, "bold"), fg="#D27D2D", bg="black")
    Class_Label.place(x=335, y=5)
    Class_Entry = Entry(PO_Frame, font=(None, 13, "bold"), fg="#00FFFF", width=20, bg="Black", bd=1)
    Class_Entry.place(x=270, y=35)

    Bookid_Label = Label(PO_Frame, text="Book ID :", font=(None, 15, "bold"), fg="#D27D2D", bg="black")
    Bookid_Label.place(x=320, y=70)
    Bookid_Entry = Entry(PO_Frame, font=(None, 13, "bold"), fg="#00FFFF", width=20, bg="Black", bd=1)
    Bookid_Entry.place(x=270, y=100)

    Date_Label = Label(PO_Frame, text="Date: Year-Month-Date", font=(None, 15, "bold"), fg="#D27D2D", bg="black")
    Date_Label.place(x=16, y=70)
    Date_Entry = Entry(PO_Frame, font=(None, 13, "bold"), fg="#00FFFF", width=25, bg="Black", bd=1)
    Date_Entry.place(x=12, y=100)

    BookName_Label = Label(PO_Frame, text="Book Name :", font=(None, 15, "bold"), fg="#D27D2D", bg="black")
    BookName_Label.place(x=12, y=133)
    BookName_Entry = Entry(PO_Frame, font=(None, 13, "bold"), fg="#00FFFF", width=49, bg="Black", bd=1)
    BookName_Entry.place(x=12, y=163)

    AuthorName_Label = Label(PO_Frame, text="Author Name :", font=(None, 15, "bold"), fg="#D27D2D", bg="black")
    AuthorName_Label.place(x=12, y=200)
    AuthorName_Entry = Entry(PO_Frame, font=(None, 13, "bold"), fg="#00FFFF", width=49, bg="Black", bd=1)
    AuthorName_Entry.place(x=12, y=230)

    Order_Button = Button(PO_Frame, text="Place Order", fg="#D27D2D", font=(None, 20, "bold"), command=lambda: [Order()], bg="Black", relief=RAISED, bd=10, activeforeground="#D27D2D", activebackground="black")
    Order_Button.place(x=140, y=300)

    def Order():
        if StudentName_Entry.get() == '' or Class_Entry.get() == '' or Bookid_Entry.get() == '' or Date_Entry.get() == '' or BookName_Entry.get() == '' or AuthorName_Entry.get() == '':
            tkinter.messagebox.showerror("ERROR", "All fields should be field")
        else:
            try:
                mydb = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="mysql80",
                    port="3306",
                    database="library_management"

                )
                Student_ID = '0'
                StudentName = StudentName_Entry.get()
                Class = Class_Entry.get()
                Bookid = Bookid_Entry.get()
                BookName = BookName_Entry.get()
                AuthorName = AuthorName_Entry.get()
                date = Date_Entry.get()

                Query = "Insert into issue_book values(%s, %s,%s,%s,%s,%s,%s)"
                val = (Student_ID, StudentName, Class, Bookid, BookName, AuthorName, date)
                mycursor.execute(Query, val)

                Query1 = "Update books_details set Quantity = Quantity - 1 where Book_ID=%s and Book_Name=%s"
                val1 = (Bookid, BookName)
                mycursor.execute(Query1, val1)

                mydb.commit()
                tkinter.messagebox.showinfo("INFO", "Your Order is  placed :) \n Please Save your Student ID")

                # Clearing the text boxes

                StudentName_Entry.delete(0, END)
                Class_Entry.delete(0, END)
                Bookid_Entry.delete(0, END)
                BookName_Entry.delete(0, END)
                AuthorName_Entry.delete(0, END)
                Date_Entry.delete(0, END)

                button = Button(PO_Frame, text="Click to see ur ID", command=lambda: [ID()], width=20, bd=0, fg="red", bg="black", activeforeground="red", activebackground="Black")
                button.place(x=165, y=390)
            except:
                mydb.rollback()
                tkinter.messagebox.showerror("ERROR", "Something went wrong \n Please check the data")

            def ID():

                ID_Frame = Frame(PO_Frame, width=254, height=75, bg="white")
                ID_Frame.place(x=105, y=430)

                STD_ID = ttk.Treeview(ID_Frame, columns=("Student_ID", "Student_Name"), show="headings")

                m = ttk.Style(ID_Frame)
                m.theme_use("clam")

                m.configure("Treeview.Heading", font=(None, 10), background="Black", foreground="#00FFFF")
                m.configure("Treeview", font=(None, 10), background="Black", foreground="Pink")

                STD_ID.heading("Student_ID", text="Your ID", anchor=CENTER)
                STD_ID.heading("Student_Name", text="Your Name", anchor=CENTER)

                STD_ID.column("Student_ID", width=100, minwidth=100, anchor=CENTER)
                STD_ID.column("Student_Name", width=150, minwidth=150, anchor=CENTER)

                Query2 = "Select Student_ID , Student_Name from issue_book where Student_Name=%s and Class=%s and Book_ID=%s and Book_Name=%s and Author_Name=%s and Date=%s"
                val2 = (StudentName, Class, Bookid, BookName, AuthorName, date)

                mycursor.execute(Query2, val2)

                for r in mycursor:
                    STD_ID.insert('', END, values=(r[0], r[1]))

                STD_ID.place(x=0, y=0)

    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="mysql80",
        port="3306",
        database="library_management"

    )
    mycursor = mydb.cursor()

    # Creating a table
    table = ttk.Treeview(PO_Frame, columns=("Book_ID", "Book_Name", "Author_Name", "Quantity"), show="headings")

    s = ttk.Style(PO_Frame)
    s.theme_use("clam")

    s.configure("Treeview.Heading", font=(None, 15), background="Black", foreground="#00FFFF")
    s.configure("Treeview", font=(None, 10), background="Black", foreground="Pink", rowheight=56)


    table.heading("Book_ID", text="Book ID", anchor=CENTER)
    table.heading("Book_Name", text="Book Name", anchor=CENTER)
    table.heading("Author_Name", text="Author", anchor=CENTER)
    table.heading("Quantity", text="Quantity", anchor=CENTER)

    table.column("Book_ID", width=90, minwidth=90, anchor=W)
    table.column("Book_Name", width=255, minwidth=255, anchor=W)
    table.column("Author_Name", width=140, minwidth=140, anchor=W)
    table.column("Quantity", width=85, minwidth=85, anchor=W)

    query = "Select Book_ID, Book_Name, Author_Name, Quantity FROM books_details"
    mycursor.execute(query)

    for row in mycursor:
        table.insert('', END, values=(row[0], row[1], row[2], row[3]))

    table.place(x=475, y=0)


def ReturnBook():
    RB_Frame = Frame(StudentWindow, width=1050, height=600, bg="black")
    RB_Frame.place(x=279, y=50)

    # **** Creating a Canvas *****
    Canvas11 = Canvas(RB_Frame, width=20, height=600, bg="#FAD5A5", highlightthickness=0)
    Canvas11.place(x=800, y=0)

    Canvas10 = Canvas(RB_Frame, width=20, height=600, bg="#967969", highlightthickness=0)  # Mocha = #967969
    Canvas10.place(x=820, y=0)

    Canvas9 = Canvas(RB_Frame, width=20, height=600, bg="#FAD5A5", highlightthickness=0)
    Canvas9.place(x=840, y=0)

    Canvas8 = Canvas(RB_Frame, width=20, height=600, bg="#967969", highlightthickness=0)
    Canvas8.place(x=860, y=0)

    Canvas1 = Canvas(RB_Frame, width=20, height=600, bg="#FAD5A5", highlightthickness=0)
    Canvas1.place(x=880, y=0)

    Canvas2 = Canvas(RB_Frame, width=20, height=600, bg="#967969", highlightthickness=0)
    Canvas2.place(x=900, y=0)

    Canvas3 = Canvas(RB_Frame, width=20, height=600, bg="#FAD5A5", highlightthickness=0)
    Canvas3.place(x=920, y=0)

    Canvas4 = Canvas(RB_Frame, width=20, height=600, bg="#967969", highlightthickness=0)
    Canvas4.place(x=940, y=0)

    Canvas5 = Canvas(RB_Frame, width=20, height=600, bg="#FAD5A5", highlightthickness=0)
    Canvas5.place(x=960, y=0)

    Canvas6 = Canvas(RB_Frame, width=20, height=600, bg="#967969", highlightthickness=0)
    Canvas6.place(x=980, y=0)

    Canvas7 = Canvas(RB_Frame, width=20, height=600, bg="#FAD5A5", highlightthickness=0)
    Canvas7.place(x=1000, y=0)





    StudentID_Label = Label(RB_Frame, text=" Student ID :", font=(None, 20, "bold"), fg="#FAD5A5", bg="black")  # Desert = #FAD5A5
    StudentID_Label.place(x=90, y=15)
    StudentID_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=20, bg="Black", bd=1)
    StudentID_Entry.place(x=20, y=55)

    StudentName_Label = Label(RB_Frame, text=" Student Name :", font=(None, 20, "bold"), fg="#FAD5A5", bg="black")
    StudentName_Label.place(x=490, y=15)
    StudentName_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=20, bg="Black", bd=1)
    StudentName_Entry.place(x=450, y=55)

    Class_Label = Label(RB_Frame, text="Class :", font=(None, 20, "bold"), fg="#FAD5A5", bg="black")
    Class_Label.place(x=560, y=120)
    Class_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=20, bg="Black", bd=1)
    Class_Entry.place(x=450, y=160)

    Bookid_Label = Label(RB_Frame, text="Book ID :", font=(None, 20, "bold"), fg="#FAD5A5", bg="black")
    Bookid_Label.place(x=610, y=220)
    Bookid_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=10, bg="Black", bd=1)
    Bookid_Entry.place(x=600, y=260)

    Date_Label = Label(RB_Frame, text="Order Date: Year-Month-Date", font=(None, 20, "bold"), fg="#FAD5A5", bg="black")
    Date_Label.place(x=20, y=120)
    Date_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=25, bg="Black", bd=1)
    Date_Entry.place(x=20, y=160)

    BookName_Label = Label(RB_Frame, text="Book Name :", font=(None, 20, "bold"), fg="#FAD5A5", bg="black")
    BookName_Label.place(x=20, y=220)
    BookName_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=35, bg="Black", bd=1)
    BookName_Entry.place(x=20, y=260)

    AuthorName_Label = Label(RB_Frame, text="Author Name :", font=(None, 20, "bold"), fg="#FAD5A5", bg="black")
    AuthorName_Label.place(x=20, y=320)
    AuthorName_Entry = Entry(RB_Frame, font=(None, 20, "bold"), fg="#00FFFF", width=49, bg="Black", bd=1)
    AuthorName_Entry.place(x=20, y=360)

    Order_Button = Button(RB_Frame, text="     Return     ", fg="#FAD5A5", font=(None, 20, "bold"), command=lambda: [Return()], bg="Black", relief=RAISED, bd=10, activeforeground="#D27D2D", activebackground="black")
    Order_Button.place(x=280, y=440)

    def Return():
        if StudentName_Entry.get() == '' or Class_Entry.get() == '' or Bookid_Entry.get() == '' or Date_Entry.get() == '' or BookName_Entry.get() == '' or AuthorName_Entry.get() == '':
            tkinter.messagebox.showerror("ERROR", "All fields should be field")
        else:
            mydb = mysql.connector.connect(
                host="localhost",
                user="root",
                password="mysql80",
                port="3306",
                database="library_management"

            )

            StudentID = StudentID_Entry.get()
            StudentName = StudentName_Entry.get()
            Class = Class_Entry.get()
            Bookid = Bookid_Entry.get()
            BookName = BookName_Entry.get()
            AuthorName = AuthorName_Entry.get()
            date = Date_Entry.get()

            mycursor = mydb.cursor()
            Query = "DELETE FROM issue_book where Student_ID=%s and Student_Name=%s and Class=%s and Book_ID=%s and Book_Name=%s and Author_Name=%s and Date=%s"
            val = (StudentID, StudentName, Class, Bookid, BookName, AuthorName, date)
            mycursor.execute(Query, val)

            Query1 = "Update books_details set Quantity = Quantity + 1 where Book_ID=%s and Book_Name=%s"
            val1 = (Bookid, BookName)
            mycursor.execute(Query1, val1)

            mydb.commit()
            tkinter.messagebox.showinfo("INFO", "Book Returned")

            # Clearing the text boxes
            StudentID_Entry.delete(0, END)
            StudentName_Entry.delete(0, END)
            Class_Entry.delete(0, END)
            Bookid_Entry.delete(0, END)
            BookName_Entry.delete(0, END)
            AuthorName_Entry.delete(0, END)
            Date_Entry.delete(0, END)

def LogOut():
    StudentWindow.destroy()






#Main Window

StudentWindow = Tk()

# format of window
StudentWindow.geometry("1370x680+0+10")
StudentWindow.configure(bg="Black")
StudentWindow.maxsize(1370, 680)
StudentWindow.minsize(1370, 680)
StudentWindow.title("OUR LIBRARY")

# Window icon
p1 = PhotoImage(file="icon.PNG")
StudentWindow.iconphoto(False, p1)


#**** IMAGES ****
SW_CImage = (Image.open("SW.Image.PNG"))
Resizing_AD_CImage = SW_CImage.resize((250, 600))
New_AD_CImage = ImageTk.PhotoImage(Resizing_AD_CImage)

# **** Creating a Canvas *****
SW_Canvas = Canvas(StudentWindow, width=250, height=600, bg="white", highlightthickness=0)
SW_Canvas.place(x=29, y=50)
SW_Canvas.create_image(125, 300, image=New_AD_CImage)

#  creating buttons
PlaceOrder_Button = Button(SW_Canvas, text="     Place order     ", font=(None, 17, "bold"), command=Place_Order, bg="#FAD5A5", fg="#4A0404", activebackground="#FAD5A5", activeforeground="#4A0404", bd=1, relief=RAISED)  # Oxblood= #4A0404 (colour)
PlaceOrder_Button.place(x=20, y=20)

ReturnBook_button = Button(SW_Canvas, text="Return Of Books", command=ReturnBook, font=(None, 17, "bold"), bg="#FAD5A5", fg="#4A0404", activebackground="#FAD5A5", activeforeground="#4A0404", bd=1, relief=RAISED)
ReturnBook_button.place(x=20, y=70)

Logout_button = Button(SW_Canvas, text="Log Out", font=(None, 10, "bold"), command=LogOut, bd=0, bg="#6E260E", fg="#FAD5A5", activebackground="#6E260E", activeforeground="#FAD5A5")  # Burnt Umber =#6E260E
Logout_button.place(x=190, y=575)

StudentWindow.mainloop()
