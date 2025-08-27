# Simple LCEL GenAI Translation Application

A simple language translation application built with LangChain Expression Language (LCEL), FastAPI, and Streamlit. This project demonstrates how to create a translation service using Groq's language models through LangChain's LCEL framework.

## Features

- **Translation Service**: Translate text from English to various languages
- **FastAPI Server**: RESTful API endpoints using LangServe
- **Streamlit Client**: User-friendly web interface
- **LCEL Chains**: Demonstrates LangChain Expression Language usage
- **Multiple Models**: Support for different Groq models (Gemma2-9b-It, llama-3.1-8b-instant)
- **Interactive Playground**: Built-in LangServe playground for testing

## Project Structure

```
├── serve.py                     # Main FastAPI server with Gemma2-9b-It model
├── serve_p.py                   # Alternative FastAPI server with llama-3.1-8b-instant
├── client.py                    # Streamlit client application
├── requirements.txt             # Project dependencies
├── simplellmLCEL.ipynb         # LCEL tutorial and examples
├── simplellmLCEL Practice.ipynb # Additional LCEL practice examples
├── .env                        # Environment variables (not included)
└── README.md                   # This file
```

## Prerequisites

- Python 3.8 or higher
- Groq API key (get one from [Groq Console](https://console.groq.com/))

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/SurajKhodade15/simple_lcem_genai.git
   cd simple_lcem_genai
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
   **Note**: If you encounter issues with the requirements.txt format, you can also install the core dependencies manually:
   ```bash
   pip install langchain langchain-groq fastapi langserve streamlit python-dotenv uvicorn
   ```

4. **Set up environment variables**:
   Create a `.env` file in the root directory:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   ```

## Usage

### 1. Start the FastAPI Server

You can choose between two server configurations:

**Option A: Using Gemma2-9b-It model**:
```bash
python serve.py
```

**Option B: Using llama-3.1-8b-instant model**:
```bash
python serve_p.py
```

The server will start on `http://localhost:8000` or `http://127.0.0.1:8000`.

### 2. Access the API

#### Interactive Playground
Visit `http://127.0.0.1:8000/chain/playground/` to use the built-in LangServe playground.

#### API Endpoint
**POST** `/chain/invoke`

**Request Body**:
```json
{
  "input": {
    "language": "French",
    "text": "Hello, how are you?"
  },
  "config": {},
  "kwargs": {}
}
```

**Response**:
```json
{
  "output": "Bonjour, comment allez-vous ?"
}
```

**cURL Example**:
```bash
curl -X POST "http://127.0.0.1:8000/chain/invoke" \
     -H "Content-Type: application/json" \
     -d '{
       "input": {
         "language": "Spanish",
         "text": "Good morning"
       },
       "config": {},
       "kwargs": {}
     }'
```

### 3. Use the Streamlit Client

In a new terminal (while the server is running):
```bash
streamlit run client.py
```

This will open a web interface where you can enter text and get translations.

## API Documentation

Once the server is running, you can access:
- **Swagger UI**: `http://127.0.0.1:8000/docs`
- **ReDoc**: `http://127.0.0.1:8000/redoc`

## LCEL Chain Structure

The application uses LangChain Expression Language (LCEL) to chain components:

```python
chain = prompt_template | model | parser
```

Where:
- **prompt_template**: ChatPromptTemplate for translation instructions
- **model**: ChatGroq model (Gemma2-9b-It or llama-3.1-8b-instant)
- **parser**: StrOutputParser to format the output

## Jupyter Notebooks

The repository includes two Jupyter notebooks with examples and tutorials:

1. **simplellmLCEL.ipynb**: Basic LCEL concepts and simple translation examples
2. **simplellmLCEL Practice.ipynb**: Advanced LCEL usage and practice exercises

To run the notebooks:
```bash
jupyter notebook
```

## Dependencies

Key dependencies include:
- `langchain`: Core LangChain library
- `langchain-groq`: Groq integration for LangChain
- `fastapi`: Web framework for the API
- `langserve`: LangChain server utilities
- `streamlit`: Frontend framework
- `python-dotenv`: Environment variable management

See `requirements.txt` for the complete list.

## Supported Languages

The application can translate to any language supported by the underlying Groq models. Common examples:
- French
- Spanish
- German
- Italian
- Portuguese
- Chinese
- Japanese
- And many more...

## Troubleshooting

### Common Issues

1. **"GROQ_API_KEY not found"**
   - Make sure you've created a `.env` file with your Groq API key
   - Verify the environment variable name is correct

2. **"Connection refused" errors**
   - Ensure the FastAPI server is running before starting the client
   - Check that the server is running on the correct port (8000)

3. **Import errors**
   - Make sure all dependencies are installed: `pip install -r requirements.txt`
   - Verify you're using the correct Python environment

4. **Pydantic validation errors**
   - This is handled in `serve.py` with the `chainBatchRequest.model_rebuild()` line
   - If issues persist, try using `serve_p.py` instead

### Getting Help

If you encounter issues:
1. Check the server logs for error messages
2. Verify your Groq API key is valid and has sufficient credits
3. Ensure all dependencies are correctly installed
4. Try different models by switching between `serve.py` and `serve_p.py`

## Contributing

Feel free to contribute to this project by:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).