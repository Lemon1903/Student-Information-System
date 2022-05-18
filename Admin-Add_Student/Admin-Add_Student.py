
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./assets")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1280x720")
window.configure(bg = "#093545")


canvas = Canvas(
    window,
    bg = "#093545",
    height = 720,
    width = 1280,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_curvy = PhotoImage(
    file=relative_to_assets("curvy.png"))
curvy = canvas.create_image(
    640.0,
    664.0,
    image=image_curvy
)

canvas.create_rectangle(
    0.0,
    0.0,
    293.0,
    720.0,
    fill="#204D5D",
    outline="")

imgQuit = PhotoImage(
    file=relative_to_assets("btnQuit.png"))
btnQuit = Button(
    image=imgQuit,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
btnQuit.place(
    x=41.0,
    y=665.0,
    width=90.0,
    height=27.0
)

imgDelete = PhotoImage(
    file=relative_to_assets("btnDelete.png"))
btnDelete = Button(
    image=imgDelete,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
btnDelete.place(
    x=41.0,
    y=439.0,
    width=212.0,
    height=46.0
)

imgUpdate = PhotoImage(
    file=relative_to_assets("btnUpdate.png"))
btnUpdate = Button(
    image=imgUpdate,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
btnUpdate.place(
    x=41.0,
    y=375.0,
    width=212.0,
    height=46.0
)

imgSearch = PhotoImage(
    file=relative_to_assets("btnSearch.png"))
btnSearch = Button(
    image=imgSearch,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
btnSearch.place(
    x=41.0,
    y=311.0,
    width=212.0,
    height=46.0
)

imgView = PhotoImage(
    file=relative_to_assets("btnView.png"))
btnView = Button(
    image=imgView,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
btnView.place(
    x=41.0,
    y=247.0,
    width=212.0,
    height=46.0
)

imgAdd = PhotoImage(
    file=relative_to_assets("btnAdd.png"))
btnAdd = Button(
    image=imgAdd,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
btnAdd.place(
    x=41.0,
    y=182.0,
    width=212.0,
    height=46.0
)

imgHome = PhotoImage(
    file=relative_to_assets("btnHome.png"))
btnHome = Button(
    image=imgHome,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
btnHome.place(
    x=41.0,
    y=37.0,
    width=90.0,
    height=27.0
)

canvas.create_text(
    116.0,
    139.0,
    anchor="nw",
    text="MENU",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 20 * -1)
)

canvas.create_text(
    355.0,
    35.0,
    anchor="nw",
    text="Add student",
    fill="#FFFFFF",
    font=("LexendDeca Light", 36 * -1)
)

imgStuNum = PhotoImage(
    file=relative_to_assets("entry_StuNum.png"))
imgStuNum_bg = canvas.create_image(
    465.0,
    215.5,
    image=imgStuNum
)
entry_StuNum = Entry(
    bd=0,
    bg="#224957",
    highlightthickness=0
)
entry_StuNum.place(
    x=325.0,
    y=193.0,
    width=280.0,
    height=43.0
)

canvas.create_text(
    316.0,
    171.0,
    anchor="nw",
    text="Student number",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 14 * -1)
)

imgLastN = PhotoImage(
    file=relative_to_assets("entry_LastN.png"))
imgLastN_bg = canvas.create_image(
    465.0,
    327.5,
    image=imgLastN
)
entry_LastN = Entry(
    bd=0,
    bg="#224957",
    highlightthickness=0
)
entry_LastN.place(
    x=325.0,
    y=305.0,
    width=280.0,
    height=43.0
)

canvas.create_text(
    316.0,
    285.0,
    anchor="nw",
    text="Last name",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 14 * -1)
)

imgEmail = PhotoImage(
    file=relative_to_assets("entry_email.png"))
imgEmail_bg = canvas.create_image(
    465.0,
    439.5,
    image=imgEmail
)
entry_Email = Entry(
    bd=0,
    bg="#224957",
    highlightthickness=0
)
entry_Email.place(
    x=325.0,
    y=417.0,
    width=280.0,
    height=43.0
)

canvas.create_text(
    316.0,
    397.0,
    anchor="nw",
    text="Email Address",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 14 * -1)
)

imgContNum = PhotoImage(
    file=relative_to_assets("entry_ContNum.png"))
imgContNum_bg = canvas.create_image(
    465.0,
    551.5,
    image=imgContNum
)
entry_ContNum = Entry(
    bd=0,
    bg="#224957",
    highlightthickness=0
)
entry_ContNum.place(
    x=325.0,
    y=529.0,
    width=280.0,
    height=43.0
)

canvas.create_text(
    315.0,
    509.0,
    anchor="nw",
    text="Contact Number",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 14 * -1)
)

imgFirstN = PhotoImage(
    file=relative_to_assets("entry_FirstN.png"))
imgFirstN_bg = canvas.create_image(
    785.0,
    327.5,
    image=imgFirstN
)
entry_FirstN = Entry(
    bd=0,
    bg="#224957",
    highlightthickness=0
)
entry_FirstN.place(
    x=645.0,
    y=305.0,
    width=280.0,
    height=43.0
)

canvas.create_text(
    635.0,
    285.0,
    anchor="nw",
    text="First name",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 14 * -1)
)

imgMiddleN = PhotoImage(
    file=relative_to_assets("entry_MiddleN.png"))
imgMiddleN_bg = canvas.create_image(
    1104.0,
    327.5,
    image=imgMiddleN
)
entry_MiddleN = Entry(
    bd=0,
    bg="#224957",
    highlightthickness=0
)
entry_MiddleN.place(
    x=964.0,
    y=305.0,
    width=280.0,
    height=43.0
)

canvas.create_text(
    954.0,
    285.0,
    anchor="nw",
    text="Middle name",
    fill="#FFFFFF",
    font=("LexendDeca Regular", 14 * -1)
)
window.resizable(False, False)
window.mainloop()
