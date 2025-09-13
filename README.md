
Project Abstarcat:

1. Title 
Design and Implementation of a Conversational AI System with Agentic Workflows for 
Intelligent Help Document Navigation and Task Automation in Enterprise Applications
 
3. Detailed Description 
In large-scale enterprise applications, users often face challenges in navigating dense help 
documentation to resolve feature-related queries or accomplish tasks. This project aims to 
streamline that process by developing a Conversational AI System that transforms static 
product help documents into an interactive, intelligent chatbot. The proposed system 
enables users to query about product features and receive accurate, context-aware 
answers in natural language, eliminating the need to manually browse through 
documentation. 
 
The chatbot will be powered by state-of-the-art LLMs (Large Language Models) 
enhanced with Retrieval-Augmented Generation (RAG) for accurate and dynamic 
response generation based on up-to-date help documents. In addition to this, the solution 
will integrate an agentic workflow system, which empowers the chatbot to not only 
provide information but also autonomously perform backend actions - such as creating 
events, generating reports, sending notifications, and triggering predefined workflows. 
 
The current process of product support relies heavily on manual intervention, resulting in 
time-consuming resolutions and inconsistent user experiences. This project proposes an 
efficient alternative by offering a natural language interface to both search and act, thus 
significantly improving user satisfaction and operational efficiency. 
• Document preprocessing and vectorization for knowledge ingestion. 
• RAG-based response generation pipeline. 
• LangChain/Groq API or similar framework integration for intent recognition and 
agentic flow. 
• Task automation through programmable workflows (example, API integration for 
event/report actions). 
• Streamlit-based front-end interface for demo and testing. 
 
This dissertation project is designed for a 16-week duration, including stages for 
literature survey, system architecture design, development, integration, testing, and 
documentation. The final deliverable will be a fully working prototype capable of end-to
end conversational support and automated task execution.

NOTE: 

activate venv: 
.\venv\Scripts\activate 

deactivate venv:
deactivate

extract requirement.txt:
pip freeze > requirements2.txt


python .\create_memory_for_llm.py    

run app: 

streamlit run .\app.py 
