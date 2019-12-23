import tkinter as tk

counter = 0


def onClick():
    print("You clicked the button")
    global counter
    counter += 1
    label["text"] = f"Button was clicked {counter} times"


def hello():
    print("Some menu action was performed")


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry('640x480')
    window.title = "My first tkinter app"

    menubar = tk.Menu(window)

    # create a pulldown menu, and add it to the menu bar
    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Open", command=hello)
    filemenu.add_command(label="Save", command=hello)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=window.quit)
    menubar.add_cascade(label="File", menu=filemenu)

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=hello)
    menubar.add_cascade(label="Help", menu=helpmenu)

    # display the menu
    window.config(menu=menubar)

    but_widget = tk.Button(window, text="Hello RCS", command=onClick)
    but_widget.pack()
    label = tk.Label(window, text='Some text:')
    label.pack()
    tk.mainloop()
