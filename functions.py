import tkinter as tk

def add_task(input_object, to_do_frame):
    entry = input_object.get()
    # print(entry)
    entry_label = tk.Label(master=to_do_frame, text=entry)
    entry_label.pack()
    input_object.delete(0, tk.END)



