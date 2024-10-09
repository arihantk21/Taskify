import streamlit as st
import sqlite3

# Database functions
def create_connection():
    conn = sqlite3.connect('todo_list.db')
    return conn

def add_task_to_db(task_name):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (name) VALUES (?)', (task_name,))
    conn.commit()
    conn.close()

def remove_task_from_db(task_id):
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

def get_tasks_from_db():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Streamlit App UI
st.title("To-Do List Manager")

# Section for adding tasks
st.subheader("Add a Task")
with st.form(key='task_form', clear_on_submit=True):
    task_name = st.text_input("Enter a new task", key="new_task_input")
    submit_button = st.form_submit_button("Add Task")
    
    if submit_button:
        if task_name:
            add_task_to_db(task_name)
            st.success(f"Task '{task_name}' added.")
        else:
            st.error("Please enter a task.")

# Section for removing tasks
st.subheader("Remove a Task")
tasks = get_tasks_from_db()
if tasks:
    task_names = [f"{task[0]}: {task[1]}" for task in tasks]  # Display task ID and name
    task_to_remove = st.selectbox("Select a task to remove", task_names, key="remove_task_select")
    
    if st.button("Remove Task"):
        task_id = int(task_to_remove.split(":")[0])  # Extract ID from selected task
        remove_task_from_db(task_id)
        st.success(f"Task '{task_to_remove}' removed.")

# Section for displaying tasks
if tasks:
    st.header("To-Do List")
    for task in tasks:
        completed = st.checkbox(task[1], value=bool(task[2]), key=f"task_{task[0]}")
        # Update completion status in the database if checked/unchecked (optional)
else:
    st.write("No tasks yet.")
