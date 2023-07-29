# PassGenerator: a free tool for produce strong password
# Author : zinfopro
# Gmail : akbarizinfo.pro@gmail.com


from tkinter import *
import random
import string
from tkinter import messagebox
import pyperclip


# ----------------------------------functions-------------------------------

# used to generate password-return a string
def generate_password():
    output_str = []
    noDigit = 0
    output_converted_str = ""
    char_choice_start = 1
    char_choice_boundry = 5
    if CHECKASCII.get() == 1 and CHECKDIGIT.get() == 0 and CHECKPUNC.get() == 0:
        char_choice_boundry = 3
    elif CHECKASCII.get() and CHECKDIGIT.get() and not CHECKPUNC.get():
        char_choice_boundry = 4
    elif CHECKASCII.get() and CHECKDIGIT.get() and CHECKPUNC.get():
        char_choice_boundry = 5
    elif CHECKASCII.get() and not CHECKDIGIT.get() and CHECKPUNC.get():
        char_choice_boundry = 4
        noDigit = 1
    elif not CHECKASCII.get() and CHECKDIGIT.get() and CHECKPUNC.get():
        char_choice_start = 3
    elif not CHECKASCII.get() and CHECKDIGIT.get() and not CHECKPUNC.get():
        char_choice_boundry = 4
        char_choice_start = 3
        noDigit = 0
    elif not CHECKASCII.get() and not CHECKDIGIT.get() and CHECKPUNC.get():
        char_choice_boundry = 5
        char_choice_start = 3
        noDigit = 1
    for item in range(1, 9):
        char_choice = random.choice(range(char_choice_start, char_choice_boundry))
        if char_choice == 1:
            output_char = random.choice(string.ascii_lowercase)
            output_str.append(output_char)
        elif char_choice == 2:
            output_char = random.choice(string.ascii_uppercase)
            output_str.append(output_char)
        elif char_choice == 3:
            if noDigit:
                output_char = random.choice(string.punctuation)
                output_str.append(output_char)
            else:
                output_char = random.choice(string.digits)
                output_str.append(output_char)
        else:
            output_char = random.choice(string.punctuation)
            output_str.append(output_char)
    for i in output_str:
        output_converted_str += i
    return output_converted_str


# This function called when "Generate Password" button clicked
def generate():
    if not CHECKASCII.get() and not CHECKDIGIT.get() and not CHECKPUNC.get():
        messagebox.showinfo("Alert", "Please select which option can be used")
        return
    generatedPass = generate_password()
    PASSWORD.set(generatedPass)
    for widget in frmMiddlePart.winfo_children():
        widget.destroy()
    lblMiddlePart = Label(frmMiddlePart, text=PASSWORD.get(), bg="green", font=45)
    lblMiddlePart.pack(side=TOP, pady=30, padx=10)


# This function called when "Copy Password" button clicked
def copy(password):
    if password != "":
        try:
            pyperclip.copy(password)
            messagebox.showinfo("Done!", "Password copied into your clipboard successfully")
        except:
            messagebox.showinfo("Error", "An error occurred")
    else:
        messagebox.showinfo("Attention", "You must first click on Create Password button")


# ----------------------------------tkinter-------------------------------

root = Tk()
root.title("Password Generator")
root.geometry("500x440")
root.resizable(width=False, height=False)
PASSWORD = StringVar()
CHECKASCII = IntVar()
CHECKDIGIT = IntVar()
CHECKPUNC = IntVar()

# ----------------------------------frames-------------------------------

frmTopPart = Frame(root, width=500, height=110)
frmTopPart.pack(side=TOP)

frmMiddlePart = Frame(root, width=500, height=110)
frmMiddlePart.pack(side=TOP)

frmMiddle2Part = Frame(root, width=500, height=110)
frmMiddle2Part.pack(side=TOP)

frmBottomPart = Frame(root, width=500, height=110)
frmBottomPart.pack(side=TOP)

# ----------------------------------frmTopPart-------------------------------

lblTopPart = Label(frmTopPart, text="Password Generator", font=30)
lblTopPart.pack(side=TOP, padx=40, pady=40)

# ------------------------frmMiddlePart-------------------------------

lblMiddlePart = Label(frmMiddlePart, text="Click on Generate button to get password", bg="red")
lblMiddlePart.pack(side=TOP, pady=30, padx=10)

# ----------------------------------frmMiddle2Part-------------------------------

lblMiddle2Part = Label(frmMiddle2Part, text="Select which option can use for produce password")
lblMiddle2Part.pack(side=TOP, padx=1, pady=1)
chBtnAscii = Checkbutton(frmMiddle2Part, text="Ascii characters", variable=CHECKASCII, onvalue=1, offvalue=0, height=2,
                         width=10)
chBtnAscii.pack(side=LEFT, pady=1, padx=1)
chBtnDigit = Checkbutton(frmMiddle2Part, text="Digits", variable=CHECKDIGIT, onvalue=2, offvalue=0, height=2,
                         width=10)
chBtnDigit.pack(side=LEFT, pady=1, padx=1)
chBtnPunc = Checkbutton(frmMiddle2Part, text="Punctuation", variable=CHECKPUNC, onvalue=3, offvalue=0, height=2,
                        width=10)
chBtnPunc.pack(side=LEFT, pady=1, padx=1)

btnGenerate = Button(frmBottomPart, text="Generate", width=15, command=lambda: generate(), bg="pink")
btnGenerate.pack(side=LEFT, pady=40, padx=15)

btnCopy = Button(frmBottomPart, text="Copy password", width=15, command=lambda: copy(PASSWORD.get()), bg="pink")
btnCopy.pack(side=LEFT, pady=40, padx=15)

root.mainloop()
