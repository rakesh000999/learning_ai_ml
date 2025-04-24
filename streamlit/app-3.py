import streamlit as st
import matplotlib.pyplot as plt

# title
st.title("Data Visualization with Matplotlib")

# Dictionary
data = {
    "Apple": 10,
    "Banana": 20,
    "Cherry": 15,
    "Date": 5,
    "Elderberry": 8
}

# Display the dictionary
st.write("Inventory:", data)

# Update dictionary
key = st.text_input("Enter a key", "")
value = st.text_input("Enter a value", "")

if st.button("Update Dictionary"):
    if key and value:
        data[key] = int(value)
        st.write("Updated Dictionary:", data)

# Plotting a bar chart

st.header("Bar Chart of Inventory")
fig, ax = plt.subplots()
ax.bar(data.keys(), data.values())
ax.set_xlabel("Fruits")
ax.set_ylabel("Quantity")
st.pyplot(fig)
