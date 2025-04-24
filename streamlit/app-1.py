import streamlit as st

# title
st.title("My first app")

# display text
st.write("Hello world!")

# Add Button
st.button("Click me!")

if st.button("Perform Action"):
    st.write("Button clicked!")
