import tkinter as tk

def add_task(input_object, to_do_frame, event=None):
    task_entry = input_object.get()
    if task_entry != "":
        task_label = tk.Label(master=to_do_frame, text=task_entry)
        task_label.pack(padx=2, pady=2)
        input_object.delete(0, tk.END)
