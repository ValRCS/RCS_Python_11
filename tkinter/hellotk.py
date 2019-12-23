import tkinter

if __name__ == "__main__":
    window = tkinter.Tk()
    window.title = "My first tkinter app"
    but_widget = tkinter.Button(window, text="Hello RCS")
    but_widget.pack()
    tkinter.mainloop()
