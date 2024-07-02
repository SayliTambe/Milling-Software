import tkinter as tk
from tkinter import ttk
from tkinter import Menubutton, Menu
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, filedialog, Scale
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os, json, ezdxf

canvas_figure = None
ax=None
zoom_factor = 1.0
canvas_offset_x = 0
canvas_offset_y = 0
input_dxf_path = None  # Define the variable globally



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("figma/Tkinter-Designer-master (1)/output/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def show_value(val):
    value_label.config(text="Value: " + str(val))

def button_clicked():
    print("Button clicked")

import os
import ezdxf

def convert_dxf_to_gcode(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    gcode = []

    for entity in msp:
        if entity.dxftype() == 'LINE':
            start = entity.dxf.start
            end = entity.dxf.end
            gcode.append(f"G1 X{start.x:.3f} Y{start.y:.3f}")  # Move to the start point
            gcode.append(f"G1 X{end.x:.3f} Y{end.y:.3f}")      # Move to the end point

    return "\n".join(gcode)
'''
def main():
    open_dxf_file = r"D:\\Interface\\data\\DimensionAI.DXF"  # Update this with your DXF file path
    gcode_output_path = r"D:\\Interface\\data\\sayli.gcode"

    gcode = convert_dxf_to_gcode(r"D:\\Interface\\data\\DimensionAI.DXF")

    with open(gcode_output_path, "w") as gcode_file:
        gcode_file.write(gcode)

    print("DXF to G-code conversion complete")

if __name__ == "__main__":
    main()'''

def convert_dxf_and_save(dxf_file_path):
    if dxf_file_path:
        gcode_output_path =  "sayli.gcode"  # Define your output G-code file path here

        gcode = convert_dxf_to_gcode(dxf_file_path)

        with open(gcode_output_path, "w") as gcode_file:
            gcode_file.write(gcode)

        print("DXF to G-code conversion complete")


   


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


def horizontal_toolbar_button_click(button_id):
    print(f"Horizontal Button {button_id} clicked")

# Create a frame for the horizontal toolbar


horizontal_toolbar_frame = tk.Frame(window, bg="White")
horizontal_toolbar_frame.pack(side=tk.TOP, fill=tk.X)

# Create a button to open the "File" submenu

button1 = tk.Button(horizontal_toolbar_frame, text="File")
button1.pack(side=tk.LEFT, padx=3)
button2 = tk.Button(horizontal_toolbar_frame, text="Edit")
button2.pack(side=tk.LEFT, padx=3)
button3 = tk.Button(horizontal_toolbar_frame, text="View")
button3.pack(side=tk.LEFT, padx=3)
button4 = tk.Button(horizontal_toolbar_frame, text="Help")
button4.pack(side=tk.LEFT, padx=3)


canvas.create_text(
    8.0,
    36.0,
    anchor="nw",
    text="Input Design File",
    fill="#000000",
    font=("Inter", 14 * -1)
)


canvas.create_text(
    10.0,
    141.0,
    anchor="nw",
    text="Status\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    7.0,
    200.0,
    anchor="nw",
    text="Output Setup\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    59.0,
    336.0,
    anchor="nw",
    text="Z Depth",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    39.0,
    505.0,
    anchor="nw",
    text="Comments",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    539.0,
    anchor="nw",
    text="Passes\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    11.0,
    573.0,
    anchor="nw",
    text="Depth per Pass\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    10.0,
    435.0,
    anchor="nw",
    text="Pen On String 2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    19.0,
    370.0,
    anchor="nw",
    text="Down At Feed",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    51.0,
    402.0,
    anchor="nw",
    text="Rev Z Dir",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    19.0,
    471.0,
    anchor="nw",
    text="Pen Off String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    35.0,
    302.0,
    anchor="nw",
    text="Z Approach",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    49.0,
    269.0,
    anchor="nw",
    text="Q-Setting",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    9.0,
    236.0,
    anchor="nw",
    text="Feedrate String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    7.0,
    86.0,
    anchor="nw",
    text="Output Run File",
    fill="#000000",
    font=("Inter", 14 * -1)
)



entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    226.0,
    247.5,
    image=entry_image_1
)

from tkinter import TclError  # Import TclError for validation

# ...

def is_valid_input(action, value_if_allowed):
    # Check if the input consists of only digits
    if action == "1":  # 1 means insertion
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return True
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
    
)
entry_1.place(
    x=137.0,
    y=236.0,
    width=178.0,
    height=21.0
)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    161.0,
    175.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=7.0,
    y=164.0,
    width=308.0,
    height=21.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    161.0,
    68.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=7.0,
    y=57.0,
    width=308.0,
    height=21.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    161.0,
    119.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=7.0,
    y=108.0,
    width=308.0,
    height=21.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    226.0,
    280.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
    
   

)
entry_5.place(
    x=137.0,
    y=269.0,
    width=178.0,
    height=21.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_dxf_and_save(entry_3.get()),
    relief="flat"
)
button_1.place(
    x=364.0,
    y=57.0,
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
    x=364.0,
    y=108.0,
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
    global canvas_figure, ax, zoom_factor, canvas_offset_x, canvas_offset_y
    global input_dxf_path

    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()

        input_dxf_path = file_path  # Update the input_dxf_path with the selected file path
        print(f"Selected DXF file: {input_dxf_path}")
        entry_4.delete(0, "end")
        entry_4.insert(0, input_dxf_path)


        global ax
        fig, ax = plt.subplots()
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        first_start = None  
        for entity in msp:
            if entity.dxftype() == 'LINE':
                start = entity.dxf.start
                end = entity.dxf.end
                if first_start is None:
                    first_start = start

                min_x = min(min_x, start.x, end.x)
                min_y = min(min_y, start.y, end.y)
                max_x = max(max_x, start.x, end.x)
                max_y = max(max_y, start.y, end.y)
                plt.plot([start.x, end.x], [start.y, end.y], 'b')

        if first_start is not None:
            # Plot a marker at the starting point of the first LINE entity
            ax.plot(first_start.x, first_start.y, marker='+', markersize=10, color='BLACK')

            open_dxf_file()
            plt.show()              
         

        



        units_conversion_factor = 0.1  # Adjust this based on your DXF file's units

        width_cm = (max_x - min_x) * units_conversion_factor
        height_cm = (max_y - min_y) * units_conversion_factor

        entry_7.delete(0, "end")
        entry_7.insert(0, f"{width_cm:.2f} cm")

        entry_8.delete(0, "end")
        entry_8.insert(0, f"{height_cm:.2f} cm")

        
                
        if canvas_figure:
            canvas_figure.get_tk_widget().destroy()  # Destroy the previous canvas



        #canvas = FigureCanvasTkAgg(fig, master=button_5)
        #canvas.draw()
        #canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        canvas_figure = FigureCanvasTkAgg(fig, master=window)
        canvas_figure.draw()

        
        # Place the canvas on the main canvas
        canvas_figure_widget = canvas_figure.get_tk_widget()
        canvas_figure_widget.place(x=451.0, y=102.0, width=650.0, height=470.0)
        

        entry_3.delete(0, "end")
        entry_3.insert(0, file_path)

def update_canvas():
    global ax, canvas_figure, zoom_factor, canvas_offset_x, canvas_offset_y
    if ax:
        ax.set_xlim(ax.get_xlim()[0] * zoom_factor + canvas_offset_x, ax.get_xlim()[1] * zoom_factor + canvas_offset_x -0.5)
        ax.set_ylim(ax.get_ylim()[0] * zoom_factor + canvas_offset_y, ax.get_ylim()[1] * zoom_factor + canvas_offset_y -0.5)
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
    x=327.0,
    y=57.0,
    width=25.0,
    height=23.0
)

