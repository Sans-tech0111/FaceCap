from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
top = Tk()
top.geometry('900x500+300+180')
top.title('Login')
top.configure(bg='#fff')
top.resizable(False,False)

img = Image.open('login.png')
img = img.resize((500,500))
img = ImageTk.PhotoImage(img)

Label(top,image=img,bg='white').place(x=10,y=10)
frame = Frame(top,width=400,height=400,bg='white')
frame.place(x=450,y=50)
head = Label(frame,text='Sign In',font=('Microsoft YaHei UI Light',20,'bold'),bg='white',fg='#4e8df2')
head.place(anchor='n',y=20,x=22,relx=0.5)

user = Entry(frame,bg='white',width=35,border=0,font=('Microsoft YaHei UI Light',12))
user.place(x=100,y=100)
user.insert(0,'Username')
Frame(frame,width=295,height=1,bg='black').place(x=90,y=130)

code = Entry(frame,bg='white',width=35,border=0,font=('Microsoft YaHei UI Light',12))
code.place(x=100,y=160)
code.insert(0,'Password')
Frame(frame,width=295,height=1,bg='black').place(x=90,y=190)

Button(frame,text='Sign In',width=25,relief='flat',font=('Microsoft YaHei UI Light',11,'bold'),bg='#4e8df2',fg='white',cursor='hand2').place(x=100,y=220)

Label(frame,text="Don't have an acoount?",font=('Microsoft YaHei UI Light',9),bg='white',fg='black').place(x=120,y=290)

sign_up = Button(frame,text='Sign Up',border=0,bg='white',fg='#4e8df2',font=('Microsoft YaHei UI Light',9),cursor='hand2')
sign_up.place(x=260,y=290)

top.mainloop()
