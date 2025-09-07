# HiLabs Roster Email Parser

This project extracts structured data from `.eml` email files and generates a consolidated Excel file. It uses Ollama with the Llama3.2:3b model for parsing and field extraction.

## Prerequisites

- Python 3.11+
- Node.js (for frontend dependencies)
- [Ollama](https://ollama.com/) installed and running
- Llama3.2:3b model downloaded via Ollama

## Setup Instructions

1. **Clone the repository**
   ```sh
   git clone https://github.com/SudhST/HiLabs-Roster.git
   cd HiLabs-Roster
   ```

2. **Set up Python virtual environment**
   ```sh
   python -m venv pyEnv313
   source ./pyEnv313/Scripts/activate
   ```

3. **Install Python dependencies**
   ```sh
   pip install -r requirements.txt
   ```

4. **Install Node.js dependencies**
   ```sh
   npm install
   ```

5. **Install and run Ollama**
   - Download and install Ollama from [here](https://ollama.com/).
   - Download the Llama3.2:3b model:
     ```sh
     ollama run llama3.2:3b
     ```
   - Serve the model on port 11434:
     ```sh
     ollama serve
     ```

## Usage

To run the parser and generate the output Excel file:
```sh
python run_parser.py
```

## Directory Structure

- `emails/` — Contains all input emails in `.eml` format.
- `output/` — Contains the final Excel file with extracted fields.
- `run_parser.py` — Main script to run the email parser.
- `llm_extractor.py` — Handles extraction of fields using the LLM.
- `config.py` — Configuration for folder paths and template file.
- `system_prompt.txt` — System prompt for the LLM.
- `requirements.txt` — Python dependencies.
- `README.md` — Project documentation.