# Talk to your PDF
Chat with your PDF using Python, Langchain and OpenAI

## Installation

### Prerequisites

1. Python 3.11 or higher
1. Git
1. OpenAI API key

### Steps
1. Clone the repository
    ```bash
    git clone https://github.com/margitantal68/rag_pdf
    ```

1. Navigate to the project directory
    ```bash
    cd rag_pdf
    ```

1. Create and activate a virtual environment
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

1. Install dependencies
    ```bash
    pip install -r requirements.txt
    ```


## Usage

This project requires an OpenAI API key. Follow these steps to set it up:

1. Obtain your OpenAI API key from [OpenAI's website](https://platform.openai.com/docs/overview).
1. Copy the **.env.example** file in the project directory:
    ```bash
    cp .env.example .env
    ```

1. Set the API key in the **.env** file:
    ```bash
    OPENAI_API_KEY=your_api_key_here
    ```

1. Run the project:
    ```bash
    python main.py
    ```

