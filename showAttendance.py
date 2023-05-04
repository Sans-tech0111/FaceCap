import tkinter as tk
import csv

filepath = 'Attendance.csv'
file = open(filepath)
Reader = csv.reader(file)
Data = list(Reader)

list1 = []
for x in range(0,len(Data)):
    list1.append([Data[x][0],Data[x][1]])


top = tk.Tk()
top.geometry('300x300+600+250')
top.title('Attendees')
top.configure(background='#27ba7a')
var = tk.StringVar(value = list1)
listbox1 = tk.Listbox(top, listvariable=var,font=('Century',15,'bold'),bg='#1b7d53',fg='snow',relief='flat')
listbox1.place(relx=0.5,rely=0.5,anchor='center')

top.mainloop()