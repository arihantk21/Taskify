import streamlit as st

# Task class to represent individual tasks
class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

# TaskManager class to manage a collection of tasks
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        new_task = Task(task_name)
        self.tasks.append(new_task)

    def remove_task(self, task_name):
        self.tasks = [task for task in self.tasks if task.name != task_name]

    def get_tasks(self):
        return self.tasks

# Initialize TaskManager instance
if 'task_manager' not in st.session_state:
    st.session_state['task_manager'] = TaskManager()

# Function to add a new task
def add_task():
    with st.form(key='task_form', clear_on_submit=True):
        task_name = st.text_input("Enter a new task", key="new_task_input")
        submit_button = st.form_submit_button("Add Task")
        
        if submit_button:
            if task_name:
                st.session_state['task_manager'].add_task(task_name)
                st.success(f"Task '{task_name}' added.")
            else:
                st.error("Please enter a task.")

# Function to remove a task
def remove_task():
    if st.session_state['task_manager'].get_tasks():
        task_names = [task.name for task in st.session_state['task_manager'].get_tasks()]
        task_to_remove = st.selectbox("Select a task to remove", task_names, key="remove_task_select")
        
        if st.button("Remove Task"):
            st.session_state['task_manager'].remove_task(task_to_remove)
            st.success(f"Task '{task_to_remove}' removed.")

# Display the to-do list with checkboxes to mark tasks as completed
def display_tasks():
    st.header("To-Do List")
    for index, task in enumerate(st.session_state['task_manager'].get_tasks()):
        completed = st.checkbox(task.name, value=task.completed, key=f"task_{index}")
        task.completed = completed  # Update the task's completion status

# Streamlit App UI
st.title("To-Do List Manager")

# Section for adding tasks
st.subheader("Add a Task")
add_task()

# Section for removing tasks
st.subheader("Remove a Task")
remove_task()

# Section for displaying tasks
if st.session_state['task_manager'].get_tasks():
    display_tasks()
else:
    st.write("No tasks yet.")
