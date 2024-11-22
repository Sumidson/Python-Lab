import tkinter as tk
from tkinter import messagebox
import sqlite3
from datetime import datetime

# Connect to SQLite database
conn = sqlite3.connect('expenses.db')
c = conn.cursor()

# Create table for expenses
c.execute('''CREATE TABLE IF NOT EXISTS expenses
             (date TEXT, category TEXT, amount REAL)''')
conn.commit()

def add_expense():
    date = date_entry.get()
    category = category_entry.get()
    amount = amount_entry.get()
    
    if not date or not category or not amount:
        messagebox.showwarning("Input Error", "All fields are required!")
        return
    
    try:
        amount = float(amount)
    except ValueError:
        messagebox.showwarning("Input Error", "Amount must be a number!")
        return
    
    c.execute("INSERT INTO expenses VALUES (?, ?, ?)", (date, category, amount))
    conn.commit()
    
    date_entry.delete(0, tk.END)
    category_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    messagebox.showinfo("Success", "Expense added successfully!")

def show_summary():
    month = month_entry.get()
    
    if not month:
        messagebox.showwarning("Input Error", "Month is required!")
        return
    
    c.execute("SELECT SUM(amount) FROM expenses WHERE date LIKE ?", (month + '%',))
    total = c.fetchone()[0]
    
    if total is None:
        total = 0
    
    summary_label.config(text=f"Total expenses for {month}: ₹{total:.2f}")

# Create main window
root = tk.Tk()
root.title("Expense Tracker")

# Date entry
tk.Label(root, text="Date (YYYY-MM-DD)").grid(row=0, column=0, padx=10, pady=10)
date_entry = tk.Entry(root)
date_entry.grid(row=0, column=1, padx=10, pady=10)

# Category entry
tk.Label(root, text="Category").grid(row=1, column=0, padx=10, pady=10)
category_entry = tk.Entry(root)
category_entry.grid(row=1, column=1, padx=10, pady=10)

# Amount entry
tk.Label(root, text="Amount").grid(row=2, column=0, padx=10, pady=10)
amount_entry = tk.Entry(root)
amount_entry.grid(row=2, column=1, padx=10, pady=10)

# Add expense button
add_button = tk.Button(root, text="Add Expense", command=add_expense)
add_button.grid(row=3, column=0, columnspan=2, pady=10)

# Month entry for summary
tk.Label(root, text="Month (YYYY-MM)").grid(row=4, column=0, padx=10, pady=10)
month_entry = tk.Entry(root)
month_entry.grid(row=4, column=1, padx=10, pady=10)

# Show summary button
summary_button = tk.Button(root, text="Show Summary", command=show_summary)
summary_button.grid(row=5, column=0, columnspan=2, pady=10)

# Label to display summary
summary_label = tk.Label(root, text="")
summary_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when the application closes
conn.close()
