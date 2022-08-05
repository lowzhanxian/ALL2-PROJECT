from tkinter import*
import mysql.connector as mysql
import os
import tkinter.messagebox as MessageBox
from PIL import Image,ImageTk #pip install Pillow


def register_user():
    username_info = username.get()
    password_info = password.get()

    #save into db
    if(username_info== "" or password_info==""):
        MessageBox.showerror("Insert status", "All fields are required")
        screen1.destroy()
    else :
        con = mysql.connect(host="localhost",user="root", password="", database="python-tkinter")
        cursor = con.cursor()
        cursor.execute("insert into user values('"+ username_info +"','" + password_info + "')")
        cursor.execute("commit");
        MessageBox.showinfo("Insert Status", "Register Succesfully");
        con.close();
        

def login_verify():
    username1 = username_verify.get()
    password1 = password_verify.get()

    if( username_verify.get() == '' or password_verify.get() == ''):
        MessageBox.showerror("Insert status", "All fields are required")
        screen2.destroy()
    else :
            con = mysql.connect(host="localhost",user="root", password="", database="python-tkinter")
            cursor=con.cursor()
            cursor.execute('Select * from user where name=%s and password=%s', (username_verify.get(), password_verify.get()))
            row=cursor.fetchone()

            if(username1 == "" or password1 == ""):
                MessageBox.showinfo("Insert Status", "Invalid Username & Password!")
            else:
                MessageBox.showinfo("Welcome", "Login Succesfully")
                screen2.destroy()
                os.system('python "C:\ALL2\All2\\Home page.py"')   
            con.close()
        
def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.title ("Register")
    screen1.geometry("500x500")
    screen1.configure(bg='skyblue2')

    global username
    global password
    global username_entry
    global password_entry
    
    username = StringVar()
    password = StringVar()

    Label(screen1, text = "Please Enter details below").pack()
    
    
    Label(screen1, text = "Username :",bg='skyblue2').pack()
    username_entry = Entry(screen1, textvariable = username)
    username_entry.pack()
    
    Label(screen1, text = "Password :",bg='skyblue2').pack()
    password_entry = Entry(screen1, textvariable = password, show = "*")
    password_entry.pack()

    
    Button(screen1, text = "Register",bg='Slategray4',fg='Black', width = 10, height = 1, command = register_user).pack()
    #back button
    backbutton33=Button(screen1,text='Back',width =10,bg='Slategray4',fg='Black',font='arial 10 bold',command=screen1.destroy)
    backbutton33.pack()

def login():
    global screen2
    screen2 = Toplevel(screen)
    screen2.title("Login")
    screen2.geometry("500x500")
    screen2.configure(bg='skyblue2')
    

    Label(screen2, text = "Please Enter details below to login").pack()
    

    global username_verify
    global password_verify
    global username_entry1
    global password_entry1
    
    username_verify = StringVar()
    Label(screen2, text = "Username :",bg='skyblue2').pack()
    username_entry1 = Entry(screen2, textvariable = username_verify)
    username_entry1.pack()
    

    password_verify = StringVar()
    Label(screen2, text = "Password :",bg='skyblue2').pack()
    password_entry1 = Entry(screen2, textvariable = password_verify, show = "*")
    password_entry1.pack()
    

    Button(screen2, text = "Login",bg='Slategray4',fg='Black', width = 10, height = 1, command = login_verify).pack()
    #back button
    backbutton22=Button(screen2,text='Back',width =10,bg='Slategray4',fg='Black',font='arial 10 bold',command=screen2.destroy)
    backbutton22.pack()
    

def main_screen ():
    global screen
    screen = Tk()
    screen.geometry("1280x1080")
    screen.title("LOGIN AND REGISTRATION")
    screen.configure(bg='skyblue2')


    #top frame
    Top_frame_page1=Frame(screen,bg='white',width=1280,height=120)
    Top_frame_page1.place(x=0,y=0)

    language_page1=Image.open('text to speech.png')
    t=ImageTk.PhotoImage(language_page1)
    labelii=Label(image=t)
    labelii.image=t
    labelii.place(x=80,y=250)
    
    Label(Top_frame_page1,text = "AUDIO TEXT CONVERTER APP", fg = "skyblue",font="arial 20 bold", bg='white').place(x=430,y=30)
    
    
    Button(text = "Login", height = "2", width = "30", command = login).place( x=500,y=150)

   
    Button(text = "Register", height = "2", width = "30", command = register).place( x=500,y=200)

    screen.mainloop
    
main_screen()
    
