
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sayli Tambe\OneDrive\Desktop\figma\Tkinter-Designer-master (1)\output\build\assets\frame1")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("134x2275")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 2275,
    width = 134,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    29.0,
    20.0,
    105.0,
    37.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    20.0,
    471.0,
    114.0,
    897.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    20.0,
    922.0,
    114.0,
    1353.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    20.0,
    1373.0,
    114.0,
    1804.0,
    fill="#000000",
    outline="")
window.resizable(False, False)
window.mainloop()
