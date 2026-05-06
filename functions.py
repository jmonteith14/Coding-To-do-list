# Imports
import tkinter as tk
from functools import partial


# Create function to add/create tasks
def add_task(input_object, to_do, today, in_progress, completed, event=None):
    frame_list = [to_do, today, in_progress, completed]
    frame = 0
    task_entry = input_object.get()
    if task_entry != "":
        task_label = tk.Label(master=frame_list[0], text=task_entry)
        task_label.pack(padx=2, pady=2)
        task_label.bind("<Button-3>", partial(delete_task, task_label))
        task_label.bind("<Button-1>", partial(move_task, task_label, frame_list, frame+1))
        input_object.delete(0, tk.END)

def move_task(task, frame_list, frame, event=None):
    if frame != len(frame_list):
        new_task = task.cget("text")
        task_label = tk.Label(master=frame_list[frame], text=new_task)
        task_label.pack(padx=2, pady=2)
        task_label.bind("<Button-3>", partial(delete_task, task_label))
        task_label.bind("<Button-1>", partial(move_task, task_label, frame_list, frame+1))
        delete_task(task)

def delete_task(task, event=None):
    task.destroy()