button_3.configure(command=open_dxf_file)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
'''button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)'''

def open_dxf_file():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf"), ("gcode Files", "*.gcode")])
    if file_path:
        # Check the file extension to determine its type
        if file_path.lower().endswith('.dxf'):
            # Process the selected DXF file
            print(f"Selected DXF file: {file_path}")
            # Add your DXF processing logic here

        elif file_path.lower().endswith('.gcode'):
            # Process the selected G-code (gcd) file
            print(f"Selected gcode file: {file_path}")
            # Add your G-code processing logic here

        # Update the corresponding entry field with the selected file path
        entry_4.delete(0, "end")
        entry_4.insert(0, file_path)

        # Rest of your code for plotting DXF content or other actions

# ... (your code)

button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)

# ... (rest of your code)



button_4.place(
    x=326.0,
    y=108.0,
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
    from_=1, to=5,
    length=700,
    sliderrelief='flat',
    #bg="#B0E0E6",
    command=lambda value: set_horizontal_slider(value)
)
horizontal_slider.place(x=425, y=600)

vertical_slider = Scale(
    window,
    orient='vertical',
    from_=1, to=5,
    length=500,
    sliderrelief='flat',
    #bg="#B0E0E6",
    command=lambda value: set_vertical_slider(value)
)
vertical_slider.place(x=1130, y=87)
def set_horizontal_slider(value):
    global canvas_offset_x
    canvas_offset_x = int(value) - 1 # Adjust as needed
    update_canvas()

