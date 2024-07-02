
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sayli Tambe\OneDrive\Desktop\figma\Tkinter-Designer-master (1)\SAY\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1215x812")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 812,
    width = 1215,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1215.0,
    28.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    5.0,
    82.0,
    anchor="nw",
    text="Project",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    5.0,
    312.0,
    anchor="nw",
    text="Settings",
    fill="#000000",
    font=("Inter", 16 * -1)
)

canvas.create_text(
    5.0,
    363.0,
    anchor="nw",
    text="Resolution",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    24.0,
    339.0,
    anchor="nw",
    text="Project",
    fill="#000000",
    font=("Inter", 15 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    131.5,
    499.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=92.0,
    y=489.0,
    width=79.0,
    height=19.0
)

canvas.create_text(
    14.0,
    438.0,
    anchor="nw",
    text="Workpiece",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    13.0,
    396.0,
    anchor="nw",
    text="Units",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    40.0,
    465.0,
    anchor="nw",
    text="Automatic",
    fill="#000000",
    font=("Inter", 15 * -1)
)

canvas.create_text(
    20.0,
    489.0,
    anchor="nw",
    text="Margin",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    40.0,
    534.0,
    anchor="nw",
    text="Manual",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    562.0,
    anchor="nw",
    text="Dimension",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    186.0,
    562.0,
    anchor="nw",
    text="Offset",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    93.5,
    600.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=40.0,
    y=590.0,
    width=107.0,
    height=19.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    215.5,
    600.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=162.0,
    y=590.0,
    width=107.0,
    height=19.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    215.5,
    665.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=162.0,
    y=655.0,
    width=107.0,
    height=19.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    93.5,
    665.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=40.0,
    y=655.0,
    width=107.0,
    height=19.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    215.5,
    632.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=162.0,
    y=622.0,
    width=107.0,
    height=19.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    93.5,
    632.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=40.0,
    y=622.0,
    width=107.0,
    height=19.0
)

canvas.create_text(
    13.0,
    586.0,
    anchor="nw",
    text="X",
    fill="#E71D1D",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    13.0,
    658.0,
    anchor="nw",
    text="Z",
    fill="#4477DB",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    13.0,
    622.0,
    anchor="nw",
    text="Y",
    fill="#1AE446",
    font=("Inter", 14 * -1)
)

canvas.create_rectangle(
    285.0,
    29.0,
    286.0,
    812.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.0,
    307.9466247558594,
    285.99945068359375,
    309.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    70.5,
    348.5,
    286.0,
    349.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    0.5,
    348.5,
    26.0,
    349.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    88.5,
    447.5,
    286.0,
    449.0,
    fill="#000000",
    outline="")

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=75.0,
    y=28.0,
    width=60.0,
    height=17.0
)

canvas.create_rectangle(
    -0.5,
    447.5,
    13.0,
    448.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -1.0,
    524.0,
    286.0,
    525.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    85.5,
    543.4801940917969,
    286.00018310546875,
    544.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    -0.5,
    543.5,
    23.0,
    544.0,
    fill="#000000",
    outline="")

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    138.0,
    371.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=93.0,
    y=363.0,
    width=90.0,
    height=15.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    238.0,
    371.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=193.0,
    y=363.0,
    width=90.0,
    height=15.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    138.0,
    404.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=93.0,
    y=396.0,
    width=90.0,
    height=15.0
)

