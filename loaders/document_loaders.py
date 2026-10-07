from langchain_community.document_loaders import (
    PyPDFLoader,
    TextLoader,
    Docx2txtLoader,
    CSVLoader,
    YoutubeLoader
)


def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

def load_txt(file_path):
    loader = TextLoader(file_path)
    return loader.load()

def load_docx(file_path):
    loader = Docx2txtLoader(file_path)
    return loader.load()

def load_csv(file_path):
    loader = CSVLoader(file_path)
    return loader.load()

def load_youtube(url):
    loader = YoutubeLoader.from_youtube_url(
        url
    )
    return loader.load()

