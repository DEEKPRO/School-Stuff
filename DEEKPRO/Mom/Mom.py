from tkinter import Tk, Label, Entry

root = Tk()
root.title("Mom")
root.geometry("400x300")

label = Label(root, text="Hello, Mom!", font=("Arial", 24))
label.pack(pady=50)
entry = Entry(root, font=("Arial", 16))
entry.pack(pady=10)
root.mainloop()