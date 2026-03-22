import streamlit as st
from openai import OpenAI

client = OpenAI(api_key="YOUR_API_KEY")

st.title("AI Project Idea Generator")

st.write("Generate Hackathon / Research / Patent Ideas")

mode = st.selectbox(
    "Select Mode",
    ["Hackathon", "Research Paper", "Patent", "Startup"]
)

topic = st.text_input("Enter Topic")

if st.button("Generate Idea"):

    prompt = f"""
    Generate an innovative {mode} idea on topic: {topic}

    Give output in format:

    Problem Statement
    Proposed Solution
    Tech Stack
    Step by Step Implementation
    Future Scope
    """

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    result = response.choices[0].message.content

    st.write(result)
