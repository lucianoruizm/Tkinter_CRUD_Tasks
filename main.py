import tkinter as tk
from tkinter import messagebox


class Login(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Login")
        self.master.geometry("300x150")
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.master, text="Username").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.master)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.master, text="Password").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.master, show="*")
        self.password_entry.grid(row=1, column=1)

        self.login_button = tk.Button(self.master, text="Login", command=self.login)
        self.login_button.grid(row=2, column=1)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "admin" and password == "admin":
            self.master.withdraw()
            main_menu = tk.Toplevel(self.master)
            main_menu.title("Main Menu")
            main_menu.geometry("300x150")
            main_menu.resizable(False, False)
            MainMenu(master=main_menu)
            
        else:
            messagebox.showerror("Error", "Invalid username or password")


class MainMenu(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.master.title("Main Menu")
        self.master.geometry("300x150")
        self.master.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        self.add_task_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_task_button.grid(row=0, column=0)

        self.edit_task_button = tk.Button(self.master, text="Edit Task", command=self.edit_task)
        self.edit_task_button.grid(row=0, column=1)

        self.delete_task_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_task_button.grid(row=1, column=0)

        self.filter_task_button = tk.Button(self.master, text="Filter Task", command=self.filter_task)
        self.filter_task_button.grid(row=1, column=1)

    def add_task(self):
       add_task_form = AddTaskForm()

    def edit_task(self):
       select_task_form = EditTaskForm("edit")

    def delete_task(self):
       select_task_form = DeleteTaskForm("delete")

    def filter_task(self):
       filter_task_form = FilterTaskForm()


class AddTaskForm(tk.Toplevel):
   def __init__(self):
       super().__init__()
       self.title("Add Task")
       self.geometry("300x150")
       self.resizable(False, False)
       self.create_widgets()

   def create_widgets(self):
       tk.Label(self, text="Task Name").grid(row=0, column=0)
       self.task_name_entry = tk.Entry(self)
       self.task_name_entry.grid(row=0, column=1)

       tk.Label(self, text="Task Description").grid(row=1, column=0)
       self.task_description_entry = tk.Entry(self)
       self.task_description_entry.grid(row=1, column=1)

       self.save_button = tk.Button(self, text="Save", command=self.save_task)
       self.save_button.grid(row=2, column=1)

   def save_task(self):
       task_name = self.task_name_entry.get()
       task_description = self.task_description_entry.get()

       print(f"{task_name}, {task_description}")

class EditTaskForm(tk.Toplevel):
   def __init__(self, task):
       super().__init__()
       self.title("Edit Task")
       self.geometry("300x150")
       self.resizable(False, False)
       self.task = task
       self.create_widgets()

   def create_widgets(self):
       tk.Label(self, text="Task Name").grid(row=0, column=0)
       self.task_name_entry = tk.Entry(self, text=self.task["name"])
       self.task_name_entry.grid(row=0, column=1)

       tk.Label(self, text="Task Description").grid(row=1, column=0)
       self.task_description_entry = tk.Entry(self, text=self.task["description"])
       self.task_description_entry.grid(row=1, column=1)

       self.save_button = tk.Button(self, text="Save", command=self.save_task)
       self.save_button.grid(row=2, column=1)

   def save_task(self):
       task_name = self.task_name_entry.get()
       task_description = self.task_description_entry.get()

       print(f"{task_name}, {task_description}")

class DeleteTaskForm(tk.Toplevel):
   def __init__(self, task):
       super().__init__()
       self.title("Delete Task")
       self.geometry("300x150")
       self.resizable(False, False)
       self.task = task
       self.create_widgets()

   def create_widgets(self):
       tk.Label(self, text=f"Do you want to delete the task {self.task['name']}?").grid(row=0, column=0, columnspan=2)

       self.yes_button = tk.Button(self, text="Yes", command=self.delete_task)
       self.yes_button.grid(row=1, column=0)

       self.no_button = tk.Button(self, text="No", command=self.destroy)
       self.no_button.grid(row=1, column=1)

   def delete_task(self):
       print("Delete task")

class FilterTaskForm(tk.Toplevel):
   def __init__(self):
       super().__init__()
       self.title("Filter Task")
       self.geometry("300x150")
       self.resizable(False, False)
       self.create_widgets()

   def create_widgets(self):
       tk.Label(self, text="Filter by").grid(row=0, column=0)
       self.filter_option = tk.StringVar(self)
       self.filter_option.set("name")

       self.filter_menu = tk.OptionMenu(self, self.filter_option, "name", "description")
       self.filter_menu.grid(row=0, column=1)

       tk.Label(self, text="Value").grid(row=1, column=0)
       self.filter_value_entry = tk.Entry(self)
       self.filter_value_entry.grid(row=1, column=1)

       self.search_button = tk.Button(self, text="Search", command=self.search_task)
       self.search_button.grid(row=2, column=1)

   def search_task(self):
       filter_option = self.filter_option.get()
       filter_value = self.filter_value_entry.get()

       print("Search Task")

root = tk.Tk()
login = Login(root)
login.mainloop()

