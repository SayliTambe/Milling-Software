import tkinter as tk
from tkinter import filedialog
import ezdxf
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def open_dxf_file():
    file_path = filedialog.askopenfilename(filetypes=[("DXF files", "*.dxf")])
    if file_path:
        read_dxf_file(file_path)


def read_dxf_file(file_path):
    doc = ezdxf.readfile(file_path)
    msp = doc.modelspace()

    # Initialize a matplotlib figure
    fig, ax = plt.subplots()
    ax.set_aspect('equal')

    # Plot entities from the DXF file
    for entity in msp:
        if entity.dxftype() in ['LINE', 'LWPOLYLINE', 'CIRCLE']:
            if entity.dxftype() == 'LINE':
                start = entity.dxf.start
                end = entity.dxf.end
                ax.plot([start[0], end[0]], [start[1], end[1]], color='blue')
            elif entity.dxftype() == 'LWPOLYLINE':
                points = list(entity.points())
                x, y = zip(*points)
                ax.plot(x, y, color='blue')
            elif entity.dxftype() == 'CIRCLE':
                center = entity.dxf.center
                radius = entity.dxf.radius
                circle = plt.Circle((center[0], center[1]), radius, color='blue', fill=False)
                ax.add_patch(circle)

    # Show the plot on the Tkinter window
    canvas = FigureCanvasTkAgg(fig, master=root)
    canvas.draw()
    canvas.get_tk_widget().pack()


# Create the main application window
root = tk.Tk()
root.title("DXF Viewer")