def set_vertical_slider(value):
    global canvas_offset_y
    canvas_offset_y = int(value) - 5  # Adjust as needed
    update_canvas()

button_5.place(
    x=427.0,
    y=87.0,
    width=698.0,
    height=509.0
)

canvas.create_text(
    549.0,
    57.0,
    anchor="nw",
    text="Drawing Width",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    769.0,
    58.0,
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
    command=zoom_in,
    relief="flat"
)
button_6.place(
    x=746.0,
    y=605.0,
    width=20.55584716796875,
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
    x=781.0,
    y=605.0,
    width=20.0,
    height=20.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    226.0,
    313.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=137.0,
    y=302.0,
    width=178.0,
    height=21.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    704.5,
    68.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=663.0,
    y=57.0,
    width=83.0,
    height=21.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    933.5,
    69.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=892.0,
    y=58.0,
    width=83.0,
    height=21.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    226.0,
    347.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=137.0,
    y=336.0,
    width=178.0,
    height=21.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    226.0,
    516.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=137.0,
    y=505.0,
    width=178.0,
    height=21.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    226.0,
    550.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=137.0,
    y=539.0,
    width=178.0,
    height=21.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    226.0,
    584.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=137.0,
    y=573.0,
    width=178.0,
    height=21.0
)

def update_entry_11(event):
    try:
        value_9 = float(entry_9.get())
        value_12 = float(entry_12.get())
        
        # Ensure that value_9 is always greater than value_12
        if value_9 <= value_12:
            entry_11.delete(0, "end")
            entry_11.insert(0, "Invalid")
            return

        result = value_9 / value_12
        entry_11.delete(0, "end")
        entry_11.insert(0, f"{result:.2f}")
        
    except ValueError:
        entry_11.delete(0, "end")

entry_9.bind("<KeyRelease>", update_entry_11)
entry_12.bind("<KeyRelease>", update_entry_11)


entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    226.0,
    446.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=137.0,
    y=435.0,
    width=178.0,
    height=21.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    226.0,
    482.5,
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
    checkbox.place(x=138.0, y=370.0)  # Adjust the placement here
    entry_14.place(x=138.0, y=370.0, width=20.0, height=2.0)  # Keep the entry_15 placement here


checkbox_vars = [2]
for i in range(1):
    var = tk.IntVar()  # IntVar holds the value of the checkbox
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(window, text=f"", variable=var)
    checkbox.place(x=138.0, y=400.0)  # Adjust the placement here
    entry_14.place(x=138.0, y=400.0, width=20.0, height=2.0)  # Keep the entry_15 placement here


