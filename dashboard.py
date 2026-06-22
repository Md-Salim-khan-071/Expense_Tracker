import tkinter as tk
from tkinter import ttk
# from logic import *

root = tk.Tk()

root.title("Expense tracker")

root.geometry("1000x600")

root.configure(bg="#F5D1D1")

header_frame = tk.Frame(root , bg="#2C3E50", bd=2 , relief="raised")
header_frame.pack(padx=10,pady=10,fill='x')

title_lable = tk.Label(header_frame , text="Expense Tracker" , font=("helvetica",20,"bold"),bg="#2C3E50",fg="white",)
title_lable.pack(padx=10 , pady=10)
title_lable2 = tk.Label(header_frame , text="by Salim khan",bg="#2C3E50",fg="white")
title_lable2.pack()

feature_frame = tk.Frame(root , bg="#2C3E50", bd=2 , relief="raised" )
feature_frame.pack(fill='x',padx=10)

add_button = tk.Button(feature_frame, text="ADD➕" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white")
add_button.pack(side="left"  , padx=10 , pady=10 )

Update_button = tk.Button(feature_frame, text="Update🖋️" , font=("helvetica",12,"bold" ) , bg="#90C0EF" , fg="white" )
Update_button.pack(side="left" , padx=10 , pady=10 )

delete_button = tk.Button(feature_frame, text="Delete🗑️" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white" )
delete_button.pack(side="left" , padx=10 , pady=10 )

refresh_button = tk.Button(feature_frame, text="Refresh🔄️" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white" )
refresh_button.pack(side="left" , padx=10 , pady=10 )

export_button = tk.Button(feature_frame, text="Export to Excel" , font=("helvetica",12,"bold") , bg="#90C0EF" , fg="white")
export_button.pack(side="left" , padx=10 , pady=10 )


content_frame = tk.Frame(root)
content_frame.pack(fill='both',expand=True)

root.mainloop()