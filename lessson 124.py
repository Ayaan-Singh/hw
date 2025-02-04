from tkinter import *

root = Tk()
root.title("Length Converter")
root.geometry("400x400")

def convert():
    inches = entry.get()
    cm = float(inches) * 2.54
    result_label.config(f"{cm} cm")

entry = Entry(root)
entry.pack()

button = Button(root, text="Convert", command=convert)
button.pack()

result_label = Label(root, text="")
result_label.pack()

root.mainloop()
