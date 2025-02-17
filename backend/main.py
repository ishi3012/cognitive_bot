"""
Initializes the FastAPI server, registers routes, and starts the application.
"""

import os
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.api.knowledge import router as knowledge_router
from backend.api.code import router as code_router
from backend.api.query_router import router as query_router
from backend.config import config


# Load CORS configurations with a fallback
ALLOWED_ORIGINS = config.ALLOWED_ORIGINS.split(",")

# Initialize FastAPI app
app = FastAPI(title="Cognitive Bot API", version="1.0")

# Configure CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routes (Fixing incorrect `tags` format)
app.include_router(knowledge_router, prefix="/knowledge", tags=["Knowledge Retrieval"])
app.include_router(code_router, prefix="/code", tags=["Code Assistant"])
app.include_router(query_router, prefix="/query", tags=["Query Routing"])

# API Endpoints

@app.get("/")
async def home():
    """
    Health check endpoint to verify if the API is running.
    """
    return {"message": "Welcome to the Cognitive Bot API"}

# Start Uvicorn Server (For local development)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
