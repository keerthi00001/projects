import streamlit as st 
import pandas as pd

from command_generator import generate_commands

print(generate_commands("create file test.txt"))

st.set_page_config(page_title="ILP Evaluator", layout="wide")

st.title("Linux Screenshot Evaluation System")

role = st.sidebar.selectbox(
    "Select Role",
    ["Faculty","Student"]
)

#Faculty Dashboard

if role == "Faculty":
    st.header("Faculty Dashboard")

    question = st.text_area("Enter Linux Question")

    if st.button("Generate Commands"):
        commands = generate_commands(question)

        st.sucess("Detected Commands")

        st.write(commands)

#Student Dashboard
if role == "Student":
    st.header("Student Dashboard")

    st.write("Student functionallity will come here")