canvas.create_text(
    529.0,
    1.0,
    anchor="nw",
    text="CAMotics",
    fill="#000000",
    font=("Inter", 22 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=0.0,
    y=28.0,
    width=30.0,
    height=17.0
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=192.0,
    y=27.0,
    width=39.0,
    height=17.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=142.0,
    y=28.0,
    width=38.0,
    height=17.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=32.0,
    y=28.0,
    width=30.0,
    height=17.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=289.0,
    y=84.0,
    width=107.0,
    height=17.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=399.0,
    y=82.0,
    width=77.0,
    height=17.0
)

canvas.create_text(
    171.0,
    492.0,
    anchor="nw",
    text="%\n",
    fill="#000000",
    font=("Inter", 13 * -1)
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=5.0,
    y=48.0,
    width=25.0,
    height=30.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=299.0,
    y=48.0,
    width=30.0,
    height=30.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=201.0,
    y=48.0,
    width=30.0,
    height=30.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=153.0,
    y=51.0,
    width=30.0,
    height=30.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=40.0,
    y=48.0,
    width=30.0,
    height=30.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=347.0,
    y=47.0,
    width=30.0,
    height=30.0
)

button_image_14 = PhotoImage(
    file=relative_to_assets("button_14.png"))
button_14 = Button(
    image=button_image_14,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_14 clicked"),
    relief="flat"
)
button_14.place(
    x=396.0,
    y=47.0,
    width=31.0,
    height=30.0
)

button_image_15 = PhotoImage(
    file=relative_to_assets("button_15.png"))
button_15 = Button(
    image=button_image_15,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_15 clicked"),
    relief="flat"
)
button_15.place(
    x=469.0,
    y=48.0,
    width=30.0,
    height=30.0
)

button_image_16 = PhotoImage(
    file=relative_to_assets("button_16.png"))
button_16 = Button(
    image=button_image_16,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_16 clicked"),
    relief="flat"
)
button_16.place(
    x=986.0,
    y=44.0,
    width=44.0,
    height=33.0
)

button_image_17 = PhotoImage(
    file=relative_to_assets("button_17.png"))
button_17 = Button(
    image=button_image_17,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_17 clicked"),
    relief="flat"
)
button_17.place(
    x=885.0,
    y=38.0,
    width=43.0,
    height=36.0
)

button_image_18 = PhotoImage(
    file=relative_to_assets("button_18.png"))
button_18 = Button(
    image=button_image_18,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_18 clicked"),
    relief="flat"
)
button_18.place(
    x=840.0,
    y=45.0,
    width=32.0,
    height=30.0
)

button_image_19 = PhotoImage(
    file=relative_to_assets("button_19.png"))
button_19 = Button(
    image=button_image_19,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_19 clicked"),
    relief="flat"
)
button_19.place(
    x=789.0,
    y=45.0,
    width=30.0,
    height=29.0
)

button_image_20 = PhotoImage(
    file=relative_to_assets("button_20.png"))
button_20 = Button(
    image=button_image_20,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_20 clicked"),
    relief="flat"
)
button_20.place(
    x=738.0,
    y=49.0,
    width=32.0,
    height=25.0
)

button_image_21 = PhotoImage(
    file=relative_to_assets("button_21.png"))
button_21 = Button(
    image=button_image_21,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_21 clicked"),
    relief="flat"
)
button_21.place(
    x=701.0,
    y=47.0,
    width=24.0,
    height=27.0
)

button_image_22 = PhotoImage(
    file=relative_to_assets("button_22.png"))
button_22 = Button(
    image=button_image_22,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_22 clicked"),
    relief="flat"
)
button_22.place(
    x=626.0,
    y=47.0,
    width=27.0,
    height=27.0
)

button_image_23 = PhotoImage(
    file=relative_to_assets("button_23.png"))
button_23 = Button(
    image=button_image_23,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_23 clicked"),
    relief="flat"
)
button_23.place(
    x=588.0,
    y=46.0,
    width=30.0,
    height=29.0
)

button_image_24 = PhotoImage(
    file=relative_to_assets("button_24.png"))
button_24 = Button(
    image=button_image_24,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_24 clicked"),
    relief="flat"
)
button_24.place(
    x=544.0,
    y=49.0,
    width=30.0,
    height=25.0
)

button_image_25 = PhotoImage(
    file=relative_to_assets("button_25.png"))
button_25 = Button(
    image=button_image_25,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_25 clicked"),
    relief="flat"
)
button_25.place(
    x=940.0,
    y=46.0,
    width=38.0,
    height=28.0
)

button_image_26 = PhotoImage(
    file=relative_to_assets("button_26.png"))
button_26 = Button(
    image=button_image_26,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_26 clicked"),
    relief="flat"
)
button_26.place(
    x=661.0,
    y=47.0,
    width=26.0,
    height=27.0
)
window.resizable(False, False)
window.mainloop()
