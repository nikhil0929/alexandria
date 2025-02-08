# MVP

### High level game plan

- Google Drive
- Connect it to an LLM
- Create a UI for the LLM
  - Should be able to:
    - Search through a document and provide answers
    - Create tables/graphs for person to see and visualize
    - Look through database
    - Come up with search results + why it’s useful
    - Help ideate Revise documents

## RAG approach

### Steps

1. **Data Ingestion and Collection**
   1. Notion, Google Docs, Slack, internal wikis. For each source, create connectors or use their APIs to pull the data.
   2. **Schedule Data Extraction:**
      1. Automate periodic extraction to keep your knowledge base updated, especially if your documents or messages change over time.
2. **Data Pre Processing**
   1. Cleaning and normalization
      1. convert various file formats to plain text
         1. Clean the text by removing unnecessary formatting, duplicates, or any irrelevant information.
      2. Chunking Large Documents:
         1. split long documents into smaller, meaningful chunks.(smaller chunks can be more precisely matched to a query).
3. **Embedding and Indexing**
   1. Generate embeddings
      1. convert cleaned/chunked text into vector representations using an **embedding model**
         1. OpenAI embeddings API
         2. SentenceTransformers API
         3. more idk
   2. Build a vector store
      1. store embeddings in a vector database
         1. FAISS: open source library for similarity search
         2. pgVector with postgres
         3. Pinecone and Milvus (managed solutions)
4. **Retrieval Mechanism**
   1. Query embedding
      1. When a user submits a query, convert it into an embedding using the same model that generated your document embeddings.
   2. Similarity Search
      1. Search the vector store to retrieve the most relevant document chunks based on similarity to the query embedding.
      2. This retrieval step effectively narrows down the context for the chatbot.
   3. **Context Aggregation:**
      1. Combine the retrieved chunks to form a coherent context that can be provided to the language model.
5. **Integration with a Language Model (LLM)**
   1. Prompt Engineering / Retrieval-Augmented Generation (RAG):
      1. leverage your retrieved context as part of the prompt to an existing language model.
         1. For instance, the prompt might include the query followed by “Relevant context:” and the text from your documents.
         2. This approach is known as retrieval-augmented generation and helps the model generate more accurate and context-aware responses.
   2. Model Selection:
      1. Decide whether to use a commercial API like ChatGPT or an open-source alternative like Deepseek r1.
   3. Optional Fine-Tuning:
      1. If prompt engineering alone isn’t sufficient, consider fine-tuning the model on a curated set of domain-specific Q&A pairs or documents. This fine-tuning is usually lighter than training a model from scratch and can significantly improve accuracy in specialized domains.
6. **Backend and frontend integration**
   1. Create backend with FastAPI
      - Receives user queries.
      - Performs the embedding and retrieval steps.
      - Constructs prompts for the language model.
      - Communicates with the chosen LLM API to get responses.
      - Returns the generated response to the frontend.
   2. Database management
      1. Use Postgres to store metadata, logs, and possibly even raw documents for auditing or further processing
   3. Frontend in React (using NextJS)
      1. interface to communicate with backend API
