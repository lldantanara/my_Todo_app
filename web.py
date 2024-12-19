import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
   todo = st.session_state["new_todo"]+"\n"
   todos.append(todo)
   functions.write_todos(todos)


st.title("My Todo App")
st.subheader("This is my Todo app")
st.write("This app is to increase your productivity.")

#i=0
for index,todo in enumerate(todos):
   # i=i+1
    checkbox=st.checkbox(todo,key=todo)
    if checkbox:
       todos.pop(index)
       functions.write_todos(todos)
       del st.session_state[todo]
       st.rerun()
st.text_input(label=" ",placeholder="Add new todo... ",
              on_change=add_todo,key="new_todo")

#print("Hello")

#st.session_state

