from os import read
import tkinter as tk
from tkinter import messagebox as msg,filedialog as fd
import PyPDF2

def upload_file():
    global reader1
    try:
        pdf1 = fd.askopenfile()
        #the image file uploaded from filedialog can be extracted using img.name
        save_as,ext = pdf1.name.split('.')  #we dont need an extension to be saved as filename
        if ext.lower() == 'pdf': #valid image extensions supported by cv2
            file = open(pdf1.name,'rb')
            reader1 = PyPDF2.PdfFileReader(file)
        else:
            msg.showerror('INVALID',"Select Valid PDF")
    except ValueError:
        msg.showerror("Invalid","Select Valid PDF")

def upload_file1():
    global reader2
    try:
        pdf2 = fd.askopenfile()
        save_as,ext = pdf2.name.split('.')
        if ext.lower() == 'pdf':
            file = open(pdf2.name,'rb')
            reader2 = PyPDF2.PdfFileReader(file)
        else:
            msg.showerror('INVALID',"Select Valid PDF")
    except ValueError:
        msg.showerror("Invalid","Select Valid PDF")

def mergeing():
    try:
        writer = PyPDF2.PdfFileWriter()
        for i in range(reader1.numPages):
            writer.addPage(reader1.getPage(i))
        for j in range(reader2.numPages):
            writer.addPage(reader2.getPage(j))
        if len(name.get()) == 0:
            msg.showerror("Invalid","Enter File Name")
        else:
            output = name.get()
            if output[-4:] == '.pdf':
                pass
            else:
                output = output+'.pdf'

            output_file = open(output,'wb')
            writer.write(output_file)
            msg.showinfo("Merge Successful","PDF Saved")

    except NameError:
        msg.showerror("Invalid","Select PDF First")
    except TypeError:
        msg.showerror("File Unknown","Select Valid PDF first")


def main(screen):
    screen.geometry("435x435+150+180")
    screen.title("Merge Automate")
    canva = tk.Canvas(screen,bg="yellow",bd=5)
    canva.pack(expand=True, fill= "both")
    screen.resizable(False,False) # in order to maintain fixed size of screen
    head = tk.Label(screen,text="Merge Two PDF's",font=("arial",15,"bold"),fg="black",bg="white").place(x=125,y=5)

    frame = tk.LabelFrame(screen,bg="red").place(x=50,y=90,width=330,height=290)

    upload = tk.Button(screen,text="Upload PDF1",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=upload_file).place(x=128,y=125,width=190,height=50)
    upload1 = tk.Button(screen,text="Upload PDF2",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=upload_file1).place(x=128,y=195,width=190,height=50)

    lbl = tk.Label(screen,text="Save File As:",font=("arial",14,"bold"),fg="black",bg="white").place(x=65,y=270)

    global name
    name=tk.Entry(screen,bg="yellow",fg="black",font=('arial',13,"bold"),bd=5)
    name.place(x=190,y=265,width=180,height=40)

    save = tk.Button(screen,text="Complete Merge",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=mergeing).place(x=105,y=320,width=230,height=40)

    screen.mainloop()

if __name__ == '__main__':
   main()
