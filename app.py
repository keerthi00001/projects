import streamlit as st
import json
import os
from command_generator import generate_commands

st.set_page_config(page_title="ILP Evaluator", layout="wide")

st.title("Linux Screenshot Evaluation System")

# ---------------- File Configuration ----------------
DATA_FOLDER = "data"
DATA_FILE = os.path.join(DATA_FOLDER, "questions.json")

os.makedirs(DATA_FOLDER, exist_ok=True)

# Ensure file exists
if not os.path.exists(DATA_FILE):
    with open(DATA_FILE, "w") as f:
        json.dump([], f)

st.write("Using JSON File:", os.path.abspath(DATA_FILE))

# ---------------- Sidebar ----------------
role = st.sidebar.selectbox(
    "Select Role",
    ["Faculty", "Student"]
)

# =====================================================
# FACULTY
# =====================================================
if role == "Faculty":
    st.header("Faculty Dashboard")

    question = st.text_area("Enter Linux Question")
    commands = []

    if question.strip():
        try:
            commands = generate_commands(question)
            st.subheader("Detected Commands")
            st.write(commands)
        except Exception as e:
            st.error(f"Error generating commands: {e}")

    if st.button("Save Question"):
        if not question.strip():
            st.warning("Please enter a question.")
        else:
            try:
                # Load existing questions
                with open(DATA_FILE, "r") as f:
                    questions = json.load(f)

                # New question entry
                question_data = {
                    "question": question,
                    "commands": commands,
                    "marks": 5
                }

                questions.append(question_data)

                # Save back
                with open(DATA_FILE, "w") as f:
                    json.dump(questions, f, indent=4)

                st.success("Question saved successfully!")

                # Always show updated JSON
                with open(DATA_FILE, "r") as f:
                    updated = json.load(f)

                st.subheader("Updated Questions JSON")
                st.json(updated)

            except Exception as e:
                st.error(f"Error saving question: {e}")

# =====================================================
# STUDENT
# =====================================================
elif role == "Student":
    st.header("Student Dashboard")

    try:
        with open(DATA_FILE, "r") as f:
            questions = json.load(f)

        if len(questions) == 0:
            st.warning("No questions available.")
        else:
            selected_question = st.selectbox(
                "Select Question",
                [q["question"] for q in questions]
            )

            selected = next(
                q for q in questions
                if q["question"] == selected_question
            )

            st.subheader("Question")
            st.write(selected["question"])

            st.subheader("Commands")
            st.write(selected["commands"])

            st.subheader("Marks")
            st.write(selected["marks"])

    except Exception as e:
        st.error(f"Error loading questions: {e}")
