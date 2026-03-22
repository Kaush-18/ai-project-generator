import streamlit as st

st.title("AI Project Idea Generator")

topic = st.text_input("Enter project topic")

if st.button("Generate Idea"):
    st.write("Generating idea for:", topic)