entry_14.place(
    x=137.0,
    y=471.0,
    width=178.0,
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

def save_parameters():
    parameters = {
        "Feedrate string": entry_1.get(),
        "Status": entry_2.get(),
        "input file name": entry_3.get(),
        "Output run file": entry_4.get(),
        "Q-Setting": entry_5.get(),
        "Z Approch": entry_6.get(),
        "Drawing width": entry_7.get(),
        "Drawing length": entry_8.get(),
        "Z Depth": entry_9.get(),
        "Comments": entry_10.get(),
        "Passes": entry_11.get(),
        "Depth Per Pass": entry_12.get(),
        "Pen On String 2": entry_13.get(),
        "Pen Off String ": entry_14.get(),
        #"Can Cycle No": entry_15.get(),
        #"Start Line No": entry_16.get(),
        #"Line Increment": entry_17.get(),
       
        # Add more entries here as needed
    }

    # Ask the user to choose the save location and file name
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])

    if file_path:
        try:
            with open(file_path, "w") as f:
                for key, value in parameters.items():
                    f.write(f"{key}: {value}\n")
            print("Parameters saved successfully.")
        except Exception as e:
            print("An error occurred:", e)
    else:
        print("Save operation canceled by the user.")

button_8.place(
    x=815.0,
    y=605.0,
    width=20.0,
    height=20.0
)

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
    x=685.0,
    y=605.0,
    width=47.0,
    height=23.0
)

'''button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)



button_10.place(
    x=315.0,
    y=0.0,
    width=97.0,
    height=26.0
)'''

import tkinter.simpledialog

# Create the menu for button_10
button_10_menu = Menu(window, tearoff=0)
button_10_menu.add_command(label="Can Cycle No", command=lambda: show_input_dialog("Suboption 1"))
button_10_menu.add_command(label="Start Line No", command=lambda: show_input_dialog("Suboption 2"))
button_10_menu.add_command(label="Line Increment", command=lambda: show_input_dialog("Suboption 3"))
button_10_menu.add_command(label="machining", command=lambda: show_input_dialog("Suboption 4"))
button_10_menu.add_command(label="3D print", command=lambda: show_input_dialog("Suboption 5"))

# Function to show an input dialog
def show_input_dialog(suboption):
    value = tkinter.simpledialog.askstring("Input", f"Enter value for {suboption}:", parent=window)
    if value is not None:
        print(f"Value entered for {suboption}: {value}")

# Create the Button for button_10
button_10 = Button(window, text="output setup")
button_10.place(x=160.0, y=0.0, width=97.0, height=26.0)

# Configure the button_10 to display the menu
def show_menu(event):
    button_10_menu.post(event.x_root, event.y_root)

button_10.bind("<Button-1>", show_menu)  # Bind left mouse button click to show the menu


window.resizable(True, True)
window.mainloop()
from tkinter import ttk
from tkinter import Menubutton, Menu
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Label, filedialog, Scale
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import os, json, ezdxf

canvas_figure = None
ax=None
zoom_factor = 1.0
canvas_offset_x = 0
canvas_offset_y = 0
input_dxf_path = None  # Define the variable globally



OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("figma/Tkinter-Designer-master (1)/output/build/assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)
def show_value(val):
    value_label.config(text="Value: " + str(val))

def button_clicked():
    print("Button clicked")

import os
import ezdxf

def convert_dxf_to_gcode(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    gcode = []

    for entity in msp:
        if entity.dxftype() == 'LINE':
            start = entity.dxf.start
            end = entity.dxf.end
            gcode.append(f"G1 X{start.x:.3f} Y{start.y:.3f}")  # Move to the start point
            gcode.append(f"G1 X{end.x:.3f} Y{end.y:.3f}")      # Move to the end point

    return "\n".join(gcode)
'''
def main():
    open_dxf_file = r"D:\\Interface\\data\\DimensionAI.DXF"  # Update this with your DXF file path
    gcode_output_path = r"D:\\Interface\\data\\sayli.gcode"

    gcode = convert_dxf_to_gcode(r"D:\\Interface\\data\\DimensionAI.DXF")

    with open(gcode_output_path, "w") as gcode_file:
        gcode_file.write(gcode)

    print("DXF to G-code conversion complete")

if __name__ == "__main__":
    main()'''

def convert_dxf_and_save(dxf_file_path):
    if dxf_file_path:
        gcode_output_path =  "sayli.gcode"  # Define your output G-code file path here

        gcode = convert_dxf_to_gcode(dxf_file_path)

        with open(gcode_output_path, "w") as gcode_file:
            gcode_file.write(gcode)

        print("DXF to G-code conversion complete")


   


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


def horizontal_toolbar_button_click(button_id):
    print(f"Horizontal Button {button_id} clicked")

# Create a frame for the horizontal toolbar


horizontal_toolbar_frame = tk.Frame(window, bg="White")
horizontal_toolbar_frame.pack(side=tk.TOP, fill=tk.X)

# Create a button to open the "File" submenu

button1 = tk.Button(horizontal_toolbar_frame, text="File")
button1.pack(side=tk.LEFT, padx=3)
button2 = tk.Button(horizontal_toolbar_frame, text="Edit")
button2.pack(side=tk.LEFT, padx=3)
button3 = tk.Button(horizontal_toolbar_frame, text="View")
button3.pack(side=tk.LEFT, padx=3)
button4 = tk.Button(horizontal_toolbar_frame, text="Help")
button4.pack(side=tk.LEFT, padx=3)


canvas.create_text(
    8.0,
    36.0,
    anchor="nw",
    text="Input Design File",
    fill="#000000",
    font=("Inter", 14 * -1)
)


canvas.create_text(
    10.0,
    141.0,
    anchor="nw",
    text="Status\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    7.0,
    200.0,
    anchor="nw",
    text="Output Setup\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    59.0,
    336.0,
    anchor="nw",
    text="Z Depth",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    39.0,
    505.0,
    anchor="nw",
    text="Comments",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    64.0,
    539.0,
    anchor="nw",
    text="Passes\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    11.0,
    573.0,
    anchor="nw",
    text="Depth per Pass\n",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    10.0,
    435.0,
    anchor="nw",
    text="Pen On String 2",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    19.0,
    370.0,
    anchor="nw",
    text="Down At Feed",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    51.0,
    402.0,
    anchor="nw",
    text="Rev Z Dir",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    19.0,
    471.0,
    anchor="nw",
    text="Pen Off String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    35.0,
    302.0,
    anchor="nw",
    text="Z Approach",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    49.0,
    269.0,
    anchor="nw",
    text="Q-Setting",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    9.0,
    236.0,
    anchor="nw",
    text="Feedrate String",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    7.0,
    86.0,
    anchor="nw",
    text="Output Run File",
    fill="#000000",
    font=("Inter", 14 * -1)
)



entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    226.0,
    247.5,
    image=entry_image_1
)

from tkinter import TclError  # Import TclError for validation

# ...

def is_valid_input(action, value_if_allowed):
    # Check if the input consists of only digits
    if action == "1":  # 1 means insertion
        try:
            int(value_if_allowed)
            return True
        except ValueError:
            return False
    return True
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
    
)
entry_1.place(
    x=137.0,
    y=236.0,
    width=178.0,
    height=21.0
)
entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    161.0,
    175.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=7.0,
    y=164.0,
    width=308.0,
    height=21.0
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    161.0,
    68.5,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=7.0,
    y=57.0,
    width=308.0,
    height=21.0
)

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    161.0,
    119.5,
    image=entry_image_4
)
entry_4 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=7.0,
    y=108.0,
    width=308.0,
    height=21.0
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    226.0,
    280.5,
    image=entry_image_5
)
entry_5 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
    
   

)
entry_5.place(
    x=137.0,
    y=269.0,
    width=178.0,
    height=21.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: convert_dxf_and_save(entry_3.get()),
    relief="flat"
)
button_1.place(
    x=364.0,
    y=57.0,
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
    x=364.0,
    y=108.0,
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
    global canvas_figure, ax, zoom_factor, canvas_offset_x, canvas_offset_y
    global input_dxf_path

    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if file_path:
        doc = ezdxf.readfile(file_path)
        msp = doc.modelspace()

        input_dxf_path = file_path  # Update the input_dxf_path with the selected file path
        print(f"Selected DXF file: {input_dxf_path}")
        entry_4.delete(0, "end")
        entry_4.insert(0, input_dxf_path)


        global ax
        fig, ax = plt.subplots()
        min_x, min_y, max_x, max_y = float('inf'), float('inf'), float('-inf'), float('-inf')
        first_start = None  
        for entity in msp:
            if entity.dxftype() == 'LINE':
                start = entity.dxf.start
                end = entity.dxf.end
                if first_start is None:
                    first_start = start

                min_x = min(min_x, start.x, end.x)
                min_y = min(min_y, start.y, end.y)
                max_x = max(max_x, start.x, end.x)
                max_y = max(max_y, start.y, end.y)
                plt.plot([start.x, end.x], [start.y, end.y], 'b')

        if first_start is not None:
            # Plot a marker at the starting point of the first LINE entity
            ax.plot(first_start.x, first_start.y, marker='+', markersize=10, color='BLACK')

            open_dxf_file()
            plt.show()              
         

        



        units_conversion_factor = 0.1  # Adjust this based on your DXF file's units

        width_cm = (max_x - min_x) * units_conversion_factor
        height_cm = (max_y - min_y) * units_conversion_factor

        entry_7.delete(0, "end")
        entry_7.insert(0, f"{width_cm:.2f} cm")

        entry_8.delete(0, "end")
        entry_8.insert(0, f"{height_cm:.2f} cm")

        
                
        if canvas_figure:
            canvas_figure.get_tk_widget().destroy()  # Destroy the previous canvas



        #canvas = FigureCanvasTkAgg(fig, master=button_5)
        #canvas.draw()
        #canvas.get_tk_widget().pack(fill=tk.BOTH, expand=1)
        canvas_figure = FigureCanvasTkAgg(fig, master=window)
        canvas_figure.draw()

        
        # Place the canvas on the main canvas
        canvas_figure_widget = canvas_figure.get_tk_widget()
        canvas_figure_widget.place(x=451.0, y=102.0, width=650.0, height=470.0)
        

        entry_3.delete(0, "end")
        entry_3.insert(0, file_path)

def update_canvas():
    global ax, canvas_figure, zoom_factor, canvas_offset_x, canvas_offset_y
    if ax:
        ax.set_xlim(ax.get_xlim()[0] * zoom_factor + canvas_offset_x, ax.get_xlim()[1] * zoom_factor + canvas_offset_x -0.5)
        ax.set_ylim(ax.get_ylim()[0] * zoom_factor + canvas_offset_y, ax.get_ylim()[1] * zoom_factor + canvas_offset_y -0.5)
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
    x=327.0,
    y=57.0,
    width=25.0,
    height=23.0
)

