#1.	Create a simple Tkinter window with a title and fixed size.
import tkinter as tk

# Create the main window
root = tk.Tk()

# Set window title
root.title("My First Tkinter Window")

# Set fixed size (width x height)
root.geometry("400x300")

# Prevent resizing (fixed size)
root.resizable(False, False)

# Run the application
root.mainloop()

#2.	Design a GUI based basic calculator for performing basic arithmetic operations.
import tkinter as tk

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())   # Evaluate the expression entered
        output_label.config(text="Result: " + str(result))
    except Exception as e:
        output_label.config(text="Error: " + str(e))

# Create main window
root = tk.Tk()
root.title("Basic Calculator")
root.geometry("300x250")
root.resizable(False, False)

# Entry widget for expression
entry = tk.Entry(root, width=25, font=("Arial", 14))
entry.pack(pady=10)

# Buttons for operations
frame = tk.Frame(root)
frame.pack()

btn_add = tk.Button(frame, text="+", width=5, command=lambda: entry.insert(tk.END, "+"))
btn_sub = tk.Button(frame, text="-", width=5, command=lambda: entry.insert(tk.END, "-"))
btn_mul = tk.Button(frame, text="*", width=5, command=lambda: entry.insert(tk.END, "*"))
btn_div = tk.Button(frame, text="/", width=5, command=lambda: entry.insert(tk.END, "/"))

btn_add.grid(row=0, column=0, padx=5, pady=5)
btn_sub.grid(row=0, column=1, padx=5, pady=5)
btn_mul.grid(row=0, column=2, padx=5, pady=5)
btn_div.grid(row=0, column=3, padx=5, pady=5)

# Equal button
btn_equal = tk.Button(root, text="=", width=10, command=calculate)
btn_equal.pack(pady=10)

# Clear button
btn_clear = tk.Button(root, text="Clear", width=10, command=lambda: entry.delete(0, tk.END))
btn_clear.pack(pady=5)

# Output label
output_label = tk.Label(root, text="Result: ", font=("Arial", 12))
output_label.pack(pady=10)

# Run the application
root.mainloop()

#3.	Design a GUI for student registration for a course and store these details in a database. Use Tkinter for UI, SQLite/MySQL for database storage.
import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- Database Setup ---
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS student (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    sap_id TEXT NOT NULL,
    course TEXT NOT NULL,
    email TEXT NOT NULL
)
""")
conn.commit()

# --- Functions ---
def register_student():
    name = entry_name.get()
    sap_id = entry_sap.get()
    course = entry_course.get()
    email = entry_email.get()

    if not (name and sap_id and course and email):
        messagebox.showerror("Error", "All fields are required!")
        return

    cursor.execute("INSERT INTO student (name, sap_id, course, email) VALUES (?, ?, ?, ?)",
                   (name, sap_id, course, email))
    conn.commit()
    messagebox.showinfo("Success", f"Student {name} registered successfully!")

    # Clear fields
    entry_name.delete(0, tk.END)
    entry_sap.delete(0, tk.END)
    entry_course.delete(0, tk.END)
    entry_email.delete(0, tk.END)

def view_students():
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    output_text.delete("1.0", tk.END)
    for row in rows:
        output_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, SAP ID: {row[2]}, Course: {row[3]}, Email: {row[4]}\n")

# --- GUI Setup ---
root = tk.Tk()
root.title("Student Registration")
root.geometry("400x400")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root, width=30)
entry_name.pack()

tk.Label(root, text="SAP ID:").pack(pady=5)
entry_sap = tk.Entry(root, width=30)
entry_sap.pack()

tk.Label(root, text="Course:").pack(pady=5)
entry_course = tk.Entry(root, width=30)
entry_course.pack()

tk.Label(root, text="Email:").pack(pady=5)
entry_email = tk.Entry(root, width=30)
entry_email.pack()

# Buttons
tk.Button(root, text="Register", command=register_student).pack(pady=10)
tk.Button(root, text="View Students", command=view_students).pack(pady=5)

# Output area
output_text = tk.Text(root, height=10, width=45)
output_text.pack(pady=10)

# Run the application
root.mainloop()

# Close DB connection when program ends
conn.close()

#4.	Create a GUI based task manager where users can add, edit and remove tasks. Use Tkinter (buttons, listbox), SQLite/MySQL (task storage).
import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- Database Setup ---
conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS task (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    description TEXT NOT NULL
)
""")
conn.commit()

