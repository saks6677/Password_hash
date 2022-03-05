
from tkinter import *
from tkinter import OptionMenu
import sqlite3
import bcrypt

ws = Tk()
ws.title('Hashed_password_login')
ws.config(bg='black')

f=17



variable = StringVar()
def submit():
    if (
       register_email.get()=='' or 
      
       
       register_pwd.get()==''
       ):
       readOnlyText.configure(state='normal')
       readOnlyText.delete("1.0","end")
       readOnlyText.insert(1.0,"Some value is missing")
       readOnlyText.configure(state='disabled')
       #print("some value is missing")
#After authentication user can create a landing page

    else:
       email=register_email.get()
       password=register_pwd.get()
       print("submitted")
       sqliteConnection = sqlite3.connect('Username_password_test.db')
       cursor = sqliteConnection.cursor()
       #getting hash value
       cursor.execute("SELECT hashedpassword FROM Username_password WHERE email=?", (email,)) #hashed password is fetched
       record=cursor.fetchall()
       cursor.close()
       #print(record)
       record=str(record)
       if record=='[]':
            #print("sdsds")
            readOnlyText.configure(state='normal')
            readOnlyText.delete("1.0","end")
            readOnlyText.insert(1.0,"Email does not exit")
            readOnlyText.configure(state='disabled')
       else:
       
        record=record[4:]
        record=record[:-4]
        print(record)
        record=record.encode()
        print(record)
        password=password.encode()
        #print (password)
        if bcrypt.checkpw(password,record): #bcrypt checkpw for password and hashed password
          #print("match")
          readOnlyText.configure(state='normal')
          readOnlyText.delete("1.0","end")
          readOnlyText.insert(1.0,"Password is correct. Login successful")
          readOnlyText.configure(state='disabled')
        else:
          #print("does not match")
          readOnlyText.configure(state='normal')
          readOnlyText.delete("1.0","end")
          readOnlyText.insert(1.0,"Password is not correct")
          readOnlyText.configure(state='disabled')
        
def clear():
    print("clear")
    register_email.delete(0,END)
    register_pwd.delete(0,END)


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
    text="Enter Email", 
    bg='white',
    font=f
    ).grid(row=1, column=0, sticky=W, pady=10)


Label(
    right_frame, 
    text="Enter Password", 
    bg='white',
    font=f
    ).grid(row=3, column=0, sticky=W, pady=10)


readOnlyText =Text(ws,height=2,width=60)
readOnlyText.insert(1.0,"Enter the corresponding inputs")
readOnlyText.configure(state='disabled')

register_email = Entry(
    right_frame, 
    font=f
    )




register_pwd = Entry(
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



register_email.grid(row=1, column=1, pady=10, padx=20) 


register_pwd.grid(row=3, column=1, pady=10, padx=20)

register_btn.grid(row=5, column=1, pady=10, padx=20)
clear_btn.grid(row=5, column=0, pady=10, padx=20)
right_frame.pack()





def on_enter_register(e):
    register_btn['background'] = 'green'

def on_leave_register(e):
   register_btn['background'] = 'SystemButtonFace'


register_btn.bind("<Enter>", on_enter_register)
register_btn.bind("<Leave>", on_leave_register)
def on_enter_clear(e):
    clear_btn['background'] = 'green'

def on_leave_clear(e):
   clear_btn['background'] = 'SystemButtonFace'


clear_btn.bind("<Enter>", on_enter_clear)
clear_btn.bind("<Leave>", on_leave_clear)
readOnlyText.pack()
ws.mainloop()