from os import read
import tkinter as tk
from tkinter import messagebox as msg,filedialog as fd
from PIL import Image

def upload_file():
    global finalized
    try:
        logo = fd.askopenfile()
        #the image file uploaded from filedialog can be extracted using img.name
        save_as,ext = logo.name.split('.')  #we dont need an extension to be saved as filename
        if ext.lower() in ['jpg','jpeg','png','tif','bmp']: #valid image extensions supported by cv2
            img = Image.open(logo.name)
            finalized = img.resize((180,180))
        else:
            msg.showerror('INVALID',"Select Valid Logo")
    except ValueError:
        msg.showerror("Invalid","Select Valid Logo")

def upload_file1():
    global img
    try:
        image = fd.askopenfile()
        save_as,ext = image.name.split('.')
        if ext.lower() in ['jpeg','png','tif','bmp']:
            img = Image.open(image.name)
        else:
            msg.showerror('INVALID',"Select Valid Image")
    except ValueError:
        msg.showerror("Invalid","Select Valid Image")

def save():
    try:
        img.paste(finalized,(0, 0))
        output = name.get()
        if len(output) == 0:
            msg.showerror("Invalid","Enter Name")
        else:
            if output[-4:] in ['.png','.jpeg','.bmp','.tiff']:
                pass
            elif output[-4:0] == '.jpg':
                output = output[-4:0]+'.jpeg'
            else:
                output = output+'.png'
            img.save(output)
            msg.showinfo("Downloaded","Image Saved")
    except NameError:
        msg.showerror("Invalid","Select Image and Logo First")
    except TypeError:
        msg.showerror("File Unknown","Select Valid Image first")

def main(screen):
    screen.geometry("435x435+150+180")
    screen.title("Logo Addition")
    canva = tk.Canvas(screen,bg="violet",bd=5)
    canva.pack(expand=True, fill= "both")
    screen.resizable(False,False) # in order to maintain fixed size of screen
    head = tk.Label(screen,text="Add Logo on Image",font=("arial",15,"bold"),fg="black",bg="white").place(x=125,y=5)

    frame = tk.LabelFrame(screen,bg="purple").place(x=50,y=90,width=330,height=290)

    upload_logo = tk.Button(screen,text="Select Logo",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=upload_file).place(x=128,y=125,width=190,height=50)
    upload_image = tk.Button(screen,text="Select Image",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=upload_file1).place(x=128,y=195,width=190,height=50)

    lbl = tk.Label(screen,text="Save File As:",font=("arial",14,"bold"),fg="black",bg="white").place(x=65,y=270)

    global name
    name=tk.Entry(screen,bg="pink",fg="black",font=('arial',13,"bold"),bd=5)
    name.place(x=190,y=265,width=180,height=40)

    download = tk.Button(screen,text="Download",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=save).place(x=105,y=320,width=230,height=40)

    screen.mainloop()

if __name__ == '__main__':
   main()
