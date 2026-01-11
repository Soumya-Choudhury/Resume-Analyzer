from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import Ollama
from rag import get_llm
def create_rag_chain(vector_db):
    retriever = vector_db.as_retriever()

    llm = get_llm()

    prompt = ChatPromptTemplate.from_template("""
You are an expert resume analyzer.

Context:
{context}

Question:
{question}

Answer:
""")

    chain = (
        {
            "context": retriever,
            "question": RunnablePassthrough()
        }
        | prompt
        | llm
    )

    return chain
