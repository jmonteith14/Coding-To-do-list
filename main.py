import tkinter as tk
from functools import partial
import functions as func

root = tk.Tk()
root.title("NovaKanban")
root.geometry("1200x500")
root.configure(bg="#222222")

title_frame = tk.Frame(root)
title_label = tk.Label(master=title_frame, text="NovaKanban", font=("Sitka Heading Bold", 30))
title_label.pack()
title_frame.pack(side=tk.TOP, padx=5, pady=5)

to_do_frame = tk.Frame(root, bg="#464646", width=200, height=400)
to_do_label = tk.Label(master=to_do_frame, bg="#E3DB62", text='To-do', font=("Sitka Text Bold", 15))
to_do_label.pack(fill=tk.BOTH)
to_do_frame.pack(side=tk.LEFT, padx=10, pady=10)
to_do_frame.pack_propagate(False)

today_frame = tk.Frame(root, bg="#464646", width=200, height=400)
today_label = tk.Label(master=today_frame, bg="#BA62E3", text='Do Today', font=("Sitka Text Bold", 15))
today_label.pack(fill=tk.BOTH)
today_frame.pack(side=tk.LEFT, padx=10, pady=10)
today_frame.pack_propagate(False)

in_progress_frame = tk.Frame(root, bg="#464646", width=200, height=400)
in_progress_label = tk.Label(master=in_progress_frame, bg="#6284E3", text='In Progress', font=("Sitka Text Bold", 15))
in_progress_label.pack(fill=tk.BOTH)
in_progress_frame.pack(side=tk.LEFT, padx=10, pady=10)
in_progress_frame.pack_propagate(False)

completed_frame = tk.Frame(root, bg="#464646", width=200, height=400)
completed_label = tk.Label(master=completed_frame, bg="#62E373", text='Completed', font=("Sitka Text Bold", 15))
completed_label.pack(fill=tk.BOTH)
completed_frame.pack(side=tk.LEFT, padx=10, pady=10)
completed_frame.pack_propagate(False)

input_task = tk.Entry(root, width=30, relief=tk.SUNKEN)
input_task.pack(side=tk.TOP, padx=10, pady=10)
input_task.bind("<Return>", partial(func.add_task, input_task, to_do_frame))

input_button = tk.Button(root, text="Add Task", command=partial(func.add_task, input_task, to_do_frame))
input_button.pack(side=tk.TOP, padx=10, pady=10)


root.mainloop()
