"""
For saved file check the location of parent directory
"""
import cv2
import tkinter as tk
from tkinter import filedialog as fd,messagebox as msg

def initial():
    global image,save_as
    try:
        img = fd.askopenfile()
        #the image file uploaded from filedialog can be extracted using img.name
        save_as,ext = img.name.split('.')  #we dont need an extension to be saved as filename
        if ext.lower() in ['png','jpg','jpeg','bmp','tiff']: #valid image extensions supported by cv2
            image = cv2.imread(img.name)
        else:
            msg.showerror('INVALID',"Select Valid Image")
    except ValueError:
        msg.showerror("Invalid","Select Valid Image")

def convert_img():
    try:
        gray_image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        _,black_white = cv2.threshold(gray_image,127,255,cv2.THRESH_BINARY)
        cv2.imwrite("{}_BW.png".format(save_as),black_white)
        msg.showinfo("Success","File Downloaded")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except NameError:
        msg.showerror("File Unknown","Select Image File first")
    except TypeError:
        msg.showerror("File Unknown","Select Valid Image")

def main(screen1):
    screen1.geometry("435x435+150+180")
    screen1.title("BLACK~WHITE")
    canva = tk.Canvas(screen1,bg="black",bd=5)
    canva.pack(expand=True, fill= "both")
    screen1.resizable(False,False)
    head = tk.Label(screen1,text="Colorful to BW",font=("arial",22,"bold"),fg="black",bg="white")
    head.place(x=105,y=15)
    frame = tk.LabelFrame(screen1,bg="white").place(x=50,y=90,width=330,height=280)
    select = tk.Label(screen1,text="Select Colorful Image",font=("arial",16,"bold"),fg="white",bg="black").place(x=92,y=120)
    convert = tk.Label(screen1,text="Convert into BW Image",font=("arial",16,"bold"),bg="black",fg="white").place(x=90,y=240)

    colorful = tk.Button(screen1,text="Upload File",font=("arial",14,"bold"),bg="black",fg="white",bd=5,command=initial).place(x=128,y=160,width=170,height=50)

    bw = tk.Button(screen1,text="Download",bg="black",fg="white",font=("arial",14,"bold"),bd=5,command=convert_img).place(x=130,y=285,width=170,height=50)
    screen1.mainloop()

if __name__ == '__main__':
    main()