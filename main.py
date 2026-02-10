# IMPORTS
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox

from scrollbar import Scrollbar
from moveableListbox import moveItems
from navbar import navbarCreation


# ----------------------------------
# INITIAL WINDOW CREATION
# ----------------------------------
root = tk.Tk() # intialize class, create new root window

root.title("Habits Tracker") # change titlebar of window

root.state("zoomed") # full screen the window


# ----------------------------------
# SCROLLBAR
# ----------------------------------
secFrame = Scrollbar.scrollBar(root)


# ----------------------------------
# NAVBAR
# ----------------------------------
navbarCreation(secFrame)


# ----------------------------------
# PAGE CONTENT
# ----------------------------------
# create page title frame
pageTitle = tk.Frame(secFrame, background="white", pady=25)
pageTitle.pack(fill="both")

# create title from the input data page in ITI-200
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
    box = tk.Entry(frmContent, width=50)
    # placeholder text
    if (i == 1):
        placeholder = "Enter your name..."
    else:
        placeholder = "Enter your hours..."

    def addPlaceholder(placeholder):
        if (box.get() == ""):
            box.insert(0, placeholder)
            box.configure(foreground="gray")

    def onEntryFocusIn(event): 
        if (box.cget("fg") == "gray"): 
            box.delete(0, tk.END) 
            # whatever the user types will be black
            box.configure(foreground="black")

    # on click out of box
    def onExitFocusOut(event):
        addPlaceholder(placeholder)

    # add initial placeholders
    addPlaceholder(placeholder)

    # bind boxes adding additional functionality to entryboxes
    box.bind("<FocusIn>", onEntryFocusIn)
    box.bind("<FocusOut>", onExitFocusOut)
    # place box on correct row
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


# ----------------------------------
# SUBMIT BUTTON
# ----------------------------------
# https://www.w3schools.com/python/python_dictionaries.asp --> dictionaries
entryBoxes = {
        "Name": nameBox, 
        "Sleep": sleepBox, 
        "Credits": creditBox, 
        "Study": studyBox, 
        "Exercise": exerciseBox, 
        "Screen": screenBox
    }
submitBtn = tk.Button(frmContent, text="Submit", cursor="hand2", command=lambda: submit(entryBoxes, listBox))
submitBtn.grid(column=0, row=15, sticky="w", pady=15)


# call this function to call the other functions below, easier to debug and add more functionality to a single button
def submit(entries, lb):
    # get input from user
    data = getText(entries)
    if not inputValidation(data):
        return
    print(data)
    listData = getListBox(lb)
    # open a new window to display output from eventual AI -- pass in the values you got earlier
    openNewWindow()


# ----------------------------------
# Functions to Get data from Entry Boxes and Listbox
# ----------------------------------
# gets the text from all the entry boxes
def getText(entries):
    data = {} # create new dictionary to put values in
    for key, entry in entries.items():
        # get values stripping whitespace
        data[key] = entry.get().strip()
    return data

# gets everything listed in the listbox
def getListBox(lb):
    # from start to end
    values = lb.get(0, tk.END)
    print(values) # print to make sure it came through correctly

# ----------------------------------
# Error message function
# ----------------------------------
# display popup error message --> https://docs.python.org/3/library/tkinter.messagebox.html#messagebox-icons
def errorMessage(message):
    messagebox.showerror(title="Input Error", message=message)

# ----------------------------------
# Function to validate input
# ----------------------------------
def inputValidation(data):
    # check if name is empty
    if not data["Name"]:
        errorMessage("Name cannot be empty")
        return False

    for key in ["Sleep", "Credits", "Study", "Exercise", "Screen"]:
        # check if other entryboxes are empty
        if not data[key]:
            errorMessage(f"{key} cannot be empty")
            return False
        try:
            # check if inputted value is a number
            value = float(data[key]) # this goes to the except if it can't convert to float
            # check if values inputted is negative
            if value < 0:
                errorMessage(f"{key} cannot be negative")
                return False
        except ValueError:
            errorMessage(f"{key} must be a number")
            return False
    return True

# ----------------------------------
# Opens a new window on submit button click if input is correct
# ----------------------------------
def openNewWindow():
    root.withdraw() # hide the root window for now --> destroying it would break the program
    #root.destroy()

    # create a new window 
    # https://www.youtube.com/watch?v=qC3FYdpJI5Y
    # https://www.tutorialspoint.com/how-to-open-a-new-window-by-the-user-pressing-a-button-in-a-tkinter-gui
    top = tk.Toplevel()
    top.state("zoomed")
    top.title("Output Window")
    # placeholder label for now
    lblOutput = ttk.Label(top, text="Hello World!", font=("Segoe UI", 12))
    lblOutput.pack(side="top")

    def closeTop():
        top.destroy()
        root.deiconify()
        root.state("zoomed")

    btnClose = tk.Button(top, text="Close", cursor="hand2", command=closeTop)
    btnClose.pack(side="top")


# makes sure application keeps running until closed or stopped
root.mainloop()
