import tkinter as tk

def take():
    from subprocess import call
    call(['python','faceAttendance.py'])

def show():
    from subprocess import call
    call(['python','showAttendance.py'])

top = tk.Tk()
top.geometry("400x400+550+200")
top.title("Attendance System")
top.configure(background='#27ba7a')
l = tk.Label(top,text="",font=('Century',15,'bold'),fg='white',bg='#1e1f1e',height=16,width=27)
l.place(relx=0.5,rely=0.5,anchor='center')
ll = tk.Label(top,text="Face Recognition Attendance System",font=('Century',15,'bold'),fg='white',bg='black',height=2)
ll.place(relx=0.5,y=10,anchor='n')

b1 = tk.Button(top,text="Take Attendance",font=('Century',15),relief='flat',bg='#1b7d53',fg='snow',width=15,command=take)
b1.place(relx=0.5,rely=0.40,anchor='center')
b2 = tk.Button(top,text="Show Attendance",font=('Century',15),relief='flat',bg='#1b7d53',fg='snow',width=15,command=show)
b2.place(relx=0.5,rely=0.55,anchor='center')

top.mainloop()