button_3.configure(command=open_dxf_file)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
'''button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)'''

def open_dxf_file():
    file_path = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf"), ("gcode Files", "*.gcode")])
    if file_path:
        # Check the file extension to determine its type
        if file_path.lower().endswith('.dxf'):
            # Process the selected DXF file
            print(f"Selected DXF file: {file_path}")
            # Add your DXF processing logic here

        elif file_path.lower().endswith('.gcode'):
            # Process the selected G-code (gcd) file
            print(f"Selected gcode file: {file_path}")
            # Add your G-code processing logic here

        # Update the corresponding entry field with the selected file path
        entry_4.delete(0, "end")
        entry_4.insert(0, file_path)

        # Rest of your code for plotting DXF content or other actions

# ... (your code)

button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)

# ... (rest of your code)



button_4.place(
    x=326.0,
    y=108.0,
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
    from_=1, to=5,
    length=700,
    sliderrelief='flat',
    #bg="#B0E0E6",
    command=lambda value: set_horizontal_slider(value)
)
horizontal_slider.place(x=425, y=600)

vertical_slider = Scale(
    window,
    orient='vertical',
    from_=1, to=5,
    length=500,
    sliderrelief='flat',
    #bg="#B0E0E6",
    command=lambda value: set_vertical_slider(value)
)
vertical_slider.place(x=1130, y=87)
def set_horizontal_slider(value):
    global canvas_offset_x
    canvas_offset_x = int(value) - 1 # Adjust as needed
    update_canvas()

