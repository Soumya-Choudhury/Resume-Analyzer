import os
from langchain_openai import ChatOpenAI

def get_llm():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not set")

    llm = ChatOpenAI(
        model="gpt-4o-mini",
        temperature=0.2,
        api_key=api_key
    )
    return llm
