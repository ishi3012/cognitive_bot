"""
Model Initialization file for embeddings and vector database.
"""

import os
import torch
from dotenv import load_dotenv
from transformers import AutoModelForCausalLM, AutoTokenizer
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import Pinecone
from pinecone import Pinecone, ServerlessSpec
from backend.config import config


# # oad environment variables from .env file
# load_dotenv()

# Load Hugging Face token
HUGGINGFACE_TOKEN = os.getenv("HUGGINGFACE_TOKEN")

# Load pre-trained embedding model
embedding_model = HuggingFaceEmbeddings(model_name=config.EMBEDDING_MODEL)

try:
    pc = Pinecone(api_key=config.PINECONE_API_KEY)

    if config.PINECONE_INDEX not in pc.list_indexes().names():
        print(f"Creating Pinecone index: {config.PINECONE_INDEX}...")
        pc.create_index(
            name=config.PINECONE_INDEX,
            dimension=1536,
            metric="euclidean",
            spec=ServerlessSpec(
                cloud="aws",
                region=config.PINECONE_ENV
            )
        )

    # Fix Pinecone vector store initialization
    vector_store = Pinecone(pc.Index(config.PINECONE_INDEX), embedding=embedding_model)
    print("Successfully connected to Pinecone index.")

except Exception as e:
    vector_store = None
    print(f"⚠ Warning: Failed to connect to Pinecone index - {e}")

# Configure LLM to generate response
MODEL_NAME = config.LLM_MODEL

print(f"Loading {MODEL_NAME} ...")
tokenizer = AutoTokenizer.from_pretrained(
    MODEL_NAME,
    token=HUGGINGFACE_TOKEN  # Use the Hugging Face token for authentication
)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    token=HUGGINGFACE_TOKEN,
    torch_dtype=torch.float16,
    device_map="auto"
)

# Fix function to generate response
def generate_llm_response(prompt: str) -> str:
    """
    Generates a response using the LLM model.
    """

    inputs = tokenizer(prompt, return_tensors="pt").to("cuda")
    output = model.generate(**inputs, max_length=500)
    response = tokenizer.decode(output[0], skip_special_tokens=True)

    return response
