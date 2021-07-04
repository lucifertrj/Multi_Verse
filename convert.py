"""
For saved image check the folder in which image was located
"""
import cv2
import tkinter as tk
from tkinter import filedialog,messagebox

def initial():
    global img_file,save_as
    try:
        img = filedialog.askopenfile()
        save_as,ext = img.name.split('.')   #we dont need an extension to be saved as filename
        if ext.upper() in options:
            img_file = cv2.imread(img.name)
            return save_as
        messagebox.showerror("Invalid","Select a valid file")
    except ValueError:
        messagebox.showerror("Invalid","Select a valid file")

def convert_img():
    try:
        cv2.imwrite("{}.{}".format(save_as,choice.get().lower()),img_file)
        messagebox.showinfo("Success","File saved")
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    except NameError:
        messagebox.showerror("File Unknown","Select Image first")
    except TypeError:  #make sures whether image is choose first before downloading
         messagebox.showerror("File Unknown","Select Valid Image first")

def main(screen):
    screen.geometry("425x425+150+180")
    screen.title("Convert Image")
    canva = tk.Canvas(screen,bg="black",bd=5)
    canva.pack(expand=True, fill= "both")
    screen.minsize(425,425)
    screen.maxsize(425,425)
    head = tk.Label(screen,text="Change Image .ext without help of Internet",font=("arial",15,"bold"),fg="black",bg="grey")
    head.place(x=6,y=15)
    frame = tk.LabelFrame(screen,bg="gray").place(x=50,y=90,width=330,height=280)
   #uploading UI
    select = tk.Label(screen,text="Select Image",font=("arial",16,"bold"),fg="white",bg="black").place(x=92,y=120)

    select_image = tk.Button(screen,text="Upload File",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=initial)
    select_image.place(x=128,y=160,width=170,height=50)

    global options,choice
    options="jpg jpeg tiff png bmp".upper().split()
    choice = tk.StringVar()
    choice.set('PNG')
    output = tk.Label(screen,text="Choose Type ==>",font=("arial",16,"bold"),fg="white",bg="black").place(x=90,y=240)

    drop = tk.OptionMenu(screen,choice, *options)
    drop.configure(bg="red",fg="white",activebackground="blue",font=("arial",14,"bold"))
    drop.place(x=280,y=235)

    save_image = tk.Button(screen,text="Download",bg="blue",fg="white",font=("arial",14,"bold"),bd=5,command=convert_img)
    save_image.place(x=130,y=285,width=170,height=50)

    screen.mainloop()

if __name__ == '__main__':
    main()