def set_vertical_slider(value):
    global canvas_offset_y
    canvas_offset_y = int(value) - 5  # Adjust as needed
    update_canvas()

button_5.place(
    x=427.0,
    y=87.0,
    width=698.0,
    height=509.0
)

canvas.create_text(
    549.0,
    57.0,
    anchor="nw",
    text="Drawing Width",
    fill="#000000",
    font=("Inter", 14 * -1)
)

canvas.create_text(
    769.0,
    58.0,
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
    command=zoom_in,
    relief="flat"
)
button_6.place(
    x=746.0,
    y=605.0,
    width=20.55584716796875,
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
    x=781.0,
    y=605.0,
    width=20.0,
    height=20.0
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    226.0,
    313.5,
    image=entry_image_6
)
entry_6 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=137.0,
    y=302.0,
    width=178.0,
    height=21.0
)

entry_image_7 = PhotoImage(
    file=relative_to_assets("entry_7.png"))
entry_bg_7 = canvas.create_image(
    704.5,
    68.5,
    image=entry_image_7
)
entry_7 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_7.place(
    x=663.0,
    y=57.0,
    width=83.0,
    height=21.0
)

entry_image_8 = PhotoImage(
    file=relative_to_assets("entry_8.png"))
entry_bg_8 = canvas.create_image(
    933.5,
    69.5,
    image=entry_image_8
)
entry_8 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_8.place(
    x=892.0,
    y=58.0,
    width=83.0,
    height=21.0
)

entry_image_9 = PhotoImage(
    file=relative_to_assets("entry_9.png"))
entry_bg_9 = canvas.create_image(
    226.0,
    347.5,
    image=entry_image_9
)
entry_9 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_9.place(
    x=137.0,
    y=336.0,
    width=178.0,
    height=21.0
)

entry_image_10 = PhotoImage(
    file=relative_to_assets("entry_10.png"))
entry_bg_10 = canvas.create_image(
    226.0,
    516.5,
    image=entry_image_10
)
entry_10 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_10.place(
    x=137.0,
    y=505.0,
    width=178.0,
    height=21.0
)

entry_image_11 = PhotoImage(
    file=relative_to_assets("entry_11.png"))
entry_bg_11 = canvas.create_image(
    226.0,
    550.5,
    image=entry_image_11
)
entry_11 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_11.place(
    x=137.0,
    y=539.0,
    width=178.0,
    height=21.0
)

entry_image_12 = PhotoImage(
    file=relative_to_assets("entry_12.png"))
entry_bg_12 = canvas.create_image(
    226.0,
    584.5,
    image=entry_image_12
)
entry_12 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_12.place(
    x=137.0,
    y=573.0,
    width=178.0,
    height=21.0
)

def update_entry_11(event):
    try:
        value_9 = float(entry_9.get())
        value_12 = float(entry_12.get())
        
        # Ensure that value_9 is always greater than value_12
        if value_9 <= value_12:
            entry_11.delete(0, "end")
            entry_11.insert(0, "Invalid")
            return

        result = value_9 / value_12
        entry_11.delete(0, "end")
        entry_11.insert(0, f"{result:.2f}")
        
    except ValueError:
        entry_11.delete(0, "end")

entry_9.bind("<KeyRelease>", update_entry_11)
entry_12.bind("<KeyRelease>", update_entry_11)


entry_image_13 = PhotoImage(
    file=relative_to_assets("entry_13.png"))
