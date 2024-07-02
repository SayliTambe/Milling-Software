import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from tkinter import filedialog
import ezdxf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import os
from tkinter import Scale


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sayli Tambe\OneDrive\Desktop\figma\Tkinter-Designer-master (1)\asmi\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def show_value(val):
    value_label.config(text="Value: " + str(val))

def button_clicked():
    print("Button clicked")



window = Tk()
window.title("Combined Slider and Tkinter Designer Example")
window.geometry("1151x667")
window.configure(bg = "#FFFFFF")

# Create a button
button = tk.Button(window, text="Button", command=button_clicked)
button.place(x=400, y=100)


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 667,
    width = 1151,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_rectangle(
    0.0,
    0.0,
    1151.0,
    26.0,
    fill="#D9D9D9",
    outline="")

canvas.create_text(
    23.0,
    69.0,
    anchor="nw",
    text="Input Design File",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    23.0,
    215.0,
    anchor="nw",
    text="Status\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    23.0,
    309.0,
    anchor="nw",
    text="Output Setup\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    409.0,
    325.0,
    anchor="nw",
    text="Output Setup\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    494.0,
    anchor="nw",
    text="Z Depth",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    410.0,
    559.0,
    anchor="nw",
    text="Comments",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    477.0,
    595.0,
    anchor="nw",
    text="Passes\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    430.0,
    489.0,
    anchor="nw",
    text="Canned",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    516.0,
    490.0,
    anchor="nw",
    text="Call",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    574.0,
    490.0,
    anchor="nw",
    text="Standalone",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    477.0,
    631.0,
    anchor="nw",
    text="Depth per Pass\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    47.0,
    593.0,
    anchor="nw",
    text="Pen On String 2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    47.0,
    529.0,
    anchor="nw",
    text="Down At Feed",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    47.0,
    559.0,
    anchor="nw",
    text="Rev Z Dir",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    47.0,
    631.0,
    anchor="nw",
    text="Pen Off String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    63.0,
    449.0,
    anchor="nw",
    text="Z Approach",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    405.0,
    anchor="nw",
    text="Q-Setting",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    355.0,
    anchor="nw",
    text="Feedrate String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    419.0,
    362.0,
    anchor="nw",
    text="Can Cycle No.",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    420.0,
    451.0,
    anchor="nw",
    text="Line Increment",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    419.0,
    405.0,
    anchor="nw",
    text="Start Line No.",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    21.0,
    144.0,
    anchor="nw",
    text="Output Run File",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    287.0,
    366.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=189.0,
    y=355.0,
    width=196.0,
    height=21.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    175.0,
    249.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=21.0,
    y=238.0,
    width=308.0,
    height=21.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    171.0,
    110.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=17.0,
    y=99.0,
    width=308.0,
    height=21.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    171.0,
    185.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=17.0,
    y=174.0,
    width=308.0,
    height=21.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    287.0,
    413.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=189.0,
    y=402.0,
    width=196.0,
    height=21.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    579.0,
    368.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=534.0,
    y=357.0,
    width=90.0,
    height=21.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    580.0,
    415.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=535.0,
    y=404.0,
    width=90.0,
    height=21.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    581.0,
    462.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#FFFFFF",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=536.0,
    y=451.0,
    width=90.0,
    height=21.0
)

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
    x=388.0,
    y=95.0,
    width=63.0,
    height=23.0
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
    x=382.0,
    y=167.0,
    width=63.0,
    height=23.0
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

def open_dxf_file():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()
      

        fig, ax = plt.subplots()
        for entity in msp:
            if entity.dxftype() == 'LINE':
                start = entity.dxf.start
                end = entity.dxf.end
                plt.plot([start.x, end.x], [start.y, end.y])
                



        #canvas = FigureCanvasTkAgg(fig, master=button_5)
        #canvas.draw()
        #canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        canvas_figure = FigureCanvasTkAgg(fig, master=window)
        canvas_figure.draw()

        # Place the canvas on the main canvas
        canvas_figure_widget = canvas_figure.get_tk_widget()
        canvas_figure_widget.place(x=680.0, y=80.0, width=440.0, height=508.0)

        entry_3.delete(0, "end")
        entry_3.insert(0, file_path)



button_3.place(
    x=345.0,
    y=99.0,
    width=25.0,
    height=23.0
)

