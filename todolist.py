import tkinter as tk

tasks = []

def add_task():
    task_text = task_entry.get()
    if task_text:
        tasks.append(task_text)
        task_entry.delete(0, tk.END)
        update_task_list()

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        tasks.pop(selected_index)
        update_task_list()
    except IndexError:
        pass

def update_task_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        task_listbox.insert(tk.END, task)

root = tk.Tk()
root.title("To-Do List")
root.geometry("500x600")
root.configure(bg="#282828")

title_label = tk.Label(root, text="To-Do List", font=("Segoe UI", 24, "bold"), fg="#FFFFFF", bg="#282828")
title_label.pack(pady=20)

task_entry = tk.Entry(root, width=30, font=("Segoe UI", 14), fg="#FFFFFF", bg="#3C3C3C")
task_entry.pack(padx=20, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, font=("Segoe UI", 14), bg="#6C63FF", fg="#FFFFFF", activebackground="#5A54D6", activeforeground="#FFFFFF")
add_button.pack(padx=20, pady=10)

task_listbox = tk.Listbox(root, width=40, height=15, font=("Segoe UI", 14), bg="#3C3C3C", fg="#FFFFFF", selectbackground="#6C63FF", selectforeground="#FFFFFF")
task_listbox.pack(padx=20, pady=10)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, font=("Segoe UI", 14), bg="#6C63FF", fg="#FFFFFF", activebackground="#5A54D6", activeforeground="#FFFFFF")
delete_button.pack(padx=20, pady=10)

root.mainloop()