entry_bg_13 = canvas.create_image(
    226.0,
    446.5,
    image=entry_image_13
)
entry_13 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_13.place(
    x=137.0,
    y=435.0,
    width=178.0,
    height=21.0
)

entry_image_14 = PhotoImage(
    file=relative_to_assets("entry_14.png"))
entry_bg_14 = canvas.create_image(
    226.0,
    482.5,
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
    checkbox.place(x=138.0, y=370.0)  # Adjust the placement here
    entry_14.place(x=138.0, y=370.0, width=20.0, height=2.0)  # Keep the entry_15 placement here


checkbox_vars = [2]
for i in range(1):
    var = tk.IntVar()  # IntVar holds the value of the checkbox
    checkbox_vars.append(var)
    checkbox = tk.Checkbutton(window, text=f"", variable=var)
    checkbox.place(x=138.0, y=400.0)  # Adjust the placement here
    entry_14.place(x=138.0, y=400.0, width=20.0, height=2.0)  # Keep the entry_15 placement here


entry_14.place(
    x=137.0,
    y=471.0,
    width=178.0,
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

def save_parameters():
    parameters = {
        "Feedrate string": entry_1.get(),
        "Status": entry_2.get(),
        "input file name": entry_3.get(),
        "Output run file": entry_4.get(),
        "Q-Setting": entry_5.get(),
        "Z Approch": entry_6.get(),
        "Drawing width": entry_7.get(),
        "Drawing length": entry_8.get(),
        "Z Depth": entry_9.get(),
        "Comments": entry_10.get(),
        "Passes": entry_11.get(),
        "Depth Per Pass": entry_12.get(),
        "Pen On String 2": entry_13.get(),
        "Pen Off String ": entry_14.get(),
        #"Can Cycle No": entry_15.get(),
        #"Start Line No": entry_16.get(),
        #"Line Increment": entry_17.get(),
       
        # Add more entries here as needed
    }

    desktop_path = Path.home() / "figma/Tkinter-Designer-master (1)/output/build/assets/frame0/para" 
    file_path = desktop_path / "figma/Tkinter-Designer-master (1)/output/build/assets/frame0/para" 

    try:
        with open(file_path, "w") as f:
            for key, value in parameters.items():
                f.write(f"{key}: {value}\n")
        print("Parameters saved successfully.")
    except Exception as e:
        print("An error occurred:", e)

button_8.place(
    x=815.0,
    y=605.0,
    width=20.0,
    height=20.0
)

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
    x=685.0,
    y=605.0,
    width=47.0,
    height=23.0
)

'''button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)



button_10.place(
    x=315.0,
    y=0.0,
    width=97.0,
    height=26.0
)'''

import tkinter.simpledialog

# Create the menu for button_10
button_10_menu = Menu(window, tearoff=0)
button_10_menu.add_command(label="Can Cycle No", command=lambda: show_input_dialog("Suboption 1"))
button_10_menu.add_command(label="Start Line No", command=lambda: show_input_dialog("Suboption 2"))
button_10_menu.add_command(label="Line Increment", command=lambda: show_input_dialog("Suboption 3"))
button_10_menu.add_command(label="machining", command=lambda: show_input_dialog("Suboption 4"))
button_10_menu.add_command(label="3D print", command=lambda: show_input_dialog("Suboption 5"))

# Function to show an input dialog
def show_input_dialog(suboption):
    value = tkinter.simpledialog.askstring("Input", f"Enter value for {suboption}:", parent=window)
    if value is not None:
        print(f"Value entered for {suboption}: {value}")

# Create the Button for button_10
button_10 = Button(window, text="output setup")
button_10.place(x=160.0, y=0.0, width=97.0, height=26.0)

# Configure the button_10 to display the menu
def show_menu(event):
    button_10_menu.post(event.x_root, event.y_root)

button_10.bind("<Button-1>", show_menu)  # Bind left mouse button click to show the menu


window.resizable(True, True)
window.mainloop()