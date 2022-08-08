import tkinter as tk
from tkinter import messagebox as msg,filedialog as fd
import cv2
import random,string

def upload_file():
    global image
    try:
        img = fd.askopenfile()
        #the image file uploaded from filedialog can be extracted using img.name
        save_as,ext = img.name.split('.')  #we dont need an extension to be saved as filename
        if ext.lower() in ['png','jpg','jpeg','bmp','tiff']: #valid image extensions supported by cv2
            image = cv2.imread(img.name)
            h,w = image.shape[:2] #separate image width and height
            width_value.set(w)
            height_value.set(h)
        else:
            msg.showerror('INVALID',"Select Valid Image")
    except ValueError:
        msg.showerror("Invalid","Select Valid Image")

def resized():
    try:
        #check different possibilities of weight and height
        #make sure user enters valid width and height
        #make sure the width and height is a number
        if len(str(width_value.get())) <=1 or len(str(height_value.get()))<=1:
            msg.showerror("Unknown Value","Enter Valid Width and Height")
        elif str(width_value.get()).isalpha() or str(height_value.get()).isalpha():
            msg.showerror("Invalid","Enter Valid Height and width")
        elif width_value.get() not in range(32,1510):
            msg.showerror("Invalid","Enter Width in Range(32-1510)")
        elif height_value.get() not in range(32,1200):
            msg.showerror("Invalid","Enter height in Range(32-1200)")
        else:
            code=[random.choice(string.ascii_letters+string.digits+string.punctuation) for i in range(12)]
            random.shuffle(code)
            resizeImg = cv2.resize(image, (width_value.get(),height_value.get()))
            cv2.imwrite('resized_img{}.png'.format(''.join(code)),resizeImg)
            msg.showinfo('Success','File Saved')
            width_entry.delete(0,'end')
            height_entry.delete(0,'end')
            cv2.waitKey(0)
            cv2.destroyAllWindows()
    except NameError:
        msg.showerror("Invalid","Select Image First")
    except TypeError:
        msg.showerror("File Unknown","Select Valid Image first")

def main(screen):
    screen.geometry("435x435+150+180")
    screen.title("Resize Image")
    canva = tk.Canvas(screen,bg="orange",bd=5)
    canva.pack(expand=True, fill= "both")
    screen.resizable(False,False) # in order to maintain fixed size of screen
    head = tk.Label(screen,text="Resize Image Locally",font=("arial",15,"bold"),fg="black",bg="white").place(x=125,y=5)

    frame = tk.LabelFrame(screen,bg="gold").place(x=50,y=90,width=330,height=290)
    select = tk.Label(screen,text="Select Image",font=("arial",15,"bold"),fg="white",bg="black").place(x=150,y=105)

    upload = tk.Button(screen,text="Upload File",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=upload_file).place(x=128,y=145,width=170,height=50)

    global width_value,height_value
    width_value = tk.IntVar()
    height_value = tk.IntVar()
    width_value.set('')
    height_value.set('')

    width = tk.Label(screen,text="Enter Width",font=("arial",14,"bold"),fg="black",bg="white").place(x=70,y=230)
    height = tk.Label(screen,text="Enter Height",font=("arial",14,"bold"),fg="black",bg="white").place(x=68,y=275)

    global width_entry,height_entry
    width_entry=tk.Entry(screen,textvariable=width_value,bg="white",fg="black",font=('arial',13,"bold"),bd=5)
    width_entry.place(x=185,y=220,width=150,height=40)
    height_entry=tk.Entry(screen,textvariable=height_value,bg="white",fg="black",font=('arial',13,"bold"),bd=5)
    height_entry.place(x=185,y=265,width=150,height=40)

    save = tk.Button(screen,text="Download Resized Image",font=("arial",13,"bold"),bg="blue",fg="white",bd=5,command=resized).place(x=105,y=320,width=230,height=40)

    screen.mainloop()

if __name__ == '__main__':
    main()

