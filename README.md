# Talk to your PDF
Chat with your PDF using Python, Langchain and OpenAI

## Installation

### Prerequisites

1. Python 3.11 or higher
2. Git
3. OpenAI API key

### Steps
1. Clone the repository
```bash
git clone https://github.com/margitantal68/rag_pdf
```

2. Navigate to the project directory
```bash
cd rag_pdf
```

3. Create and activate a virtual environment
* On Linux/macOS:
```bash
python3 -m venv venv
source venv/bin/activate
```

* On Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

4. Install dependencies
```bash
pip install -r requirements.txt
```


## Usage

This project requires an OpenAI API key. Follow these steps to set it up:

1. Obtain your OpenAI API key from [OpenAI's website](https://platform.openai.com/docs/overview).
2. Create a **.env** file in the project directory and add your API key:
```bash
OPENAI_API_KEY=your_api_key_here
```

2. Run the project:
```bash
python main.py
```

