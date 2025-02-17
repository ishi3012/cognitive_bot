import os
from langchain.text_splitter import RecursiveCharacterTextSplitter

class DocumentLoader:
    """
        Loads and preprocesses knowledge documents by splitting them into chunks.
    """
    def __init__(self, chunk_size=500, chunk_overlap=50):
        """
            Initialize the DocumentLoader class with chunk size and overlap settings.
        """
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap
        self.text_splitter = RecursiveCharacterTextSplitter(chunk_size=self.chunk_size, chunk_overlap=self.chunk_overlap)
    
    def load_and_split_documents(self, file_path:str):
        """
            Loads a text document and splits it into smaller chunks.
        """

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File {file_path} not found!")
        
        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
        
        chunks = self.text_splitter.split_text(text)

        return chunks
