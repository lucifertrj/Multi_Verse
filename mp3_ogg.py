"""
For saved file check the location of parent directory
"""
from pydub import AudioSegment
import tkinter as tk
from tkinter import filedialog,messagebox

def initial():
    global save_as
    music = filedialog.askopenfile()
    save_as,ext = music.name.split('.')   #we dont need an extension to be saved as filename
    if ext=='mp3':
        return save_as
    messagebox.showerror("File not recognised","Select MP3 file only")

def convert_img():
    try:
        #AudioSegment.from_mp3("{}.mp3").export('convertedfile.wav',format="wav")
        AudioSegment.from_mp3("{}.mp3".format(save_as)).export('{}.ogg'.format(save_as),format="ogg")
        messagebox.showinfo("Success","File Saved")
    except NameError:
        messagebox.showerror("File Unknown","Select Music File first")
    except TypeError:
         messagebox.showerror("File Unknown","Select Valid Music File")

def main(screen1):
    screen1.geometry("435x435+150+180")
    screen1.title("Music .ext Conversion")
    canva = tk.Canvas(screen1,bg="green",bd=5)
    canva.pack(expand=True, fill= "both")
    screen1.resizable(False,False)
    head = tk.Label(screen1,text="Convert Audio File",font=("arial",20,"bold"),fg="black",bg="grey")
    head.place(x=85,y=15)
    frame = tk.LabelFrame(screen1,bg="chocolate").place(x=50,y=90,width=330,height=280)
    select = tk.Label(screen1,text="Select a MP3 Song",font=("arial",16,"bold"),fg="white",bg="black").place(x=92,y=120)
    convert = tk.Label(screen1,text="Download OGG Form",font=("arial",16,"bold"),bg="white",fg="black").place(x=90,y=240)

    anime = tk.Button(screen1,text=".MP3",font=("arial",14,"bold"),bg="blue",fg="white",bd=5,command=initial)
    anime.place(x=128,y=160,width=170,height=50)

    manga = tk.Button(screen1,text=".OGG",bg="blue",fg="white",font=("arial",14,"bold"),bd=5,command=convert_img)
    manga.place(x=130,y=285,width=170,height=50)
    screen1.mainloop()

if __name__ == '__main__':
    main()
