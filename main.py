# IMPORTS
import tkinter as tk
import tkinter.ttk as ttk

from scrollbar import Scrollbar
from moveableListbox import moveItems


# INITIAL WINDOW CREATION
root = tk.Tk() # intialize class, create new root window

root.title("Habits Tracker") # change titlebar of window

root.state("zoomed") # full screen the window


# SCROLLBAR

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


# NAVBAR

# navbar background color
navBlue = "#0d6dfa"

# navbar creation, color, and position
navBar = tk.Frame(secFrame, background=navBlue, height=50)
navBar.pack(side="top", fill="x")

# before buttons add habit tracker title -- https://tkdocs.com/widgets/label.html --> labels
companyTitle = tk.Label(navBar, text="Habits Tracker", background=navBlue, fg="white", font=("Segoe UI", 16), padx=15, pady=10)
companyTitle.pack(side="left")

# navbar buttons -- https://tkdocs.com/widgets/button.html --> buttons
navButtons = ["Home", "Input Data", "View Goals", "Great Tips"]
for btnName in navButtons:
    newBtn = tk.Button(navBar, text=btnName, bg=navBlue, fg="white", font=("Segoe UI", 12), padx=15, pady=10, 
                       relief="flat", activebackground=navBlue, activeforeground="white", cursor="hand2")
    newBtn.pack(side="left")
    # when mouse enters and leaves buttons make text certain color
    newBtn.bind("<Enter>", lambda event: event.widget.config(fg="#c2dbfe"))
    newBtn.bind("<Leave>", lambda event: event.widget.config(fg="white"))


# PAGE CONTENT

# create page title frame
pageTitle = tk.Frame(secFrame, background="white", pady=25)
pageTitle.pack(fill="both")

# create title from input data page
labelTitle = ttk.Label(pageTitle, text="Tell Us About Your Habits", font=("Segoe UI", 32, "bold"), background="white")
labelTitle.pack(side="top")


# add in additional page content -- labels, response boxes, etc. into new frame(s) to neatly align
# outer frame -- this is for the background, if not here the background won't be white
frmBackground = tk.Frame(secFrame, background="white")
frmBackground.pack(fill="both", expand=True)

# actual frame the text boxes and labels go into -- this frame is inside frmBackground
frmContent = tk.Frame(frmBackground, background="white", pady=15)
frmContent.pack(anchor="center")

# creates label from text given and puts it in the grid from the location given
def createLabel(text, i):
    label = ttk.Label(frmContent, text=text, font=("Segoe UI", 12), background="white")
    label.grid(column=0, row=i, sticky="w", pady=15)
    return label

# create box and put on grid from the location given
def createBox(i):
    box = ttk.Entry(frmContent, width=50)
    # placeholder text
    box.insert(0, "0")

    # gets called once for each box
    def clearBoxPlaceholder(event):
        if box.get() == "0":
            box.delete(0, tk.END)

    # clear placeholder inside box when box is clicked
    box.bind("<FocusIn>", clearBoxPlaceholder)
    box.grid(column=0, row=i, sticky="w")
    return box

# name
lblName = createLabel("What is your name", 0)
nameBox = createBox(1)

# sleep
lblSleep = createLabel("How much sleep do you get each night?", 2)
sleepBox = createBox(3)

# credit hours
lblCredit = createLabel("How many credit hours are you enrolled in right now?", 4)
creditBox = createBox(5)

# hours studied
lblStudy = createLabel("How many hours do you study per week?", 6)
studyBox = createBox(7)

# hours exercised
lblExercise = createLabel("How many hours do you exercise per week?", 8)
exerciseBox = createBox(9)

# avg screen time per day (hours)
lblScreen = createLabel("What is your average screen time per day?", 10)
screenBox = createBox(11)

# add in listbox for importance ranking of habits -- https://tkdocs.com/tutorial/morewidgets.html
lblImportance = createLabel("Rank the importance of the following habits to you:", 12)

listHabits = ["Sleep", "Studying", "Exercise", "Screen Time"]
listvar = tk.StringVar(value=listHabits)

listBox = tk.Listbox(frmContent, height=10, width=50, selectmode="single", 
                     disabledforeground="gray", font=("Segoe UI", 12), 
                     listvariable=listvar, activestyle="none")
listBox.grid(column=0, row=13, sticky="w", pady=15)

# move up button
upBtn = tk.Button(frmContent, text="Move Up", cursor="hand2", command=lambda: moveItems.moveUp(listBox))
upBtn.grid(column=0, row=14, sticky="w", pady=15)

# move down button
downBtn = tk.Button(frmContent, text="Move Down", cursor="hand2", command=lambda: moveItems.moveDown(listBox))
downBtn.grid(column=0, row=14, sticky="w", padx=75)


# SUBMIT BUTTON functionality

# call this function to call the other two functions below, easier to debug
def getContent(entries, lb):
    getText(entries)
    getListBox(lb)

# gets the text from all the entry boxes
def getText(entries):
    for key, entry in entries.items():
        print(key + ": " + entry.get())
        entry.delete(0, tk.END)

# gets everything listed in the listbox
def getListBox(lb):
    values = lb.get(0, tk.END)
    print(values)

# https://www.w3schools.com/python/python_dictionaries.asp --> dictionaries
entryBoxes = {
        "Name": nameBox, 
        "Sleep": sleepBox, 
        "Credits": creditBox, 
        "Study": studyBox, 
        "Exercise": exerciseBox, 
        "Screen": screenBox
    }
submitBtn = tk.Button(frmContent, text="Submit", cursor="hand2", command=lambda: getContent(entryBoxes, listBox))
submitBtn.grid(column=0, row=15, sticky="w", pady=15)


# makes sure application keeps running until closed or stopped
root.mainloop()
