# Task Queue Based on Priority in Python

This project demonstrates how to use a priority queue in Python to manage and execute tasks based on their priority. It ensures that higher priority tasks (with lower priority numbers) are completed first. Threading can optionally be used to process multiple tasks concurrently, but the main focus is task execution based on priority.

## Requirements

You can run this program either by using:
- An **online Python compiler**, or
- A local setup using **VSCode** or **NetBeans** with Python installed.

## Step-by-Step Guide

### 1. Using an Online Compiler

#### a. Using OnlineGDB

1. Go to [OnlineGDB Python Compiler](https://www.onlinegdb.com/online_python_compiler).
2. Select **Python** from the language dropdown.
3. Paste the code (provided below) into the editor.
4. Click **Run** to execute the code.

#### b. Using Replit, PythonAnywhere, JDoodle, or Programiz

1. Visit the respective website:
   - [Replit](https://replit.com/languages/python3)
   - [PythonAnywhere](https://www.pythonanywhere.com/try/)
   - [JDoodle](https://www.jdoodle.com/python3-programming-online/)
   - [Programiz](https://www.programiz.com/python-programming/online-compiler/)
2. Paste the code and run it.

### 2. Using VSCode (Visual Studio Code)

#### Requirements
- [Python 3.x](https://www.python.org/downloads/) must be installed on your system.
- Install **Visual Studio Code** from [here](https://code.visualstudio.com/Download).
- Install the **Python extension** for VSCode.

#### Steps

1. **Open VSCode**: Launch VSCode on your computer.
2. **Install the Python Extension**:
   - Click on the Extensions icon in the sidebar (or press `Ctrl + Shift + X`).
   - Search for **Python** and click **Install**.
3. **Create a New Folder**:
   - Open the command palette (`Ctrl + Shift + P`) and type **New Folder** to create a project folder.
4. **Open the Folder in VSCode**:
   - Navigate to the newly created folder, right-click on it, and select **Open with Code** (or open it from the VSCode interface).
5. **Create a Python File**:
   - Inside the folder, create a new file called `base_priority.py` (or any name you prefer) by clicking on **New File**.
6. **Paste the Code**:
   - Paste the following Python code into the file:
7. **Run the Code**:
   - Right-click inside the base_priority.py file and select Run Python File.
   - Alternatively, use the terminal (`Ctrl + ``) and type: python base_priority.py
8. **Expected Output: The tasks will be processed in priority order:**
```
Task Task 2 with priority 1 started.
Task Task 2 completed.
Task Task 1 with priority 2 started.
Task Task 1 completed.
Task Task 3 with priority 3 started.
Task Task 3 completed.
All tasks completed.

### 3. Using NetBeans with Python

#### Requirements
   -Install Python 3.x.
   -Install NetBeans.
   -Install the Python plugin for NetBeans (NetBeans may not have native Python support, so you'll need the plugin).

#### Steps
1. Open NetBeans: Launch NetBeans on your computer.
2. Install the Python Plugin:
   -Go to Tools > Plugins.
   -In the Available Plugins tab, search for Python and install it.
3. Create a New Python Project:
   -Go to File > New Project.
   -Select Python as the project type and click Next.
4. Add a Python File:
   -Right-click on the Source Files folder and select New > Python File.
   -Name it base_priority.py (or another name you prefer).
5. Paste the Code:
   -Paste the Python code provided earlier into this file.
   -Run the Project:
6. Right-click on the file in the Projects panel and select Run.
7. Expected Output: The program will run and display task execution in order of priority.

### How the Code Works
This Python program uses threading and queue to run tasks in order of priority. The tasks are added to a priority queue, and multiple threads ("workers") take tasks from the queue, execute them, and ensure that they are done in the correct order. The tasks with lower priority numbers are done first.

### Customizing the Program
You can change or add more tasks by adjusting this part of the code:
```python
priority_queue.put((2, 'Task 1'))  # Priority 2
priority_queue.put((1, 'Task 2'))  # Priority 1 (highest)
priority_queue.put((3, 'Task 3'))  # Priority 3 (lowest)

Feel free to experiment with different priority numbers or add more tasks!
