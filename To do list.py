from tkinter import *
from tkinter import messagebox
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To Do List')
ws.config(bg='#223441')
ws.resizable(False,False)

frame = Frame(ws)
frame.pack(pady=10)


def AddTask():
    task = my_entry.get()
    if task != "":
        task_list.append(task)
        box.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning", "Please enter a task.")

def DeleteTask():
    task_list.pop()
    box.delete(ANCHOR)
    print(task_list)

box = Listbox(frame,width=25,height=8,font=('Arial', 18),bd=0,fg='#464646',highlightthickness=0,selectbackground='#a6a6a6',activestyle="none",)
box.pack(side=LEFT, fill=BOTH)

task_list = []

for item in task_list:
    box.insert(END, item)

sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)

box.config(yscrollcommand=sb.set)
sb.config(command=box.yview)

my_entry = Entry(ws,font=('Arial', 18))

label_frame= Frame(ws)
label_frame.pack(pady=10)

my_entry.pack(pady=20)

button_frame = Frame(ws)
button_frame.pack(pady=20)

add_label=Label(label_frame,text="Add task:",font=("Arial",15,),bg='#223441')
add_label.pack()

addTask_btn = Button(button_frame,text='Add Task',font=('Arial 14'),bg='#c5f776',padx=20,pady=10,command=AddTask)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(button_frame,text='Delete Task',font=('Arial 14'),bg='#ff8b61',padx=20,pady=10,command=DeleteTask)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()
