import pyqrcode
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image

root = Tk()

# universal fonts
universal_font = ("Arial", 16, "bold")
bd = 6

img = None

def generate_qr_code():
    global img
    input_user = text_param_input.get()
    print(input_user)

    if not input_user:
        messagebox.showerror("error", "Please enter something to generate qrcode!")
        return

    big_code = pyqrcode.create(input_user, error='L', version=10, mode='binary')
    big_code.png('code.png', scale=6, module_color=[0, 0, 0, 128], background=[0xff, 0xff, 0xcc])
    img = ImageTk.PhotoImage(Image.open("code.png"))

    image_qrcode = Label(root, image=img)
    image_qrcode.grid(row=1, column=0, columnspan=5)

    return


label_texts = Label(root, text="Enter Text or URL", font=universal_font, fg="black")
label_texts.grid(row=0, column=0)


text_param_input = StringVar()
text_input = Entry(root, textvariable=text_param_input, width=40, bd=bd, font=universal_font, fg="black")
text_input.grid(row=0, column=1)


button_qrcode = Button(root, text="Generate", bd=bd, font=("Arial", 10, "bold"), width=20, height=3, command=generate_qr_code)
button_qrcode.grid(row=2, column=0, columnspan=5, pady=20)

# root configurations
root.title("QR Code Generator")
root.resizable(False, False)
root.mainloop()
