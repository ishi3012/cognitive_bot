"""
Code Assistance API for generating and executing AI code snippets. 
"""

from fastapi import APIRouter, HTTPException
from backend.config import config
from backend.utils.helpers import format_response, log_message
from backend.models import generate_llm_response
router = APIRouter()

@router.get("/generate/")
async def generate_code(prompt: str):
    """
    Generates Python code based on the user prompt.
    """

    try:
        log_message(f"Generating code for prompt: {prompt}", "info")
        
        # Create an instruction-specific prompt for Mistral 7B
        llm_prompt = f"Generate Python code for the following request: \n\n{prompt}\n\n Provide well-commented, executable code."

        generate_code = generate_llm_response(llm_prompt)

        return format_response(data={"code":generate_code})
    
    except Exception as e:
        log_message(f"Error in code generation: {str(e)}", "error")
        raise HTTPException(status_code=500, detail="Error generating code.")