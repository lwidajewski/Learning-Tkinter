import tkinter as tk
import tkinter as ttk


class Scrollbar:

    def __init__(self, canvas, canvasWindow):
        self.canvas = canvas
        self.canvasWindow = canvasWindow

    # SCROLLBAR functions
    # https://www.youtube.com/watch?v=0WafQCaok6g
    # there is a comment on this video that shows how to bind MouseWheel
    def mouseScroll(self, event):
        self.canvas.yview_scroll(-1*int((event.delta/120)), "units")

    def configureFrame(self, event):
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

    def configureCanvas(self, event):
        self.canvas.itemconfig(self.canvasWindow, width=event.width)

    def scrollBar(root):
        # frame one
        firstFrame = tk.Frame(root)
        firstFrame.pack(fill="both", expand=True)

        # canvas creation --> you can put scrollbars on a canvas
        canvas = tk.Canvas(firstFrame)
        canvas.pack(side="left", fill="both", expand=True)

        # actual scrollbar creation
        scrollbar = ttk.Scrollbar(firstFrame, orient="vertical", command=canvas.yview)
        scrollbar.pack(side="right", fill="y")

        # configure canvas
        canvas.configure(yscrollcommand=scrollbar.set)

        # create frame inside canvas
        secFrame = tk.Frame(canvas)

        # add frame to a window inside canvas
        canvasWindow = canvas.create_window((0, 0), window=secFrame, anchor="nw")

        # create instance of scrollbar
        bar = Scrollbar(canvas, canvasWindow)

        # bindings
        canvas.bind("<Configure>", bar.configureCanvas)
        secFrame.bind("<Configure>", bar.configureFrame)
        canvas.bind_all("<MouseWheel>", bar.mouseScroll)

        return secFrame
