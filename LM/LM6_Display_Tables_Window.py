from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="mysql80",
    port="3306",
    database="library_management"
)

def DisplayBooks():
    booksDetails_Frame = Frame(DisplayTables, width=1000, height=600, bg="black")
    booksDetails_Frame.place(x=334, y=50)

    mycursor = mydb.cursor()

    booksDetails = ttk.Treeview(booksDetails_Frame, columns=("Book_ID", "Book_Name", "Author_Name", "Cost", "Quantity"), show="headings")


    #table theme
    s = ttk.Style(booksDetails_Frame)
    s.theme_use("clam")

    s.configure("Treeview", font=(None, 13, "bold"), background="Black", foreground="Pink", rowheight=55)
    s.configure("Treeview.Heading", font=(None, 15, "bold"), background="Black", foreground="#00FFFF")


    ##Assigning the heading names for each column
    booksDetails.heading("Book_ID", text="Book ID", anchor=CENTER)
    booksDetails.heading("Book_Name", text="Book Name", anchor=CENTER)
    booksDetails.heading("Author_Name", text="Author Name", anchor=CENTER)
    booksDetails.heading("Cost", text="Cost", anchor=CENTER)
    booksDetails.heading("Quantity", text="Quantity", anchor=CENTER)

    ##Formating the columns
    booksDetails.column("Book_ID", width=130, minwidth=130, anchor=W)
    booksDetails.column("Book_Name", width=355, minwidth=355, anchor=W)
    booksDetails.column("Author_Name", width=300, minwidth=300, anchor=W)
    booksDetails.column("Cost", width=100, minwidth=100, anchor=W)
    booksDetails.column("Quantity", width=100, minwidth=100, anchor=W)

    # Connecting to the database

    query1 = "Create table if not exists books_details (book_id int(10) PRIMARY KEY, book_name varchar(30), author_name varchar(39), cost int(10), quantity int(10) )"
    mycursor.execute(query1)

    query2 = "SELECT * FROM books_details"
    mycursor.execute(query2)

    i = 0
    for row in mycursor:
        booksDetails.insert('', END, text='', values=(row[0], row[1], row[2], row[3], row[4]))
        i = i + 1

    booksDetails.place(x=5, y=5)



def DisplayIssuedBooks():

    IB_Frame = Frame(DisplayTables, width=1000, height=600, bg="black")
    IB_Frame.place(x=334, y=50)

    mycursor = mydb.cursor()

    IB_details = ttk.Treeview(IB_Frame, columns=("Student_ID", "Student_Name", "Class", "Book_ID", "Book_Name", "Author_Name", "Date"), show="headings")

    # table theme
    s = ttk.Style(IB_Frame)
    s.theme_use("clam")

    s.configure("Treeview", font=(None, 13, "bold"), background="black", foreground="pink", rowheight=55)
    s.configure("Treeview.Heading", font=(None, 12, "bold"), background="Black", foreground="#00FFFF")


    ##Assigning the heading names for each column
    IB_details.heading("Student_ID", text="Student ID", anchor=CENTER)
    IB_details.heading("Student_Name", text="Student Name", anchor=CENTER)
    IB_details.heading("Class", text="Class", anchor=CENTER)
    IB_details.heading("Book_ID", text="Book ID", anchor=CENTER)
    IB_details.heading("Book_Name", text="Book Name", anchor=CENTER)
    IB_details.heading("Author_Name", text="Author Name", anchor=CENTER)
    IB_details.heading("Date", text="Date", anchor=CENTER)

    ##Formating the columns
    IB_details.column("Student_ID", width=90, minwidth=90, anchor=W)
    IB_details.column("Student_Name", width=120, minwidth=120, anchor=W)
    IB_details.column("Class", width=60, minwidth=60, anchor=W)
    IB_details.column("Book_ID", width=80, minwidth=80, anchor=W)
    IB_details.column("Book_Name", width=320, minwidth=320, anchor=W)
    IB_details.column("Author_Name", width=220, minwidth=220, anchor=W)
    IB_details.column("Date", width=100, minwidth=100, anchor=W)

    # Connecting to the database

    query1 = "Create table if not exists issue_book (Student_id int(10) PRIMARY KEY, Student_name varchar(30), Class varchar(30), Book_Name varchar(45), Author_Name varchar(45), Date DATE)"
    mycursor.execute(query1)

    query2 = "SELECT * FROM issue_book"
    mycursor.execute(query2)

    i = 0
    for row in mycursor:
        IB_details.insert('', END, text=' ', values=(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))

        i = i + 1

    IB_details.place(x=5, y=7)

def back():
    DisplayTables.destroy()

    import LM5_AdminWindow




# main window *********
DisplayTables = Tk()

# format of window
DisplayTables.geometry("1390x680+0+15")
DisplayTables.configure(bg="Black")
DisplayTables.maxsize(1390, 680)
DisplayTables.minsize(1390, 680)
DisplayTables.title(" OUR LIBRARY")

# Window icon
p1 = PhotoImage(file="icon.PNG")
DisplayTables.iconphoto(False, p1)


#**** IMAGES ****
AD_CImage = (Image.open("AD_Canvas1.PNG"))   # AD_Canvas Image
Resizing_AD_CImage = AD_CImage.resize((300, 600))
New_AD_CImage = ImageTk.PhotoImage(Resizing_AD_CImage)

# **** Creating a Canvas *****
AD_Canvas = Canvas(DisplayTables, width=300, height=600, bg="Black", highlightthickness=0)
AD_Canvas.place(x=29, y=50)
AD_Canvas.create_image(150, 300, image=New_AD_CImage)


Books_Button = Button(AD_Canvas, text="          Book Details          ", font=(None, 17, "bold"), command=DisplayBooks, bg="#E6E6FA", fg="Black", activebackground="Black", activeforeground="#F2D2BD", bd=1, relief=RAISED)  # lavender= #E6E6FA (colour)
Books_Button.place(x=10, y=20)

IssuedBooks_button = Button(AD_Canvas, text="Details of issued books", font=(None, 17, "bold"), command=DisplayIssuedBooks, bg="#E6E6FA", fg="Black", activebackground="Black", activeforeground="#F2D2BD", bd=1, relief=RAISED)
IssuedBooks_button.place(x=10, y=70)

Back_Button = Button(AD_Canvas, text="                 Back                 ", command=back, font=(None, 17, "bold"), bg="#E6E6FA", fg="Black", activebackground="Black", activeforeground="#F2D2BD", bd=1, relief=RAISED)
Back_Button.place(x=10, y=120)

DisplayTables.mainloop()
