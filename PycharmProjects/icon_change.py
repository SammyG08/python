import tkinter
from PIL import Image, ImageTk

screen = tkinter.Tk()

ico = Image.open('icon.png')
photo = ImageTk.PhotoImage(ico)
screen.wm_iconphoto(False, photo)

screen.mainloop()
