import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

# Read a task from file
def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()

# Make a call to Gemini with prompt to categorize the task
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

if __name__ == "__main__":
    task_text = read_tasks("tasks_text.txt")
    summary = summarize_tasks(task_text)
    print("\n Task Summary")
    print("-" * 30)
    print(summary)
