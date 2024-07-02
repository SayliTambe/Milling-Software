import tkinter as tk
from tkinter import ttk
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label
from tkinter import filedialog
import ezdxf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import filedialog
import os
import json
from tkinter import Scale
canvas_figure = None
ax=None

zoom_factor = 1.0
canvas_offset_x = 0
canvas_offset_y = 0





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Sayli Tambe\OneDrive\Desktop\figma\Tkinter-Designer-master (1)\op\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def show_value(val):
    value_label.config(text="Value: " + str(val))

def button_clicked():
    print("Button clicked")


window = Tk()

window.geometry("1151x667")
window.configure(bg = "#FFFFFF")


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
    24.0,
    46.0,
    anchor="nw",
    text="Input Design File",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    24.0,
    180.0,
    anchor="nw",
    text="Status\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    24.0,
    270.0,
    anchor="nw",
    text="Output Setup\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    408.0,
    293.0,
    anchor="nw",
    text="Output Setup\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    115.0,
    430.0,
    anchor="nw",
    text="Z Depth",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    432.0,
    512.0,
    anchor="nw",
    text="Comments",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    456.0,
    550.0,
    anchor="nw",
    text="Passes\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    428.0,
    446.0,
    anchor="nw",
    text="Canned",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    505.0,
    446.0,
    anchor="nw",
    text="Call",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    556.0,
    446.0,
    anchor="nw",
    text="Standalone",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    404.0,
    590.0,
    anchor="nw",
    text="Depth per Pass\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    550.0,
    anchor="nw",
    text="Pen On String 2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    75.0,
    470.0,
    anchor="nw",
    text="Down At Feed",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    108.0,
    510.0,
    anchor="nw",
    text="Rev Z Dir",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    75.0,
    590.0,
    anchor="nw",
    text="Pen Off String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    91.0,
    390.0,
    anchor="nw",
    text="Z Approach",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    103.0,
    350.0,
    anchor="nw",
    text="Q-Setting",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    310.0,
    anchor="nw",
    text="Feedrate String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    408.0,
    329.0,
    anchor="nw",
    text="Can Cycle No.",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    406.0,
    407.0,
    anchor="nw",
    text="Line Increment",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    413.0,
    368.0,
    anchor="nw",
    text="Start Line No.",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    24.0,
    118.0,
    anchor="nw",
    text="Output Run File",
    fill="#000000",
    font=("Inter", 14 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    287.0,
    321.5,
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
    y=310.0,
    width=196.0,
    height=21.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    178.0,
    220.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=24.0,
    y=209.0,
    width=308.0,
    height=21.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    178.0,
    86.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=24.0,
    y=75.0,
    width=308.0,
    height=21.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    178.0,
    155.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=24.0,
    y=144.0,
    width=308.0,
    height=21.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    287.0,
    361.5,
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
    y=350.0,
    width=196.0,
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
    x=380.0,
    y=75.0,
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
    x=385.0,
    y=141.0,
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
    global canvas_figure, ax

    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()
        
        global ax
        fig, ax = plt.subplots()
        for entity in msp:
            if entity.dxftype() == 'LINE':
                start = entity.dxf.start
                end = entity.dxf.end
                plt.plot([start.x, end.x], [start.y, end.y])
                
        if canvas_figure:
            canvas_figure.get_tk_widget().destroy()  # Destroy the previous canvas



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

def update_canvas():
    global ax, canvas_figure, zoom_factor, canvas_offset_x, canvas_offset_y
    if ax:
        ax.set_xlim(ax.get_xlim()[0] * zoom_factor + canvas_offset_x, ax.get_xlim()[1] * zoom_factor + canvas_offset_x)
        ax.set_ylim(ax.get_ylim()[0] * zoom_factor + canvas_offset_y, ax.get_ylim()[1] * zoom_factor + canvas_offset_y)
        canvas_figure.draw()

def zoom_in():
    global ax, zoom_factor
    if ax:
        ax.set_xlim(ax.get_xlim()[0] * 0.9, ax.get_xlim()[1] * 0.9)
        ax.set_ylim(ax.get_ylim()[0] * 0.9, ax.get_ylim()[1] * 0.9)
        canvas_figure.draw()
       
        update_canvas()

def zoom_out():
    global ax, zoom_factor
    if ax:
        ax.set_xlim(ax.get_xlim()[0] * 1.1, ax.get_xlim()[1] * 1.1)
        ax.set_ylim(ax.get_ylim()[0] * 1.1, ax.get_ylim()[1] * 1.1)
        canvas_figure.draw()
        
        update_canvas()
    
def show_all():
    global ax, zoom_factor, canvas_offset_x, canvas_offset_y
    if ax:
        ax.set_xlim(ax.get_xlim()[0] * 1.5, ax.get_xlim()[1] * 1.5)
        ax.set_ylim(ax.get_ylim()[0] * 1.5, ax.get_ylim()[1] * 1.5)
        canvas_figure.draw()
        
        update_canvas()



'''def update_canvas():
    global ax, canvas_figure, zoom_factor, canvas_offset_x, canvas_offset_y
    if ax:
        ax.set_xlim(ax.get_xlim()[0] * zoom_factor + canvas_offset_x, ax.get_xlim()[1] * zoom_factor + canvas_offset_x)
        ax.set_ylim(ax.get_ylim()[0] * zoom_factor + canvas_offset_y, ax.get_ylim()[1] * zoom_factor + canvas_offset_y)
        canvas_figure.draw()'''


button_3.place(
    x=343.0,
    y=80.0,
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
button_4.place(
    x=343.0,
    y=144.0,
    width=25.0,
    height=23.0
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

horizontal_slider = Scale(
    window,
    orient='horizontal',
    from_=1, to=5,
    length=400,
    sliderrelief='flat',
    #bg="#B0E0E6",
    command=lambda value: set_horizontal_slider(value)
)
horizontal_slider.place(x=700, y=600)

vertical_slider = Scale(
    window,
    orient='vertical',
    from_=1, to=5,
    length=500,
    sliderrelief='flat',
    #bg="#B0E0E6",
    command=lambda value: set_vertical_slider(value)
)
vertical_slider.place(x=1150, y=100)

def set_horizontal_slider(value):
    global canvas_offset_x
    canvas_offset_x = int(value) - 1 # Adjust as needed
    update_canvas()

def set_vertical_slider(value):
    global canvas_offset_y
    canvas_offset_y = int(value) - 1  # Adjust as needed
    update_canvas()



button_5.place(
    x=685.0,
    y=87.0,
    width=440.0,
    height=508.0
)

canvas.create_rectangle(
    678.0,
    284.0,
    678.0,
    661.0,
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

canvas.create_rectangle(
    395.5,
    303.5,
    396.9830627441406,
    478.0001220703125,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    395.5,
    303.5,
    408.0,
    304.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    495.0,
    304.0,
    665.5014953613281,
    305.25,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    665.5,
    304.5,
    666.0,
    478.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    396.5,
    477.5,
    666.0,
    478.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    107.0,
    282.0,
    676.9955444335938,
    283.03564453125,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    5.5,
    281.5,
    19.0,
    282.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    11.50067138671875,
    659.8732299804688,
    677.999267578125,
    661.7347412109375,
    fill="#000000",
    outline="")

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=zoom_in,
    relief="flat"
)
button_6.place(
    x=879.9999895095825,
    y=599.0,
    width=20.555843353271484,
    height=20.55584716796875
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=zoom_out,
    relief="flat"
)
button_7.place(
    x=908.0,
    y=600.0,
    width=20.0,
    height=20.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    235.0,
    401.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=189.0,
    y=390.0,
    width=92.0,
    height=21.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    839.5,
    67.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=798.0,
    y=56.0,
    width=83.0,
    height=21.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    1057.5,
    67.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=1016.0,
    y=56.0,
    width=83.0,
    height=21.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    235.0,
    441.5,
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
    y=430.0,
    width=92.0,
    height=21.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    589.0,
    521.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=522.0,
    y=510.0,
    width=134.0,
    height=21.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    540.5,
    561.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=522.0,
    y=550.0,
    width=37.0,
    height=21.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    540.5,
    601.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=522.0,
    y=590.0,
    width=37.0,
    height=21.0
)

entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    289.0,
    561.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=189.0,
    y=550.0,
    width=200.0,
    height=21.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    289.0,
    601.5,
    image=entry_image_14
)
entry_14 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)

checkbox_vars = [2]
for i in range(1):
    var = tk.IntVar()  # IntVar holds the value of the checkbox
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(window, text=f"", variable=var)
    checkbox.place(x=188.0, y=470.0)  # Adjust the placement here
    entry_14.place(x=188.0, y=470.0, width=20.0, height=2.0)  # Keep the entry_15 placement here


checkbox_vars = [2]
for i in range(1):
    var = tk.IntVar()  # IntVar holds the value of the checkbox
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(window, text=f"", variable=var)
    checkbox.place(x=188.0, y=510.0)  # Adjust the placement here
    entry_14.place(x=188.0, y=510.0, width=20.0, height=2.0)  # Keep the entry_15 placement here


checkbox_vars = [2]
for i in range(1):
    var = tk.IntVar()  # IntVar holds the value of the checkbox
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(window, text=f"", variable=var)
    checkbox.place(x=528.0, y=445.0)  # Adjust the placement here
    entry_14.place(x=528.0, y=445.0, width=5.0, height=1.0)  # Keep the entry_15 placement here right side


checkbox_vars = [2]
for i in range(1):
    var = tk.IntVar()  # IntVar holds the value of the checkbox
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(window, text=f"", variable=var)
    checkbox.place(x=478.0, y=445.0)  # Adjust the placement here
    entry_14.place(x=478.0, y=445.0, width=5.0, height=1.0)  # Keep the entry_15 placement here middle


checkbox_vars = [2]
for i in range(1):
    var = tk.IntVar()  # IntVar holds the value of the checkbox
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(window, text=f"", variable=var)
    checkbox.place(x=400.0, y=445.0)  # Adjust the placement here
    entry_14.place(x=400.0, y=445.0, width=5.0, height=1.0)  # Keep the entry_15 placement here





entry_14.place(
    x=189.0,
    y=590.0,
    width=200.0,
    height=21.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=show_all,
    relief="flat"
)
button_8.place(
    x=935.0,
    y=600.0,
    width=20.0,
    height=20.0
)



def save_parameters():
    parameters = {
        "entry_1": entry_1.get(),
        "entry_2": entry_2.get(),
        "entry_3": entry_3.get(),
        "entry_4": entry_4.get(),
        "entry_5": entry_5.get(),
        "entry_6": entry_6.get(),
        "entry_7": entry_7.get(),
        "entry_8": entry_8.get(),
        "entry_9": entry_9.get(),
        "entry_10": entry_10.get(),
        "entry_11": entry_11.get(),
        "entry_12": entry_12.get(),
        "entry_13": entry_13.get(),
        "entry_14": entry_14.get(),
        "entry_15": entry_15.get(),
        "entry_16": entry_16.get(),
        "entry_17": entry_17.get(),
       
        # Add more entries here as needed
    }

    desktop_path = Path.home() / r"C:\\Users\\Sayli Tambe\\OneDrive\\Desktop\\parameters.txt" 
    file_path = desktop_path / r"C:\\Users\\Sayli Tambe\\OneDrive\\Desktop\\parameters.txt" 

    try:
        with open(file_path, "w") as f:
            json.dump(parameters, f)
        print("Parameters saved successfully to the desktop.")
    except Exception as e:
        print("An error occurred:", e)



button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=save_parameters,
    relief="flat"
)
button_9.place(
    x=826.0,
    y=599.0,
    width=47.0,
    height=20.0
)

