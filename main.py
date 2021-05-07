from tkinter import *

from PIL._imaging import convert
from future.moves.tkinter import messagebox

converter = Tk()
converter.title("Temperature Convertor")
converter.geometry("900x500")
converter.config(bg="red")
convert = "none"


def enable_ctf():
    en_CtF.config(state="normal")
    en_CtF.delete(0, END)

    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.config(state="readonly")

    en_FtC.config(state="normal")
    en_FtC.delete(0, END)
    en_FtC.config(state="readonly")

    global convert
    convert = "ctf"


def enable_ftc():
    en_FtC.config(state="normal")
    en_FtC.delete(0, END)

    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.config(state="readonly")

    en_CtF.config(state="normal")
    en_CtF.delete(0, END)
    en_CtF.config(state="readonly")

    global convert
    convert = "ftc"


def cal():
    try:
        global convert
        if convert == "ctf":
            temp = float(en_CtF.get())
            Answer = str(temp * 9 / 5 + 32)
            en_Answer.config(state="normal")
            en_Answer.delete(0, END)
            en_Answer.insert(0, Answer)
            en_Answer.config(state="readonly")
        elif convert == "ftc":
            temp = float(en_FtC.get())
            Answer = str((temp - 32) * 5 / 9)
            en_Answer.config(state="normal")
            en_Answer.delete(0, END)
            en_Answer.insert(0, Answer)
            en_Answer.config(state="readonly")
    except ValueError as ex:
        en_CtF.config(state="normal")
        en_CtF.delete(0, END)
        en_CtF.config(state="readonly")

        en_FtC.config(state="normal")
        en_FtC.delete(0, END)
        en_FtC.config(state="readonly")

        messagebox.showerror("Error", ex)


def clear():
    en_CtF.config(state="normal")
    en_CtF.delete(0, END)
    en_CtF.config(state="readonly")

    en_FtC.config(state="normal")
    en_FtC.delete(0, END)
    en_FtC.config(state="readonly")

    en_Answer.config(state="normal")
    en_Answer.delete(0, END)
    en_Answer.config(state="readonly")


# code start

CtF = LabelFrame(converter, text="Celsius To Fahrenheit", borderwidth=10, font=("Times", 10))
CtF["bg"] = "White"
CtF.place(x=100, y=100, height=100, width=300)

FtC = LabelFrame(converter, text="Fahrenheit To Celsius", borderwidth=10, font=("Times", 10))
FtC["bg"] = "White"
FtC.place(x=500, y=100, height=100, width=300)

en_CtF = Entry(CtF)
en_CtF.place(x=100, y=25, width=100)
en_CtF.config(state="readonly")

en_FtC = Entry(FtC)
en_FtC.place(x=100, y=25, width=100)
en_FtC.config(state="readonly")

btn_CtF = Button(converter, text="Activate - Celsius To Fahrenheit", borderwidth=10, font=("Times", 10))
btn_CtF["bg"] = "White"
btn_CtF["command"] = enable_ctf
btn_CtF.place(x=100, y=250, width=300, height=50)

btn_FtC = Button(converter, text="Activate - Fahrenheit To Celsius", borderwidth=10, font=("Times", 10))
btn_FtC["bg"] = "White"
btn_FtC["command"] = enable_ctf
btn_FtC.place(x=500, y=250, width=300, height=50)

btn_Cal = Button(converter, text="Calculate Conversion", borderwidth=10, font=("Times", 10))
btn_Cal["bg"] = "White"
btn_Cal["command"] = cal
btn_Cal.place(x=100, y=350, width=200)

en_Answer = Entry(converter, text="", bg="white")
en_Answer.place(x=400, y=350, width=200, height=100)
en_Answer.config(state="readonly")

btn_Clear = Button(converter, text="Clear", borderwidth=10, font=("Times", 10))
btn_Clear["bg"] = "White"
btn_Clear["command"] = clear
btn_Clear.place(x=700, y=350, width=100)

btn_Exit = Button(converter, text="Exit Program", borderwidth=10, font=("Times", 10))
btn_Exit["bg"] = "White"
btn_Exit["command"] = exit
btn_Exit.place(x=700, y=400, width=100)

# code end
converter.mainloop()
