import tkinter as tk

def navbarCreation(secFrame):
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