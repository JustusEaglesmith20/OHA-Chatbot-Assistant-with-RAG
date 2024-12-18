import os
from flask import Flask, request, render_template, jsonify
from langchain_chroma import Chroma
from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from dotenv import load_dotenv

load_dotenv()

# Get the OpenAI API Key
openai_api_key = os.getenv("OPENAI_API_KEY")
if not openai_api_key:
    raise EnvironmentError("Missing OPENAI_API_KEY in environment variables")

os.environ['OPENAI_API_KEY'] = openai_api_key

# Set up Flask app
app = Flask(__name__)

# Initialize vector database
persist_directory = "./db"
vector_db = Chroma(
    persist_directory=persist_directory,
    embedding_function=OpenAIEmbeddings()  
)

# Create retriever
retriever = vector_db.as_retriever(search_kwargs={"k": 4})

# Initialize LLM
llm = ChatOpenAI(model="gpt-4")  
qa_chain = RetrievalQA.from_chain_type(llm=llm,
                                       chain_type="stuff",
                                       retriever=retriever,
                                       return_source_documents=True)

# Helper function to process the LLM output
def process_llm_response(llm_response):
    result = llm_response["result"]
    sources = [doc.metadata.get("source", "Unknown source") for doc in llm_response.get("source_documents", [])]
    for doc in llm_response.get("source_documents", []):
        print(doc)
        print("")
    return result, sources

# Home route to display the form
@app.route("/")
def home():
    return render_template("home.html")

# API route to process user input dynamically
@app.route("/api/process", methods=["POST"])
def process_input():
    try:
        # Extract the user input from the request
        user_input = request.json.get("user_input", "")
        if not user_input:
            return jsonify({"error": "Input cannot be empty"}), 400
        
        # Run the RAG pipeline
        response = qa_chain({"query": user_input})
        result, sources = process_llm_response(response)

        # Return the result and sources as JSON
        return jsonify({"result": result, "sources": sources})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
