import tkinter as tk
from functools import partial
import functions as func

root = tk.Tk()
root.title("Coding To-Do List")
root.geometry("1000x500")
root.configure(bg="#424242")

to_do_frame = tk.Frame(root, bg="#E3DB62", width=200, height=400)
to_do_label = tk.Label(master=to_do_frame, text='To-do', font="bold")
to_do_label.pack(fill=tk.BOTH)
to_do_frame.pack(side=tk.LEFT, padx=10, pady=10)
to_do_frame.pack_propagate(False)

in_progress_frame = tk.Frame(root, bg="#6284E3", width=200, height=400)
in_progress_label = tk.Label(master=in_progress_frame, text='In Progress', font="bold")
in_progress_label.pack(fill=tk.BOTH)
in_progress_frame.pack(side=tk.LEFT, padx=10, pady=10)
in_progress_frame.pack_propagate(False)

completed_frame = tk.Frame(root, bg="#62E373", width=200, height=400)
completed_label = tk.Label(master=completed_frame, text='Completed', font="bold")
completed_label.pack(fill=tk.BOTH)
completed_frame.pack(side=tk.LEFT, padx=10, pady=10)
completed_frame.pack_propagate(False)

dropped_frame = tk.Frame(root, bg="#E37362", width=200, height=400)
dropped_label = tk.Label(master=dropped_frame, text='Dropped', font="bold")
dropped_label.pack(fill=tk.BOTH)
dropped_frame.pack(side=tk.LEFT, padx=10, pady=10)
dropped_frame.pack_propagate(False)

input_task = tk.Entry(root, width=30, relief=tk.SUNKEN)
input_task.pack(side=tk.TOP, padx=10, pady=10)
input_task.bind("<Return>", partial(func.add_task, input_task, to_do_frame))

input_button = tk.Button(root, text="Add Task", command=partial(func.add_task, input_task, to_do_frame))
input_button.pack(side=tk.TOP, padx=10, pady=10)

root.mainloop()
