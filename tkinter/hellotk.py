import tkinter as tk

counter = 0


def onClick():
    print("You clicked the button")
    global counter
    counter += 1
    label["text"] = f"Button was clicked {counter} times"


if __name__ == "__main__":
    window = tk.Tk()
    window.geometry('640x480')
    window.title = "My first tkinter app"
    but_widget = tk.Button(window, text="Hello RCS", command=onClick)
    but_widget.pack()
    label = tk.Label(window, text='Some text:')
    label.pack()
    tk.mainloop()
