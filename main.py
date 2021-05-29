from tkinter import *
from PIL import Image, ImageTk, ImageDraw, ImageFont
from tkinter import filedialog

filename = None
window = Tk()
window.title("Watermark App")
window.minsize(width=800, height=500)
window.config(bg="#77acf1")

my_label = Label(text="To watermark an image click below to upload a image", font=("Ariel", 24, "bold"), bg="#3edbf0")
my_label.grid()


def open_img():
    # Select the Imagename  from a folder
    x = openfilename()
    # opens the image
    img = Image.open(x)
    # resize the image and apply a high-quality down sampling filter
    img = img.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(window, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=3)

    edit_btn = Button(window, text="Edit", height=1, width=15, bg="#c0fefc", command=edit)
    edit_btn.grid(row=6, columnspan=4)


open_btn = Button(window, text='open image', height=1, width=15, bg="#c0fefc", command=open_img)
open_btn.grid(row=1, columnspan=4)


def openfilename():
    # open file dialog box to select image
    # The dialogue box has a title "Open"
    global filename
    filename = filedialog.askopenfilename(title='"pen')
    return filename


def edit():
    im = Image.open(filename)
    width, height = im.size

    draw = ImageDraw.Draw(im)
    text = "sample watermark"

    font = ImageFont.truetype('arial.ttf', 100)
    textwidth, textheight = draw.textsize(text, font)

    # calculate the x,y coordinates of the text
    margin = 10
    x = width - textwidth - margin
    y = height - textheight - margin

    # draw watermark in the bottom right corner
    draw.text((x, y), text, font=font)
    im.show()

    # Save watermarked image
    im.save('watermark.jpg')

    Label(text="Image After Watermarked", font=("Ariel", 24, "bold"), bg="#3edbf0")
    img = im.resize((250, 250), Image.ANTIALIAS)

    # PhotoImage class is used to add image to widgets, icons etc
    img = ImageTk.PhotoImage(img)

    # create a label
    panel = Label(window, image=img)

    # set the image as img
    panel.image = img
    panel.grid(row=8)



window.mainloop()