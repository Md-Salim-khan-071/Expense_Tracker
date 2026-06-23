import tkinter as tk
from tkinter import ttk
import mysql.connector
# from logic import *
import logic

""" the dashboard specific functions """

# refreshing the table . reason : as we update the table , the updated table data is not automatically displayed , hence we refresh it using this function where we first delete all table table and re fetch it form datbase  
def refresh_table():
    #deleting table data 
    for item in table.get_children():
        table.delete(item)

    rows = logic.get_all_expenses()

    for row in rows:
        table.insert("","end",values=row)

# function to open a new  windo when the ADD button is clicked 
def open_add_window():
    add_window = tk.Toplevel(root)

    add_window.title("Add Expense" )
    add_window.geometry("400x300")

    # the frame in which all the entries will be there . for a more modular look 
    add_expense_frame = tk.Frame(add_window)
    add_expense_frame.columnconfigure(0 , weight=1)
    add_expense_frame.columnconfigure(1 , weight=1)

    date_label = tk.Label(add_expense_frame, text="Date(yyyy-mm-dd):" , font=("helvetica",12,"bold"),bg="#2C3E50",fg="white")
    date_label.grid(row=0 , column=0)
    date_entry = tk.Entry(add_expense_frame)
    date_entry.grid(row=0 , column=1)

    Amount_label = tk.Label(add_expense_frame, text="Amount:")
    Amount_label.grid(row=1 , column=0)
    Amount_entry = tk.Entry(add_expense_frame)
    Amount_entry.grid(row=1 , column=1)

    Category_label = tk.Label(add_expense_frame, text="Category:")
    Category_label.grid(row=2 , column=0)
    Category_entry = tk.Entry(add_expense_frame)
    Category_entry.grid(row=2 , column=1)

    Description_label = tk.Label(add_expense_frame, text="Description:")
    Description_label.grid(row=3 , column=0)
    Description_entry = tk.Entry(add_expense_frame)
    Description_entry.grid(row=3 , column=1)

    add_expense_frame.pack(padx=20, pady=20)




root = tk.Tk()

root.title("Expense tracker")

root.geometry("1500x800")

# the feature buttons 

root.configure(bg="#F5D1D1")

header_frame = tk.Frame(root , bg="#2C3E50", bd=2 , relief="raised")
header_frame.pack(padx=10,pady=10,fill='x')

title_lable = tk.Label(header_frame , text="Expense Tracker" , font=("helvetica",20,"bold"),bg="#2C3E50",fg="white",)
title_lable.pack(padx=10 , pady=10)
title_lable2 = tk.Label(header_frame , text="by Salim khan",bg="#2C3E50",fg="white")
title_lable2.pack()

feature_frame = tk.Frame(root , bg="#2C3E50", bd=2 , relief="raised" )
feature_frame.pack(fill='x',padx=10,pady=10)

add_button = tk.Button(feature_frame, text="ADD➕" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white" , command=open_add_window )
add_button.pack(side="left"  , padx=10 , pady=10 )

Update_button = tk.Button(feature_frame, text="Update🖋️" , font=("helvetica",12,"bold" ) , bg="#90C0EF" , fg="white" )
Update_button.pack(side="left" , padx=10 , pady=10 )

delete_button = tk.Button(feature_frame, text="Delete🗑️" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white" )
delete_button.pack(side="left" , padx=10 , pady=10 )

refresh_button = tk.Button(feature_frame, text="Refresh🔄️" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white" , command=refresh_table )
refresh_button.pack(side="left" , padx=10 , pady=10 )

export_button = tk.Button(feature_frame, text="Export to Excel" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white")
export_button.pack(side="left" , padx=10 , pady=10 )

#creating button for dropdown
more_button = tk.Menubutton(feature_frame, text="More ⬇️" , font=("helvetica",12,"bold" ) , bg="#90C0EF" , fg="white" ,  )
more_button.pack(side="left" , padx=10 , pady=10 )
# creating the dropdown
dropdown = tk.Menu(more_button , tearoff=0)

more_button["menu"] = dropdown 

dropdown.add_command(label="Export")
dropdown.add_command(label="Show Total")
dropdown.add_command(label="Search")

content_frame = tk.Frame(root , bg="#2C3E50", bd=2 , relief="raised")
content_frame.pack(fill='both',expand=True , padx=10 , pady=10)

ttk.Treeview()

columns = ("ID", "Date", "Amount", "Category", "Description")

table = ttk.Treeview(
    content_frame,
    columns=columns,
    show="headings"
)

for column in columns:
    table.heading(column , text=column)

table.column("ID", width=60)
table.column("Date", width=120)
table.column("Amount", width=100)
table.column("Category", width=150)
table.column("Description", width=300)

table.pack(fill="both", expand=True , padx=10 , pady=10)

style = ttk.Style()

style.theme_use("clam") #  this is used to actual style in the tables

style.configure(
    "Treeview",
    font=("Helvetica", 11),
    rowheight=28,
    background="#2C3E50",
    foreground="white",
    # fieldbackground="#2C3E50",
    fieldbackground="#44607C",
)

style.configure(
    "Treeview.Heading",
    font=("Helvetica", 12, "bold")
)

# table.insert(
#     "",
#     "end",
#     values=(1, "2026-06-22", 250, "Food", "Lunch")
# )

# rows = logic.get_all_expenses()
# for row in rows:
#     table.insert("", "end", values=row)





root.mainloop()