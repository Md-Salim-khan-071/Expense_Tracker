# Create the main window
root = tk.Tk()   # root is a variable name that referes to the window

# Set the window title
root.title("Expense Tracker Dashboard")

# Set the window size (Width x Height)
root.geometry("1000x600")


# creating the table to view data 

columns = ("ID" , "Date" , "Amount" , "Category" , "Description")

table = ttk.Treeview(root , columns=columns , show="headings")

for column in columns:
    table.heading(column, text="column")

table.pack(fill="both", expand=True)

table.insert("", "end", values=(1, "2026-03-28", 250, "Food", "Lunch"))
table.insert("", "end", values=(1, "2026-03-28", 500, "Food", "dinner"))


# buttons 

add_button = tk.Button(root , text=" + Add Expense", command=add_expenses)
add_button.pack(pady = 10)

view_button = tk.Button(root , text="View Expenses", command=view_expenses)
view_button.pack(pady = 10)

total_button = tk.Button (root , text="total expenses",command=show_total_expense) 
total_button.pack(pady = 10)

delete_button = tk.Button(root , text=" delete expenses", command=delete_expenses)
delete_button.pack(pady = 10)


# Start the application
root.mainloop()