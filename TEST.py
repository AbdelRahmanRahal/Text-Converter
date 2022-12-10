from tkinter import *

# ----- WINDOW SETTINGS -----
wndw = Tk()
wndw.title("Test title!")
wndw.geometry("800x450")
wndw.configure(bg="#D5E5ED")

# ----- TITLE -----
titlelabel = Label(master=wndw, text="Text Converter\n", font=("Segoe UI", 22, "bold", "underline"), fg="#001061", bg="#D5E5ED")
titlelabel.grid(column=1, columnspan=4)

# ----- BODY -----
# ----- USERINPUT -----
boxlabel = Label(master=wndw, text="Enter text to convert:  ", font=("Segoe UI", 16), fg="#001061", bg="#D5E5ED")
boxlabel.grid(column=0, row=1)

txtbox = Entry(master=wndw, font=("Segoe UI", 16), fg="#001061", width=35)
txtbox.grid(column=1, row=1, columnspan=4)

linebreak = Label(master=wndw, text="", bg="#D5E5ED")
linebreak.grid(column= 0, row=2, columnspan=5)

# ----- BUTTONS -----
TCbttn = Button(text="Title Case", font=("Segoe UI", 11), fg="#001061")
TCbttn.grid(column=1, row=3)
UCbttn = Button(text="UPPERCASE", font=("Segoe UI", 11), fg="#001061")
UCbttn.grid(column=2, row=3)
LCbttn = Button(text="lowercase", font=("Segoe UI", 11), fg="#001061")
LCbttn.grid(column=3, row=3)
ACbttn = Button(text="AlT CaSe", font=("Segoe UI", 11), fg="#001061")
ACbttn.grid(column=4, row=3)

# ----- PROGRAM INITIATION -----
wndw.mainloop()