# --- Functions ---
def load_tasks():
    listbox.delete(0, tk.END)
    cursor.execute("SELECT * FROM task")
    for row in cursor.fetchall():
        listbox.insert(tk.END, f"{row[0]}: {row[1]}")

def add_task():
    task = entry.get()
    if task.strip() == "":
        messagebox.showerror("Error", "Task cannot be empty!")
        return
    cursor.execute("INSERT INTO task (description) VALUES (?)", (task,))
    conn.commit()
    entry.delete(0, tk.END)
    load_tasks()

def edit_task():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = int(selected.split(":")[0])
        new_task = entry.get()
        if new_task.strip() == "":
            messagebox.showerror("Error", "Task cannot be empty!")
            return
        cursor.execute("UPDATE task SET description=? WHERE id=?", (new_task, task_id))
        conn.commit()
        entry.delete(0, tk.END)
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task to edit!")

def delete_task():
    try:
        selected = listbox.get(listbox.curselection())
        task_id = int(selected.split(":")[0])
        cursor.execute("DELETE FROM task WHERE id=?", (task_id,))
        conn.commit()
        load_tasks()
    except:
        messagebox.showerror("Error", "Select a task to delete!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, width=30)
entry.pack(pady=10)

# Buttons
frame = tk.Frame(root)
frame.pack()

btn_add = tk.Button(frame, text="Add Task", width=10, command=add_task)
btn_edit = tk.Button(frame, text="Edit Task", width=10, command=edit_task)
btn_delete = tk.Button(frame, text="Delete Task", width=10, command=delete_task)

btn_add.grid(row=0, column=0, padx=5)
btn_edit.grid(row=0, column=1, padx=5)
btn_delete.grid(row=0, column=2, padx=5)

# Listbox to display tasks
listbox = tk.Listbox(root, width=50, height=15)
listbox.pack(pady=10)

# Load tasks initially
load_tasks()

# Run the application
root.mainloop()

# Close DB connection when program ends
conn.close()


#5.	Design a login and signup authentication system.
import tkinter as tk
from tkinter import messagebox
import sqlite3

# --- Database Setup ---
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
""")
conn.commit()

# --- Functions ---
def signup():
    username = entry_username.get()
    password = entry_password.get()

    if not (username and password):
        messagebox.showerror("Error", "All fields are required!")
        return

    try:
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        messagebox.showinfo("Success", "Signup successful! You can now log in.")
        entry_username.delete(0, tk.END)
        entry_password.delete(0, tk.END)
    except sqlite3.IntegrityError:
        messagebox.showerror("Error", "Username already exists!")

def login():
    username = entry_username.get()
    password = entry_password.get()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    row = cursor.fetchone()

    if row:
        messagebox.showinfo("Success", f"Welcome, {username}!")
    else:
        messagebox.showerror("Error", "Invalid username or password!")

# --- GUI Setup ---
root = tk.Tk()
root.title("Login & Signup System")
root.geometry("350x250")
root.resizable(False, False)

# Labels and Entries
tk.Label(root, text="Username:").pack(pady=5)
entry_username = tk.Entry(root, width=30)
entry_username.pack()

tk.Label(root, text="Password:").pack(pady=5)
entry_password = tk.Entry(root, width=30, show="*")
entry_password.pack()

# Buttons
frame = tk.Frame(root)
frame.pack(pady=20)

btn_login = tk.Button(frame, text="Login", width=10, command=login)
btn_signup = tk.Button(frame, text="Signup", width=10, command=signup)

btn_login.grid(row=0, column=0, padx=10)
btn_signup.grid(row=0, column=1, padx=10)

# Run the application
root.mainloop()

# Close DB connection when program ends
conn.close()