canvas.create_rectangle(
    410.0,
    448.0,
    426.0,
    464.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    487.0,
    448.0,
    503.0,
    464.0,
    fill="#000000",
    outline="")

canvas.create_rectangle(
    538.0,
    448.0,
    554.0,
    464.0,
    fill="#000000",
    outline="")

entry_image_15 = PhotoImage(
    file=relative_to_assets("entry_15.png"))
entry_bg_15 = canvas.create_image(
    578.0,
    340.5,
    image=entry_image_15
)
entry_15 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_15.place(
    x=522.0,
    y=329.0,
    width=112.0,
    height=21.0
)

entry_image_16 = PhotoImage(
    file=relative_to_assets("entry_16.png"))
entry_bg_16 = canvas.create_image(
    578.0,
    379.5,
    image=entry_image_16
)
entry_16 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_16.place(
    x=522.0,
    y=368.0,
    width=112.0,
    height=21.0
)

entry_image_17 = PhotoImage(
    file=relative_to_assets("entry_17.png"))
entry_bg_17 = canvas.create_image(
    578.0,
    418.5,
    image=entry_image_17
)
entry_17 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_17.place(
    x=522.0,
    y=407.0,
    width=112.0,
    height=21.0
)

window.resizable(True, True)
window.mainloop()
