from tkinter import *
from tkinter import messagebox
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from tkinter import filedialog
from tkinter.ttk import Combobox


#GUI

window = Tk()
window.title("Watermark")
window.config(padx=20,pady=20)
canvas = Canvas(width=1000,height=1000,highlightthickness=0)



website_label = Label(text='print your watermark text:',font=('courier',10,'bold'))
website_label.grid(column=0,row=1)

website_entry = Entry(width=32)
website_entry.grid(column=1,row=1)
website_entry.focus()


website_label = Label(text='Choose color of watermark',font=('courier',10,'bold'))
website_label.grid(column=0,row=3)



listbox = Combobox(values=["black","white"])

listbox.grid(column=0,row=4)


font_size_label = Label(text='Choose watermark font size',font=('courier',10,'bold'))
font_size = Combobox(values=["10","20", "30", "40", "50", "60","70"])
font_size_label.grid(row=3,column=1)
font_size.grid(row=4,column=1)





l1 = Label(text='Upload File',width=30,font=('courier',10,'bold'))
l1.grid(row=5,column=1)
b1 = Button( text='Upload File and enter',
   width=20,command = lambda:upload_file())
b1.grid(row=6,column=1)



file = Label(text='Print file name:',font=('courier',10,'bold'))
file.grid(column=0,row=2)

file_name = Entry(width=32)
file_name.grid(column=1,row=2)








def upload_file():
    file = filedialog.askopenfilename()
    image = Image.open(f"{file}")
    watermark_image = image.copy()
    website = website_entry.get()
    color = listbox.get()
    file_names = file_name.get()
    font_sizee = font_size.get()
    watermark(watermark_image=watermark_image,text=website,color=color,files_name=file_names,font_size=font_sizee)


def watermark(watermark_image,text,color,files_name, font_size):
    white = (255,255,255)
    black = (0,0,0)
    draw = ImageDraw.Draw(watermark_image)
    font = ImageFont.truetype("arial.ttf", int(font_size))
    if color == "white":
        draw.text((0,0), f"{text}", white, font=font)
        messagebox.showinfo(title="Succesful", message=f"Image with white {font_size} watermark text:{text} succesfuly saved as {files_name}.png ")
    elif color == "black":
        draw.text((0, 0), f"{text}", black, font=font)
        messagebox.showinfo(title="Succesful", message=f"Image with white {font_size} watermark text:{text} succesfuly saved as {files_name}.png ")

    watermark_image.save(f"{files_name}.png")


















window.mainloop()




