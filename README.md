# PDF Summarizer Web Portal

This Python script creates a simple web portal using Streamlit to summarize PDF documents.

## Features

- Upload PDF files
- Extract text from PDFs
- Generate summaries of PDF content
- Display summaries in a user-friendly web interface

## Requirements

- Python 3.7+
- Streamlit
- PyPDF2
- NLTK

## Installation

1. Clone this repository
2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

Run the script using Streamlit:

```
streamlit run script.py
```

Then, open your web browser and navigate to the provided local URL (typically http://localhost:8501).

## How it works

1. Upload a PDF file through the web interface
2. The script extracts text from the PDF
3. It then generates a summary using NLTK's summarization algorithm
4. The summary is displayed on the web page

## Contributing

Contributions, issues, and feature requests are welcome. Feel free to check the issues page if you want to contribute.

## License

[MIT](https://choosealicense.com/licenses/mit/)
