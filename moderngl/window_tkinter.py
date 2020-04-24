# based on moderngl/examples/window_tkinter.py

import tkinter as tk

import moderngl
import numpy as np

from tkinter_framebuffer import FramebufferImage
from renderer_example import HelloWorld2D, PanTool

ctx = moderngl.create_standalone_context()

canvas = HelloWorld2D(ctx)
pan_tool = PanTool()


def vertices():
    x = np.linspace(-1.0, 1.0, 50)
    y = np.random.rand(50) - 0.5
    r = np.ones(50)
    g = np.zeros(50)
    b = np.zeros(50)
    a = np.ones(50)
    return np.dstack([x, y, r, g, b, a])


verts = vertices()


def update(evt):
    if evt.type == tk.EventType.ButtonPress:
        pan_tool.start_drag(evt.x / size[0], evt.y / size[1])
    if evt.type == tk.EventType.Motion:
        pan_tool.dragging(evt.x / size[0], evt.y / size[1])
    if evt.type == tk.EventType.ButtonRelease:
        pan_tool.stop_drag(evt.x / size[0], evt.y / size[1])
    canvas.pan(pan_tool.value)

    with tkfbo:
        ctx.clear()
        canvas.plot(verts)

root = tk.Tk()
root.title("프로그람")
size = (300, 200) # root.winfo_screenwidth(), root.winfo_screenheight()-50)
tkfbo = FramebufferImage(root, ctx, size)

lbl = tk.Label(root, image=tkfbo)
lbl.bind("<ButtonPress-1>", update)
lbl.bind("<ButtonRelease-1>", update)
lbl.bind('<Motion>', update)
lbl.pack()

def btn_click():
    print("아야")

btn = tk.Button(root, text="눌러바", command=btn_click)
btn.pack()

def exit(event):
    root.destroy()

root.bind("<Escape>", exit)

# root.attributes('-fullscreen', True)

root.mainloop()