button_3.configure(command=open_dxf_file)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)

def open_dxf_file():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()

        fig, ax = plt.subplots()
        for entity in msp:
            if entity.dxftype() == 'LINE':
                start = entity.dxf.start
                end = entity.dxf.end
                plt.plot([start.x, end.x], [start.y, end.y])
                

        canvas = FigureCanvasTkAgg(fig, master=button_5)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        entry_2.delete(0, "end")
        entry_2.insert(0, file_path)


button_4.place(
    x=345.0,
    y=167.0,
    width=25.0,
    height=23.0
)

button_4.configure(command=open_dxf_file)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)

horizontal_slider = Scale(
    window,
    orient='horizontal',
    from_=0, to=100,
    length=400,
    sliderrelief='flat',
    #bg="#B0E0E6",
    
)
horizontal_slider.place(x=700, y=600)

vertical_slider = Scale(
    window,
    orient='vertical',
    from_=0, to=100,
    length=500,
    sliderrelief='flat',
    #bg="#B0E0E6",
    
)
vertical_slider.place(x=1150, y=100)



button_5.place(
    x=685.0,
    y=87.0,
    width=440.0,
    height=508.0
)

canvas.create_rectangle(
    678.0,
    323.0,
    678.0,
    662.0,
    fill="#000000",
    outline="")

canvas.create_text(
    689.0,
    56.0,
    anchor="nw",
    text="Drawing Width",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    898.0,
    57.0,
    anchor="nw",
    text="Drawing Length",
    fill="#000000",
    font=("Inter", 14 * -1)
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
    x=413.0,
    y=494.0,
    width=10.0,
    height=10.0
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
    x=499.0,
    y=495.0,
    width=10.0,
    height=10.0
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
    x=558.0,
    y=494.0,
    width=10.0,
    height=10.0
)

canvas.create_rectangle(
    397.5,
    333.5,
    399.0,
    529.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    397.5,
    333.5,
    410.0,
    334.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    496.0,
    335.75,
    666.5014953613281,
    337.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    665.5,
    336.5,
    666.0,
    529.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    398.5,
    527.5,
    666.0001831054688,
    528.9468383789062,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    108.00360107421875,
    320.0,
    678.0079956054688,
    321.4842529296875,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    10.5,
    318.5,
    24.0,
    319.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    11.0,
    319.0,
    11.970947265625,
    665.0000610351562,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    11.50067138671875,
    659.8732299804688,
    677.999267578125,
    661.7347412109375,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    10.0,
    318.0,
    11.0,
    660.0,
    fill="#000000",
    outline="")

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
    x=889.722095489502,
    y=598.7221069335938,
    width=20.555845260620117,
    height=20.55584716796875
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
    x=926.0,
    y=599.0,
    width=20.0,
    height=20.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    235.0,
    460.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=189.0,
    y=449.0,
    width=92.0,
    height=21.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    839.5,
    67.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=798.0,
    y=56.0,
    width=83.0,
    height=21.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    1057.5,
    67.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=1016.0,
    y=56.0,
    width=83.0,
    height=21.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    235.0,
    501.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=189.0,
    y=490.0,
    width=92.0,
    height=21.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    583.0,
    570.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=516.0,
    y=559.0,
    width=134.0,
    height=21.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    207.5,
    537.0,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_14.place(
    x=189.0,
    y=526.0,
    width=37.0,
    height=20.0
)

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    207.5,
    573.0,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=189.0,
    y=562.0,
    width=37.0,
    height=20.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    434.5,
    606.0,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=416.0,
    y=595.0,
    width=37.0,
    height=20.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    434.5,
    641.0,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=416.0,
    y=630.0,
    width=37.0,
    height=20.0
)

entry_image_18 = PhotoImage(
    file=relative_to_assets("entry_18.png"))
entry_bg_18 = canvas.create_image(
    289.0,
    607.0,
    image=entry_image_18
)
entry_18 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_18.place(
    x=189.0,
    y=596.0,
    width=200.0,
    height=20.0
)

entry_image_19 = PhotoImage(
    file=relative_to_assets("entry_19.png"))
entry_bg_19 = canvas.create_image(
    289.0,
    641.0,
    image=entry_image_19
)
entry_19 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_19.place(
    x=189.0,
    y=630.0,
    width=200.0,
    height=20.0
)
window.resizable(True, True)
window.mainloop()