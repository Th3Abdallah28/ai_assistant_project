
🤖 AI Personal Assistant (Multi-Agent System)

This is a simple AI-powered personal assistant built using *Python*, *LangChain*, *OpenAI*, and *Streamlit*. It uses a multi-agent approach where each agent has a specialized task (e.g. search, reminders).

---

🚀 Features

- Multi-agent support (easily extendable)
- Search simulation agent
- Reminder-setting agent
- Streamlit user interface
- OpenAI-powered language logic

---

📂 Project Structure


ai_assistant_project/
├── app.py              # Streamlit UI
├── assistant.py        # Agent logic
├── tools.py            # Tool functions (agents)
├── requirements.txt    # Dependencies
└── README.md           # Project documentation


---

⚙️ Installation

bash
git clone https://github.com/your-username/ai_assistant_project.git
cd ai_assistant_project
pip install -r requirements.txt


---

🔑 Setup

You must set your *OpenAI API Key* as an environment variable:

bash
export OPENAI_API_KEY="your-key-here"


---

▶️ Run the Assistant

bash
streamlit run app.py
```
