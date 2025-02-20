#Consists of task id, tasks, Status of the task, Duedate in ASC order, Priority of task in DESC order.
import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("todo.db")
cursor = conn.cursor()

# Create table if it doesn't exist
cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    due_date TEXT,
    priority TEXT CHECK(priority IN ('Low', 'Medium', 'High')) DEFAULT 'Medium'
)
""")
conn.commit()

# Function to add a new task
def add_task(task, due_date, priority):
    cursor.execute("INSERT INTO tasks (task, due_date, priority) VALUES (?, ?, ?)", (task, due_date, priority))
    conn.commit()
    print("Task added successfully!")

# Function to view all tasks
def view_tasks():
    cursor.execute("SELECT * FROM tasks ORDER BY priority DESC, due_date ASC")
    tasks = cursor.fetchall()
    if not tasks:
        print("No tasks found!")
    else:
        for task in tasks:
            print(f"{task[0]}. {task[1]} - {task[2]} | Due: {task[3]} | Priority: {task[4]}")

# Function to update task status
def update_task(task_id, status):
    cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
    conn.commit()
    print("Task updated successfully!")

# Function to update task priority and due date
def update_task_details(task_id, due_date, priority):
    cursor.execute("UPDATE tasks SET due_date = ?, priority = ? WHERE id = ?", (due_date, priority, task_id))
    conn.commit()
    print("Task details updated successfully!")

# Function to delete a task
def delete_task(task_id):
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    print("Task deleted successfully!")

# CLI menu
def menu():
    while True:
        print("\nTo-Do List")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task Status")
        print("4. Update Task Details")
        print("5. Delete Task")
        print("6. Exit")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task = input("Enter task: ")
            due_date = input("Enter due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low/Medium/High): ").strip().title()
            add_task(task, due_date, priority)
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            task_id = int(input("Enter task ID: "))
            status = input("Enter new status (pending/done): ")
            update_task(task_id, status)
        elif choice == "4":
            task_id = int(input("Enter task ID: "))
            due_date = input("Enter new due date (YYYY-MM-DD): ")
            priority = input("Enter priority (Low/Medium/High): ").strip().title()

            update_task_details(task_id, due_date, priority)
        elif choice == "5":
            task_id = int(input("Enter task ID: "))
            delete_task(task_id)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

menu()

# Close connection when done
conn.close()

