import streamlit as st

# title
st.title("Python Data Structures")

# creating list
st.header("We are creating a list")
fruits = ["apple", "banana", "cherry"]
st.write("Original list:", fruits)

# adding an element to the list
new_fruit = st.text_input("Add a new fruit to the list:")
if st.button("Add Fruit"):
    if new_fruit:
        fruits.append(new_fruit)
        st.write("Updated list:", fruits)