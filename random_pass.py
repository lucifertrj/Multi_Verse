'''

author: Tarun R Jain
complete content is my own
github: github.com/lucifertrj

'''

#read comments to follow, Thank you -TRJ
import random,string
import tkinter as tk
from tkinter import messagebox as mb

def random_password():
    letters=[random.choice(string.ascii_letters) for letter in range(8)]  #list of random 8 letters(both uppercase and lowercase included)
    numbers=[random.choice(string.digits) for digit in range(3)] #list of random 3 numbers from 0-9
    character=[random.choice(string.punctuation) for symbols in range(3)] #list of 3 random punctuation
    password=letters+character+numbers
    random.shuffle(password) #dont return this statement inside return block, as random.shuffle returns none
    return(password) #the password is shuffled

def get_otp():
    otp = [random.choice(string.digits) for show in range(4)]
    random.shuffle(otp)
    return otp

def generate():
    username=name_var.get()
    if username=='': #empty name will rise a error
        mb.askretrycancel("Error occured","User not recognized")
    elif len(username)<=3: #a valid username consists of atleast 4 or 5 minimum characters
        mb.askretrycancel("Invalid Entry","Please enter a proper name")
    elif username[0] in string.digits:
        mb.askretrycancel("Alert","Dont play with me, enter valid name")
    else:
        while True:
            password=random_password()
            answer=mb.askquestion(f"{username}'s:Random password",f"{''.join(password)}\nAre you satisfed?").lower()
            if answer.startswith('y'):
                mb._show("Copy The password","Thank You")
                break
            else:
                continue
def otp():
    otp_received = get_otp()
    mb._show("OTP",'{}'.format(''.join(otp_received)))

def main(screen):
    screen.title("Password Generator")
    screen.geometry("435x435+150+180")
    screen.resizable(False,False)

    frame = tk.LabelFrame(screen,bg="black",fg="white").place(x=75,y=100,width=300,height=270)

    title=tk.Label(screen,text="Random Password Generator",font=("Times New Roman",20,"bold")).pack()
    name=tk.Label(screen,text="Name:",bg="black",fg="white",font=("arial",16,"bold")).place(x=100,y=130)
    global name_var

    name_var=tk.StringVar()
    name_entry=tk.Entry(screen,textvariable=name_var,bd=5)
    name_entry.focus_set()
    name_entry.place(x=170,y=120,width=150,height=50)

    button=tk.Button(screen,text="Generate Password",command=generate,font=("arial",14,"bold"),bg="black",fg="white",bd=5).place(x=140,y=220,width=180,height=50)
    button_otp=tk.Button(screen,text="Generate OTP",command=otp,font=("arial",14,"bold"),bg="black",fg="white",bd=5).place(x=140,y=295,width=180,height=50)

    screen.mainloop()


if __name__ == '__main__':
    main()
