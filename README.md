# 📝 Task-Planning-Agent

This project is an **AI-powered task prioritization assistant** built with **Google Gemini**.  
It reads a list of tasks from a file and categorizes them into **High**, **Medium**, and **Low** priority buckets.

---

## 🚀 Features

- **Google Gemini Integration** – Uses `gemini-1.5-flash` for fast categorization.
- **Automatic Task Prioritization** – No manual sorting needed.
- **Customizable Prompt** – Easily change categorization rules in the code.
- **Simple CLI Tool** – Just run and see the results.

---

## 🔑 API Key Setup

This project requires a **Google Gemini API Key** to work.

1. Create a `.env` file in the project root.
2. Add your API key:

```env
GEMINI_API_KEY=your_gemini_api_key_here
```
---
## 📂 Input File
- The Project reads the tasks from **tasks_text.txt**.
---
## ▶️ How It Works

- The script loads your tasks from tasks_text.txt.
- The Project reads the content from 'tasks_text.txt'

- Sends them to Google Gemini with a prompt asking for categorization.

- Prints the results in a priority-based format.
## 🚀 Usage
To run the Task Categorization Agent with a Streamlit UI:
```
streamlit run task_agentgs.py
```
## 📄 Sample Output

 Task Summary
------------------------------
High Priority:

- Fix login bug
- Investigate and resolve payment gateway timeout issue
- Update SSL certificates for production server        
- Reply to customer support
- Respond to pending customer feedback emails


Medium Priority:

- Backup the database
- Draft and send weekly progress report to stakeholders
- Update HomePage UI
- Redesign the pricing page layout
- Post Instagram Update for product launch
- Create LinkedIn post announcing new feature rollout
- Prepare monthly sales performance presentation
- Debug and fix API response time issue
- Follow up with vendor about delayed shipment


Low Priority:

- Write a montly newsletter
- Clean up unused AWS Buckets
- Research competitor pricing
- Schedule a team standup
- Discuss the queries with the team
- Archive old project files from shared drive
- Analyze website traffic trends from last quarter
- Organize a brainstorming session for Q4 goals
- Review and approve pull requests in GitHub
- Update product FAQ section on the website
- Remove outdated entries from CRM database
- Design promotional banner for upcoming event
- Run full security audit on staging environment
- Collect customer testimonials for case studies
- Schedule quarterly performance reviews
- Draft blog post about industry trends

