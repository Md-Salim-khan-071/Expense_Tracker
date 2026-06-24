import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import mysql.connector
# from logic import *
import logic
from datetime import datetime  # for date format validation

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

    Date_label = tk.Label(add_expense_frame, text="Date(yyyy-mm-dd):" )
    Date_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    Date_entry = tk.Entry(add_expense_frame)
    Date_entry.grid(row=0 , column=1)

    Amount_label = tk.Label(add_expense_frame, text="Amount:")
    Amount_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Amount_entry = tk.Entry(add_expense_frame)
    Amount_entry.grid(row=1 , column=1)

    Category_label = tk.Label(add_expense_frame, text="Category:")
    Category_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Category_entry = tk.Entry(add_expense_frame)
    Category_entry.grid(row=2 , column=1)

    Description_label = tk.Label(add_expense_frame, text="Description:")
    Description_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Description_entry = tk.Entry(add_expense_frame)
    Description_entry.grid(row=3 , column=1)

    add_expense_frame.pack(padx=20, pady=20)

    #function to save the expenses 
    def save_expenses():
        date = Date_entry.get()
        amount = Amount_entry.get()
        category = Category_entry.get()
        description = Description_entry.get()

        if not date or not amount or not category:
        # Show an error message and don't save
            messagebox.showerror("Error","please fill all the records"
        )
            
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Invalid Date",
                "Please enter the date in YYYY-MM-DD format."
            )
            return    # this part is to check for date format , as mysql will only take date in (yyyy-mm-dd) format . and also this part should be before the sql querying 

        logic.add_expense_gui(
        date,
        amount,
        category,
        description
        )

        refresh_table()

        add_window.destroy()

    save_button = tk.Button(
        add_window,
        text="Save Expense",
        command=save_expenses
    )

    save_button.pack( pady=10)


# function for deleting an expense 
def delete_selected_expense():
    selected_item = table.selection()

    if not selected_item: #checks if user has selected an item . if any user didnt select an item and pressed delete an error should pop
        messagebox.showerror(
            "No Selection",
            "Select a row before deleting"
        )
    
    values = table.item(selected_item[0] , "values")  # selected_item[0] bcoz selected_item actually returns a tuple ("ex",)  but we want only "ex" . so we use selected_item[0] .
    expense_id = values[0]
    
    #ask for confirmation to delete
    confirm = messagebox.askyesno(
        "Confirm delete",
        "Are you sure! you want to  delete this  expense "
    )
    if not confirm:
        return

    logic.delete_expense_gui(expense_id)

    refresh_table()


# function for the update button
def update_selected_item():
    selected_item  = table.selection()
    
    if not selected_item:
        messagebox.showerror("ERROR!!","select a row to Update")
        return
    
    values = table.item(selected_item[0],"values")

    #now we have selected the values . but to update them we need to store them in variables
    expense_id = values[0]
    date = values[1]
    amount = values[2]
    category = values[3]
    description = values[4]

    update_window = tk.Toplevel(root)
    update_window.title("update the values")
    
    # NOW after creating the window , we do exactly as the add window , but we also  show the existing values .
    
    update_expense_frame = tk.Frame(update_window)
    update_expense_frame.columnconfigure(0 , weight=1)
    update_expense_frame.columnconfigure(1 , weight=1)

    ID_label = tk.Label(update_expense_frame, text="Expense ID:" )
    ID_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
    ID_entry = tk.Entry(update_expense_frame)
    ID_entry.grid(row=0 , column=1)
    ID_entry.insert(0,expense_id)
    ID_entry.config(state="readonly") # id should not be changed

    Date_label = tk.Label(update_expense_frame, text="Date(yyyy-mm-dd):" )
    Date_label.grid(row=1, column=0, padx=10, pady=5, sticky="w")
    Date_entry = tk.Entry(update_expense_frame)
    Date_entry.grid(row=1 , column=1)
    Date_entry.insert(1,date)   # this line is what changes this  from ADD window  , as this gives already existing values

    Amount_label = tk.Label(update_expense_frame, text="Amount:")
    Amount_label.grid(row=2, column=0, padx=10, pady=5, sticky="w")
    Amount_entry = tk.Entry(update_expense_frame)
    Amount_entry.grid(row=2 , column=1)
    Amount_entry.insert(2,amount)
    
    Category_label = tk.Label(update_expense_frame, text="Category:")
    Category_label.grid(row=3, column=0, padx=10, pady=5, sticky="w")
    Category_entry = tk.Entry(update_expense_frame)
    Category_entry.grid(row=3 , column=1)
    Category_entry.insert(3,category)

    Description_label = tk.Label(update_expense_frame, text="Description:")
    Description_label.grid(row=4, column=0, padx=10, pady=5, sticky="w")
    Description_entry = tk.Entry(update_expense_frame)
    Description_entry.grid(row=4 , column=1)
    Description_entry.insert(4,description)

    update_expense_frame.pack(padx=20, pady=20)

    def save_expenses():
        expense_id = ID_entry.get()
        date = Date_entry.get()
        amount = Amount_entry.get()
        category = Category_entry.get()
        description = Description_entry.get()

        if not date or not amount or not category or not description:
        # Show an error message and don't save
            messagebox.showerror("Error","please fill all the records")
            return
            
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror(
                "Invalid Date",
                "Please enter the date in YYYY-MM-DD format."
            )
            return

        logic.update_expense_gui(
        expense_id,
        date,
        amount,
        category,
        description
        )

        

        refresh_table()

        update_window.destroy()

    save_button = tk.Button(
        update_window,
        text="Save Expense",
        command=save_expenses
    )

    save_button.pack( pady=10)



    

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

Update_button = tk.Button(feature_frame, text="Update🖋️" , font=("helvetica",12,"bold" ) , bg="#90C0EF" , fg="white" , command=update_selected_item )
Update_button.pack(side="left" , padx=10 , pady=10 )

delete_button = tk.Button(feature_frame, text="Delete🗑️" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white" , command=delete_selected_expense )
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




root.mainloop()