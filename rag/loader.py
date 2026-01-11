from langchain_community.document_loaders import PyPDFLoader

def load_pdf(file_path: str) -> str:
    loader = PyPDFLoader(file_path)
    docs = loader.load()
    return "\n".join([doc.page_content for doc in docs])


def load_text(text: str) -> str:
    return text
