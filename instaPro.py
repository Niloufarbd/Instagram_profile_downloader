from tkinter import *
import instaloader
import urllib
from urllib.request import urlopen
from PIL import Image , ImageTk
import io
from tkinter import messagebox
def get_image():
    L = instaloader.Instaloader()
    profile = instaloader.Profile.from_username(L.context, f"{username.get()}")
    urlPro = urlopen(profile.get_profile_pic_url())
    date = urlPro.read()
    urlPro.close()
    image = Image.open(io.BytesIO(date))
    pic = ImageTk.PhotoImage(image)
    label1.config(image=pic)
    label1.image = pic
    label1.place(x=35, y=75)



window = Tk()
window.geometry("600x600")
window.resizable(width=False, height=False)
window.title('Instagram profile downloader')

label = Label(window, text='Enter your instagram username', bg='gray', fg='black')
label.pack()

username = Entry(window, width=50)
username.place(x=145, y=25)

button = Button(window, text='download profile', bg='gray', fg='black')
button.config(command=get_image)
button.place(x=250, y=50)

label1 = Label(window)

window.mainloop()
