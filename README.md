# AI MENTOR  

**AI MENTOR** is a Retrieval-Augmented Generation (RAG) based learning platform tailored to help students and professionals master foundational AI concepts. The platform leverages state-of-the-art technologies to create an interactive and intelligent AI tutor.

---

## Features  

### 1. **AI Knowledge Base**  
The platform provides a robust knowledge base focused on the following areas:  
- **Machine Learning**: Basics, algorithms, and best practices.  
- **Deep Learning**: Neural networks, CNNs, RNNs, and transformers.  
- **Natural Language Processing (NLP)**: Tokenization, embeddings, and state-of-the-art LLMs.  
- **Computer Vision**: Image classification, object detection, and visual embeddings.  

Content sources include:  
- Research papers (e.g., arXiv, Semantic Scholar).  
- Textbooks (e.g., *Deep Learning* by Goodfellow et al.).  
- Online courses (e.g., Coursera, edX).  

### 2. **Query Answering**  
- Get concise, accurate, and relevant answers to questions.  
- Powered by a RAG pipeline that retrieves context-specific documents and generates AI-assisted responses.

### 3. **Web Interface**  
- A simple, user-friendly web app to input questions and view responses.  
- Designed for accessibility and efficiency.  

---

## Tech Stack  
- **Backend**: [FastAPI](https://fastapi.tiangolo.com/), [LangChain](https://www.langchain.com/), [Haystack](https://github.com/deepset-ai/haystack).  
- **Frontend**: [Streamlit](https://streamlit.io/) or React (planned).  
- **LLM**: OpenAI GPT or equivalent model for response generation.  
- **Vector Database**: [Weaviate](https://weaviate.io/), [Pinecone](https://www.pinecone.io/), or [Milvus](https://milvus.io/).  

---

## Project Structure  
```plaintext
AI-Mentor/
│
├── data/                    # Raw and processed knowledge base materials  
│   ├── raw/                 # Unprocessed files  
│   ├── processed/           # Cleaned and chunked documents  
│
├── src/                     # Source code  
│   ├── ingestion/           # Scripts for data collection and preprocessing  
│   ├── retrieval/           # Document retrieval logic  
│   ├── qa/                  # Query answering pipeline  
│   ├── ui/                  # Web interface code  
│
├── models/                  # Pretrained and fine-tuned models  
├── tests/                   # Unit and integration tests  
├── requirements.txt         # Python dependencies  
├── README.md                # Project documentation  
└── LICENSE                  # License (optional)  
```

## Installation 
### Prerequisites
- Python 3.8+
- Virtual environment (recommended)

### Steps

#### 1. Clone the Repository:

```python
git clone https://github.com/ishi3012/ai-mentor  
cd AI-MENTOR  
```

#### 2. Set Up the Environment:

```python
python -m venv venv  
source venv/bin/activate
```

#### 3. Install Dependencies:

```python
pip install -r requirements.txt  
```

#### 4. Start the Application:
- Backend
```python
uvicorn src.main:app --reload  
```
- Frontend 
```python
streamlit run src/ui/app.py  
```

## Usage
- Access the web interface via your browser at http://127.0.0.1:8000 (or the Streamlit link).
- Enter a question about AI (e.g., "What is a convolutional neural network?").
- Receive a detailed response powered by the RAG system.

## Milestones
- Week 1-2: Collect and preprocess AI learning materials.
- Week 3-4: Build the RAG pipeline.
- Week 5-6: Develop and deploy the web interface.

## Contributing
Contributions are welcome! Please submit a pull request or open an issue for any suggestions or bug reports.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
Feel free to reach out for questions or collaborations:

Email: shilpa.musale02@gmail.com
GitHub: Shilpa Musale


