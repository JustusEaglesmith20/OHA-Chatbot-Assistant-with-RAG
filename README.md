# Flask-LangChain App

A Flask application that integrates **LangChain**, **OpenAI GPT-4**, and **Chroma vector database** to provide a dynamic question-answering experience with Retrieval-Augmented Generation (RAG). This app uses a combination of backend intelligence and user-friendly design to deliver contextual and accurate responses.

---

## Features
- **Question-Answering**: Users can ask natural language questions, and the app responds with answers backed by relevant document sources.
- **Context-Aware Responses**: Maintains conversation context for enhanced understanding.
- **RAG Architecture**: Combines a vector database retriever with GPT-4 for intelligent responses.
- **User-Friendly Interface**: Built with Flask and a responsive frontend for seamless user interaction.
- **Secure Configuration**: API keys are managed securely using environment variables.

---

## Technologies Used
- **Backend**:
  - [Flask](https://flask.palletsprojects.com/): Python web framework.
  - [LangChain](https://www.langchain.com/): Framework for building language model applications.
  - [Chroma](https://www.trychroma.com/): Vector database for document embeddings.
  - [OpenAI GPT-4](https://openai.com/): Large Language Model for generating intelligent responses.
  
- **Frontend**:
  - HTML, CSS (Bootstrap for responsive design).
  - JavaScript (Axios for API interaction).

- **Environment Management**:
  - `python-dotenv` for loading environment variables.

---

## Setup and Installation

### Prerequisites
- Python 3.8 or above installed.
- OpenAI API key.
- [LangChain API key](https://docs.langchain.com/).

---

### 1. Clone the Repository
git clone https://github.com/your-username/flask-langchain-app.git
cd flask-langchain-app

2. Set Up a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate   # On macOS/Linux
venv\Scripts\activate      # On Windows
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Configure Environment Variables
Create a .env file in the project root:

plaintext
Copy code
# OpenAI API Key
OPENAI_API_KEY=your_openai_api_key_here

# LangChain API Key
LANGCHAIN_API_KEY=your_langchain_api_key_here

# Optional Hugging Face Key
OHP_LLM=your_huggingface_api_key_here
5. Initialize the Vector Database
Ensure the ./db directory contains your pre-processed document embeddings.

To build the vector database:
Use a document loader and embedding function compatible with Chroma.
Save embeddings to ./db.
6. Run the Application
bash
Copy code
python app.py
The app will start locally at http://127.0.0.1:5000/.

Usage
1. Ask Questions
Navigate to the homepage, enter your question, and click "Submit." The app will display an intelligent response along with the sources used.

2. Reset Conversation
Send /reset as a query to clear the conversation history.

File Structure
plaintext
Copy code
flask-langchain-app/
│
├── app.py               # Main Flask application
├── requirements.txt     # Python dependencies
├── .env                 # Environment variables (not included in version control)
├── db/                  # Vector database directory
├── templates/           # HTML templates
│   └── home.html        # Main frontend page
├── static/              # Optional static files (CSS, JS, images)
└── README.md            # Project documentation
Customization
1. Adjust Number of Results
Modify the number of documents retrieved:

python
Copy code
retriever = vector_db.as_retriever(search_kwargs={"k": 4})  # Change `k` as needed
2. Change the Frontend
Update templates/home.html to customize the UI or add new features like file uploads.

Troubleshooting
Common Issues
Environment Variables Not Loaded:
Ensure python-dotenv is installed.
Verify the .env file path and content.
Flask Not Running:
Check Python version compatibility.
Ensure dependencies are installed.
Debugging
Add debug prints to inspect API keys or request data:

print(os.getenv("OPENAI_API_KEY"))  # For testing only, remove in production.

Future Enhancements
Add user authentication for personalized experiences.
Deploy to a cloud platform (e.g., Render, AWS).
Expand document sources for enhanced knowledge.
Contributing
Fork the repository.
Create a feature branch:
git checkout -b feature-name
Commit your changes:
git commit -m "Add feature-name"
Push to the branch:
git push origin feature-name
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for details.
