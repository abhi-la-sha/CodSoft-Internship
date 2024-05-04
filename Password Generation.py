import random
from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("900x600+40+40")
root.title("Password Generator")

passwords = {}

head_title = Label(root,text="Password Generator", width=27,bg="#D20062",fg="white",
            font=("Arial",20,"bold"), padx=10,pady=10,highlightbackground="black",highlightthickness=1).grid(columnspan=4, pady=20)

def generate():
    try:
        char = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
              'q', 'r','s', 't', 'u', 'v', 'w', 'x', 'y','z',
              'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
              'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
              '0','1','2','3','4','5','6','7','8','9','!','@','#','$','&','*']
        passwd = ""
        get_pass.delete(0,END)
        for i in range(int(get_len.get())):
            passwd += random.choice(char)
        get_pass.insert(0,passwd)

    except:
        if get_len =="":
            messagebox.showwarning("Password length","Please enter valid password length(number)!")
        else:
            messagebox.showinfo("Password generate successfully!")


frame = Frame(root,highlightbackground="black",highlightthickness=1,padx=8,pady=20,bg="#EEEEEE")
frame.grid(column=0,row=1)

pass_len= Label(frame,text="Password_length",font=("Arial",15))
pass_len.grid(column=2,row=0,padx=20)

password= Label(frame,text="Password",font=("Arial",15))
password.grid(column=3,row=0,padx=20)

get_len = Entry(frame, font=("Arial",20),width=5,bg="#C7C8CC")
get_len.grid(column=2,row=1,padx=10,pady=10)

get_pass = Entry(frame, font=("Arial",20),width=15,bg="#C7C8CC")
get_pass.grid(column=3,row=1,padx=20,pady=10)

btn_generate = Button(frame, text="Generate Password",font=("Arial",15,"bold"),bg="#58A399",command=generate)
btn_generate.grid(column=3,row=4,pady=10)

root.mainloop()
