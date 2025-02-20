# Python-Project To-Do List Application (Python + SQLite)
1. Introduction:The To-Do List Application is a command-line interface (CLI) tool built using Python and SQLite. It allows users to efficiently manage their tasks by providing essential CRUD (Create, Read, Update, Delete) functionalities. The application aims to enhance productivity by organizing tasks with due dates and priority levels.
2. Features 
✅ Add tasks with descriptions, due dates, and priority levels (Low, Medium, High)
✅ View all tasks in a sorted order (by due date and priority) 
✅ Update task status (mark as complete or modify details) 
✅ Delete tasks that are no longer needed 
✅ Persistent storage using SQLite for data management Developed using Visual Studio for an enhanced development experience
3. Enhancements and Modifications To improve usability and efficiency, the following modifications have been implemented:
 1.	Database Schema Update: The schema now includes due date and priority fields.
 2.	Enhanced Task Addition: Users can specify due dates and set priority levels when adding a task.
 3.	Sorting Mechanism: Tasks are displayed in an organized manner, sorted by due date and priority.
 4.	User-friendly Interaction: Clear prompts and structured output make the CLI intuitive.
 5.	Software Development: Implemented using Visual Studio for better code management and debugging.
4. Technical Implementation
 •	Programming Language: Python
 •	Database: SQLite
 •	Libraries Used: 
  o	sqlite3 for database operations
  o	datetime for handling due dates
  o	tabulate (optional) for better task display in tabular format
 •	Development Environment: Visual Studio
5. Database Schema
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    status TEXT DEFAULT 'pending',
    due_date TEXT,
    priority TEXT CHECK (priority IN ('Low', 'Medium', 'High')) DEFAULT 'Medium'
);
6. Functional Breakdown
•	add_task (task, due_date, priority): Inserts a new task into the database.
•	view_tasks(): Retrieves and displays tasks sorted by due date and priority.
•	update_task (task_id, status): To update task status.
•	update_task (task_id, due_date, priority): To update task priority and due date.
•	delete_task(task_id): Removes a task from the database.
7. Conclusion The To-Do List Application effectively helps users manage their tasks by incorporating due dates and priority levels. The use of SQLite ensures persistent data storage, while Python provides a flexible and robust backend. The development process was enhanced using Visual Studio, offering better debugging and code management. With planned future enhancements, this tool can be extended into a more comprehensive task management solution.
