
from langchain.agents import initialize_agent, Tool
from langchain.llms import OpenAI
from tools import search_tool, reminder_tool

llm = OpenAI(temperature=0)
tools = [search_tool, reminder_tool]

agent = initialize_agent(tools, llm, agent="zero-shot-react-description")

def run_query(query):
    return agent.run(query)

