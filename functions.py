# Imports
import tkinter as tk
from functools import partial


# Create function to add/create tasks
def add_task(input_object, to_do_frame, event=None):
    task_entry = input_object.get()
    if task_entry != "":
        task_label = tk.Label(master=to_do_frame, text=task_entry)
        task_label.pack(padx=2, pady=2)
        task_label.bind("<Button-3>", partial(delete_task, task_label))
        input_object.delete(0, tk.END)


def delete_task(task, event=None):
    task.destroy()