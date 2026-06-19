import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Salimk@SQL28",      # Replace with your MySQL password

    database="expense_tracker"
)

cursor = conn.cursor()

print("Connected to MySQL successfully!")

def add_expenses():
        print ( "ADD your expenses"  )
        date = input("Enter date (YYYY-MM-DD): ")
        amount = float(input("Enter amount: "))
        category = input("Enter category: ")
        description = input("Enter description: ")

        query = """
        INSERT INTO expenses (expense_date, amount, category, description)
        VALUES (%s, %s, %s, %s)
        """

        values = (date, amount, category, description)

        print(values)
        cursor.execute(query, values)
        conn.commit()

        print("Expense added successfully!")


def view_expenses():
    print("View Expense Selected")

    cursor.execute("SELECT id,expense_date, amount, category, description FROM expenses")

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No expenses found.")
    else:
        print("\n--- All Expenses ---")

        for row in rows:
            print(f"id: {row[0]}")
            print(f"Date: {row[1]}")
            print(f"Amount: {row[2]}")
            print(f"Category: {row[3]}")
            print(f"Description: {row[4]}")
            print("--------------------")


def show_total_expense():
        print("Show Total Expense Selected")

        cursor.execute("SELECT SUM(amount) FROM expenses")

        result = cursor.fetchone()

        total = result[0]

        if total is None:
            total = 0
        
        print(result)

        print(f"Total Expense is {total}")


def delete_expenses():
    cursor.execute("""
        SELECT id, expense_date, amount, category, description
        FROM expenses
    """)

    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No expenses to delete.")
    else:
        print("\n--- Expenses ---")

        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Date: {row[1]}")
            print(f"Amount: {row[2]}")
            print(f"Category: {row[3]}")
            print(f"Description: {row[4]}")
            print("--------------------")

        delete_id = int(input("Enter the ID of the expense to delete: "))

        cursor.execute(
            "DELETE FROM expenses WHERE id = %s",
            (delete_id,)
        )
        conn.commit()

        print("Expense deleted successfully!")

def view_monthly_expenses():
    month = input( " enter the month ( yyyy - mm )")

    query = """ SELECT * FROM expenses 
    WHERE expense_date LIKE %s"""

    cursor.execute(query , (month + "%",))
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No expenses found for this month.")
    else:
        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Date: {row[1]}")
            print(f"Amount: {row[2]}")
            print(f"Category: {row[3]}")
            print(f"Description: {row[4]}")
            print("----------------------")


def update_expense():
    #first we need  expense_id
    expense_id  = int(input("enter expense id"))

    new_date = input("enter date yyyy-mm-dd")
    new_amount = float(input("enter the amount"))
    new_category = input("enter the category")
    new_description = input("enter the description")

    query = """
    UPDATE expenses
    SET expense_date = %s,
        amount = %s,
        category = %s,
        description = %s
    WHERE id = %s
    """

    values = {
         new_date , new_amount , new_category , new_description 
    }

    cursor.execute(query,values)

    cursor.commit()

    print(" expense updated successfully ")


def search_by_category():
     
    category = input("enter the category")

    query = """
    SELECT * FROM expenses 
    where category LIKE %s
    """

    cursor.execute(query , (category,))
    rows = cursor.fetchall()

    if len(rows) == 0:
        print("No expenses found in this category.")
    else:
        print("\n--- Matching Expenses ---")

        for row in rows:
            print(f"ID: {row[0]}")
            print(f"Date: {row[1]}")
            print(f"Amount: {row[2]}")
            print(f"Category: {row[3]}")
            print(f"Description: {row[4]}")
            print("------------------------")