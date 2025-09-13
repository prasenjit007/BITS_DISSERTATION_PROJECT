import os
import streamlit as st
import traceback
from langchain.chains import RetrievalQA

from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_community.llms import Ollama
from dotenv import load_dotenv, find_dotenv
from langsmith import traceable  

load_dotenv(find_dotenv())

DB_FAISS_PATH="vectorstore/db_faiss"
traceable(name="load vectorstore")
@st.cache_resource
def get_vectorstore():
    embedding_model=HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db=FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db

traceable(name="set custom prompt")
def set_custom_prompt(custom_prompt_template):
    prompt=PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

traceable(name="load llm")
def load_llm():
    return Ollama(model="mistral", temperature=0.5)

traceable(name="ask bot")
def askBot(intent, text):
    prompt=text

    if prompt:

        CUSTOM_PROMPT_TEMPLATE = """
                Use the pieces of information provided in the context to answer user's question.
                If you dont know the answer, just say that you dont know, dont try to make up an answer. 
                Dont provide anything out of the given context

                Context: {context}
                Question: {question}

                Start the answer directly. No small talk please.
                """
        
        HF_TOKEN=os.environ.get("HF_TOKEN")

        try: 
            vectorstore=get_vectorstore()
            if vectorstore is None:
                st.error("Failed to load the vector store")

            qa_chain = RetrievalQA.from_chain_type(
                llm=load_llm(),
                chain_type="stuff",
                retriever=vectorstore.as_retriever(search_kwargs={'k': 3}),
                return_source_documents=True,
                chain_type_kwargs={'prompt': set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)}
            )

            response=qa_chain.invoke({'query':prompt})

            result=response["result"]
            #source_documents=response["source_documents"]
            #result_to_show=result
            #+"\nSource Docs:\n"+str(source_documents) #commented source document
            #response="Hi, I am MediBot!"
            
            return result

        except Exception as e:
            st.error(f"Error: {str(e)}")
            #st.text(traceback.format_exc())  # Show full traceback
