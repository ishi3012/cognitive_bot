"""
Configuration file for storing environment variables and API keys.
"""

import os
from dotenv import load_dotenv


# Load environment variables from .env file
load_dotenv()

class Config:
    """
    Config class to hold all the environment 
    """

    # OpenAI api key for LLM operations
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    if not OPENAI_API_KEY:
        raise ValueError("Missing OPENAI_API_KEY! Set it in the environment.")
    
    # LLM Model 
    LLM_MODEL="mistralai/Mistral-7B-Instruct-v0.3"
    HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")
    
    # Pinecone API Key and Index for vector database
    PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
    PINECONE_ENV=os.getenv("PINECONE_ENV")
    if not PINECONE_API_KEY:
        raise ValueError("Missing PINECONE_API_KEY! Set it in the environment.")
    
    PINECONE_INDEX = os.getenv("PINECONE_INDEX")

    # Hugging Face model for embeddings
    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "sentence-transformers/all-MiniLM-L6-v2")

    # CORS Allowed Origins
    ALLOWED_ORIGINS = os.getenv("ALLOWED_ORIGINS", "*").split(",")

# create a config object

config = Config()
