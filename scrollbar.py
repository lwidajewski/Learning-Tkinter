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
