
from langchain.tools import tool

@tool
def search_tool(query: str) -> str:
    return f"Search result for '{query}'"

@tool
def reminder_tool(task: str) -> str:
    return f"Reminder set for: {task}"
