import streamlit as st

# Initialize the session state to store tasks and completion status
if 'tasks' not in st.session_state:
    st.session_state['tasks'] = []  # List to store task names
    st.session_state['completed'] = []  # List to store completion status (True/False)

# Function to add a new task
def add_task():
    task_name = st.text_input("Enter a new task", key="new_task_input")
    if st.button("Add Task"):
        if task_name:
            st.session_state['tasks'].append(task_name)  # Add the task to the list
            st.session_state['completed'].append(False)  # Set completion status to False
            st.success(f"Task '{task_name}' added.")
        else:
            st.error("Please enter a task.")

# Function to remove a task
def remove_task():
    task_to_remove = st.selectbox("Select a task to remove", st.session_state['tasks'], key="remove_task_select")
    if st.button("Remove Task"):
        if task_to_remove:
            index = st.session_state['tasks'].index(task_to_remove)  # Get the index of the task
            del st.session_state['tasks'][index]  # Remove the task
            del st.session_state['completed'][index]  # Remove the corresponding completion status
            st.success(f"Task '{task_to_remove}' removed.")

# Display the to-do list with checkboxes to mark tasks as completed
def display_tasks():
    st.header("To-Do List")
    for index, task in enumerate(st.session_state['tasks']):
        completed = st.checkbox(task, value=st.session_state['completed'][index], key=f"task_{index}")
        st.session_state['completed'][index] = completed  # Update the task's completion status

# Streamlit App UI
st.title("To-Do List Manager")

# Section for adding tasks
st.subheader("Add a Task")
add_task()

# Section for removing tasks
st.subheader("Remove a Task")
if st.session_state['tasks']:  # Only show remove option if there are tasks
    remove_task()

# Section for displaying tasks
if st.session_state['tasks']:
    display_tasks()
else:
    st.write("No tasks yet.")
