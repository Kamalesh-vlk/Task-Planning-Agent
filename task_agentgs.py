# streamlit_task_agent.py
import os
import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def summarize_tasks(tasks):
    prompt = f"""You are a Task Planning Agent.
    Given a list of tasks, categorize them into 3 priority buckets:
    - High Priority
    - Medium Priority
    - Low Priority

    Tasks:{tasks}

    Return the response in this form:
    
    High Priority:
    - task 1
    - task 2

    Medium Priority:
    - task 1
    - task 2

    Low Priority:
    - task 1
    - task 2
    """

    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI Setup
st.set_page_config(page_title="🗂 Task Planning Agent", page_icon="✅", layout="wide")
st.title("🗂 Task Planning Agent")
st.write("Upload your list of tasks and categorize them by priority using **Google Gemini**.")

# Create two columns
col1, col2 = st.columns(2)

with col1:
    st.subheader("📤 Upload Tasks")
    uploaded_file = st.file_uploader("Upload tasks_text.txt", type=["txt"])
    tasks_text = ""
    if uploaded_file is not None:
        tasks_text = uploaded_file.read().decode("utf-8")
        st.text_area("📋 Uploaded Tasks", tasks_text, height=400)

with col2:
    st.subheader("✅ Categorized Tasks")
    if tasks_text:
        if st.button("Categorize Tasks"):
            with st.spinner("Analyzing tasks..."):
                summary = summarize_tasks(tasks_text)
            st.text_area("📌 Task Summary", summary, height=400)
    else:
        st.info("Please upload a tasks file from the left panel.")
