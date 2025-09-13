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