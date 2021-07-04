from tkinter import *
import cv2
import os,random,string
from tkinter import messagebox as msg,filedialog as fd
from PIL import Image,ImageTk
import mp3_ogg,resize,convert,merge_2_pdf,random_pass,logo,black_and_white
import pyjokes

class ALL_IN_ONE:
    def __init__(self,parent):
        self._root = parent

    def top_level(self):
        screen = Toplevel(self._root)
        return screen

    def resized(self):
        resize.main(in_one.top_level())

    def mp3_to_ogg(self):
        mp3_ogg.main(in_one.top_level())

    def change(self):
        convert.main(in_one.top_level())

    def merge(self):
        merge_2_pdf.main(in_one.top_level())

    def bw(self):
        black_and_white.main(in_one.top_level())

    def generate(self):
        random_pass.main(in_one.top_level())

    def add_logo(self):
        logo.main(in_one.top_level())

    def joke(self):
        msg.showinfo("Have a Good Day!",pyjokes.get_joke(language='en'))

    def main(self):
        self._root.geometry("1200x680")
        self._root.resizable(False,False)
        self._root.title("Multi-Convertor-Saviour")

        img = Image.open("images/home_page.jpeg")
        img = img.convert("RGBA")
        img = img.resize((590,680), Image.ANTIALIAS)
        bg= ImageTk.PhotoImage(img)

        canvas= Canvas(self._root,bg="skyblue")
        canvas.pack(expand=True, fill= "both")
        canvas.create_image(0,0,image=bg, anchor="nw")

        frame = LabelFrame(text = "CHOOSE YOUR CHOICE",font=("sans",15,"bold"),bg="aqua",fg="black",bd=5)
        frame.place(x=625,y=140,width=545,height=460)

        welcome = Label(self._root,text=" WELCOME USER \n Help Yourself",font=("arial",24,"bold"),fg="black").place(x=155,y=10)

        about = Label(self._root,text="About this Project",font=("arial",20,"bold"),bg="black",fg="white").place(x=780,y=15)

        about_text = Label(self._root,text="One local platform to satisfy multiple remote deeds.",font=("arial",16,"bold"),fg="black",bg="white").place(x=630,y=70)

        btn1 = Button(frame,text="Resize Image",command=self.resized,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=20,y=60,width=150,height=50)
        btn2 = Button(frame,text="MP3 to OGG",command=self.mp3_to_ogg,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=190,y=60,width=150,height=50)
        btn3 = Button(frame,text="RGBA to BW",command=self.bw,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=360,y=60,width=150,height=50)
        btn4 = Button(frame,text="JPG to PNG",command=self.change,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=20,y=140,width=150,height=50)
        btn5 = Button(frame,text="Merge 2 PDF",command=self.merge,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=190,y=140,width=150,height=50)
        btn6 = Button(frame,text="Logo on Image",command=self.add_logo,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=360,y=140,width=150,height=50)
        btn7 = Button(frame,text="Random P-word",command=self.generate,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=20,y=220,width=150,height=50)
        btn8 = Button(frame,text="Watermark on PDF",bd=4,bg="blue",fg="white",font=("arial",12,"bold")).place(x=360,y=220,width=160,height=50)
        btn9 = Button(frame,text="Rotate Image",bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=190,y=220,width=150,height=50)
        btn10 = Button(frame,text="Remove Bg",bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=20,y=300,width=150,height=50)
        btn11 = Button(frame,text="Excel-HTML",bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=360,y=300,width=150,height=50)
        btn12 = Button(frame,text="Coding Jokes",command=self.joke,bd=5,bg="blue",fg="white",font=("arial",12,"bold")).place(x=190,y=300,width=150,height=50)

        creator = Label(self._root,text="Creator: TARUN R JAIN",bg="black",fg="red",font=("arial",16,"bold")).place(x=770,y=630,width=280,height=40)

        self._root.mainloop()

if __name__ == '__main__':
    root = Tk()
    in_one = ALL_IN_ONE(root)
    in_one.main()