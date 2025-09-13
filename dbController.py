# main.py
import os
from langchain_community.utilities import SQLDatabase
from langchain.agents import initialize_agent
from langchain.agents.agent_types import AgentType
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain_groq import ChatGroq
from db import DB_PATH, initialize_database

## Uncomment the following files if you're not using pipenv as your virtual environment manager
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# Initialize the DB if it doesn't exist
initialize_database()

# Load model
llm = ChatGroq(model_name="llama3-8b-8192", temperature=0)

# Connect to SQLite
db = SQLDatabase.from_uri(f"sqlite:///{DB_PATH}")
toolkit = SQLDatabaseToolkit(db=db, llm=llm)

# Initialize agent
agent_executor = initialize_agent(
    tools=toolkit.get_tools(),
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=False
)

def run_query(prompt: str) -> str:
    try:
        result =  agent_executor.invoke({"input": prompt})
        return result["output"]
        #return agent_executor.run(prompt)
    except Exception as e:
        return f"Error: {str(e)}"