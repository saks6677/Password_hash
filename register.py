from tkinter import *
from tkinter import OptionMenu
import sqlite3
import bcrypt
ws = Tk()
ws.title('Hashed_passwords')
ws.config(bg='black')

f = ('Times', 15)
var = StringVar()
var.set('3')
OPTIONS = [
"Russia",
"USA",
"China",
"India",
"Other"
] #etc

#setting the window,font as well as setting variables for dropdowm,radiobutton etc

variable23 = StringVar(ws)
variable23.set(OPTIONS[0]) # default value
variable23.set("")


variable = StringVar()
#submit if data is not repeated and everything is entered
def submit():
    if (var.get()=='3' or 
       register_email.get()=='' or 
       register_name.get()=='' or
       register_mobile.get()=='' or
       register_pwd.get()==''
       or pwd_again.get()==''):
       #print("some value is missing")
       readOnlyText.configure(state='normal')
       readOnlyText.delete("1.0","end")
       readOnlyText.insert(1.0,"Some value is missing")
       readOnlyText.configure(state='disabled')
       
    elif(register_pwd.get()!=pwd_again.get()):
       #print("Password and reentered password don't match")
       readOnlyText.configure(state='normal')
       readOnlyText.delete("1.0","end")
       readOnlyText.insert(1.0,"Password and reentered password don't match")
       readOnlyText.configure(state='disabled')
    else:
       name= register_name.get()
       email= register_email.get()
       password= register_pwd.get()
       mobile= register_mobile.get()
       gender=var.get()
       country=variable23.get()
       passwd = password.encode('utf-8')
       salt = bcrypt.gensalt()
       hashed = bcrypt.hashpw(passwd, salt)
       sqliteConnection = sqlite3.connect('Username_password_test.db')
       #sqlite_insert_query="insert into Username_password (name,email,mobile,password,gender,country,hashedpassword) values(?,?,?,?,?,?,?)",
       #(name,email,mobile,password,gender,country,hashed)
       cursor = sqliteConnection.cursor()
       cursor.execute("SELECT hashedpassword FROM Username_password WHERE name=?", (email,))
       record=cursor.fetchall()
       record=str(record)
       if record!='[]':
            print("sdsds")
            readOnlyText.configure(state='normal')
            readOnlyText.delete("1.0","end")
            readOnlyText.insert(1.0,"Email already exists")
            readOnlyText.configure(state='disabled') 
            cursor.close()
       else:     
        cursor.execute("insert into Username_password (name,email,mobile,password,gender,country,hashedpassword) values(?,?,?,?,?,?,?)",
        (name,email,mobile,password,gender,country,hashed))
       #cursor.execute(sqlite_insert_query)
        sqliteConnection.commit()
        cursor.close()
        #print(hashed)
        #print(passwd)
        clear()    
        readOnlyText.configure(state='normal')
        readOnlyText.delete("1.0","end")
        readOnlyText.insert(1.0,"Data was inputted succesfully")
        readOnlyText.configure(state='disabled')
       #print("submitted")
#clear everything        
def clear():
    #print("clear")
    register_email.delete(0,END)
    register_name.delete(0,END)
    register_pwd.delete(0,END)
    pwd_again.delete(0,END)
    register_mobile.delete(0,END)
    var.set("3")
    variable23.set("")
    readOnlyText.configure(state='normal')
    readOnlyText.delete("1.0","end")
    readOnlyText.insert(1.0,"Data was cleared")
    readOnlyText.configure(state='disabled')
    #print("submitted")
right_frame = Frame(
    ws, 
    bd=2, 
    bg='yellow',
    relief=SOLID, 
    padx=10, 
    pady=10
    )


Label(
    right_frame, 
    text="Enter Name", 
    bg='white',
    font=f
    ).grid(row=0, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Email", 
    bg='white',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Contact Number", 
    bg='white',
    font=f
    ).grid(row=2, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Gender", 
    bg='white',
    font=f
    ).grid(row=3, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Select Country", 
    bg='white',
    font=f
    ).grid(row=4, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Enter Password", 
    bg='white',
    font=f
    ).grid(row=5, column=0, sticky=W, pady=10)

Label(
    right_frame, 
    text="Re-Enter Password", 
    bg='white',
    font=f
    ).grid(row=6, column=0, sticky=W, pady=10)

gender_frame = LabelFrame(
    right_frame,
    bg='white',
    padx=10, 
    pady=10,
    )

readOnlyText =Text(ws,height=2,width=60)
readOnlyText.insert(1.0,"Enter the corresponding inputs")
readOnlyText.configure(state='disabled')

#readOnlyText.pack()
register_name = Entry(
    right_frame, 
    font=f
    )

register_email = Entry(
    right_frame, 
    font=f
    )

register_mobile = Entry(
    right_frame, 
    font=f
    )


male_rb = Radiobutton(
    gender_frame, 
    text='Male',
    bg='white',
    variable=var,
    value='male',
    font=('Times', 10),
    
)

female_rb = Radiobutton(
    gender_frame,
    text='Female',
    bg='white',
    variable=var,
    value='female',
    font=('Times', 10),
  
)

others_rb = Radiobutton(
    gender_frame,
    text='Others',
    bg='white',
    variable=var,
    value='others',
    font=('Times', 10)
   
)

w = OptionMenu(right_frame, variable23, *OPTIONS)


register_pwd = Entry(
    right_frame, 
    font=f,
    show='*'
)
pwd_again = Entry(
    right_frame, 
    font=f,
    show='*'
)

register_btn = Button(
    right_frame, 
    width=15, 
    text='Register', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=submit
)
clear_btn = Button(
    right_frame, 
    width=15, 
    text='Clear', 
    font=f, 
    relief=SOLID,
    cursor='hand2',
    command=clear
)



register_name.grid(row=0, column=1, pady=10, padx=20)
register_email.grid(row=1, column=1, pady=10, padx=20) 
register_mobile.grid(row=2, column=1, pady=10, padx=20)
w.grid(row=4, column=1, pady=10, padx=20)
register_pwd.grid(row=5, column=1, pady=10, padx=20)
pwd_again.grid(row=6, column=1, pady=10, padx=20)
register_btn.grid(row=7, column=1, pady=10, padx=20)
clear_btn.grid(row=7, column=0, pady=10, padx=20)
#readOnlyText.grid(row=8,  pady=10, padx=20)
right_frame.pack()



gender_frame.grid(row=3, column=1, pady=10, padx=20)
male_rb.pack(expand=True, side=LEFT)
female_rb.pack(expand=True, side=LEFT)
others_rb.pack(expand=True, side=LEFT)
def on_enter_register(e):
    register_btn['background'] = 'green'

def on_leave_register(e):
   register_btn['background'] = 'SystemButtonFace'


register_btn.bind("<Enter>", on_enter_register)
register_btn.bind("<Leave>", on_leave_register)
#for hover effects
def on_enter_clear(e):
    clear_btn['background'] = 'green'

def on_leave_clear(e):
   clear_btn['background'] = 'SystemButtonFace'
readOnlyText.pack()
clear_btn.bind("<Enter>", on_enter_clear)
clear_btn.bind("<Leave>", on_leave_clear)
ws.mainloop()