"""
Handles Retrieval API for handling user queries and retrieving relevant AI information.

"""
from fastapi import APIRouter, HTTPException
from backend.models import vector_store, embedding_model, generate_llm_response
from backend.utils.helpers import format_response, log_message

router = APIRouter()

@router.get("/search/")
async def search_knowledge(query: str):
    """
    Searches the knowledge base and generates an LLM-enhanced response.
    """
    try:
        log_message(f"Searching knowledge base for query:  {query}", "info")

        # Convert query to embedding
        query_embedding = embedding_model.embed_query(query)

        # Search Pinecone index for similar documents
        results = vector_store.similarity_search(query_embedding, k=5)
        
        if not results:
            raise HTTPException(status_code=404, detail="No relevalant information found.")

        retrieved_text = " ".join([doc.page_content for doc in results])
        llm_prompt = f"Based on the following retrieved knowledge, answer the query:\n\n{retrieved_text}\n\nQuery: {query}"
        llm_response = generate_llm_response(llm_prompt)

        
        return format_response(data={"llm_response": llm_response, "retrieved_context": retrieved_text})
    
    except Exception as e:
        log_message(f"Error in knowledge search: {str(e)}", "error")
        return HTTPException(status_code=500, detail="Error retrieving knowledge.")
