# 📄 Document Analyzer

A modern Streamlit app to analyze, search, summarize, and extract keywords from PDF and DOCX documents.

## Features

- **Upload** PDF or DOCX files
- **Extract** and view document text
- **Semantic Search**: Find the most relevant sentence for your query
- **Summarize**: Get a concise summary of your document
- **TF-IDF Keywords**: Extract top keywords
- **Token Count**: See how many tokens your document contains
- **Modern UI/UX**: Responsive, clean, and user-friendly interface

## File Structure

```
.
├── app.py
├── file_utils.py
├── model_utils.py
├── custom_css.py
├── requirements.txt
└── README.md
```

## Setup

1. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the app**  
   ```bash
   streamlit run app.py
   ```

3. **Open in your browser**  
   Streamlit will provide a local URL (usually http://localhost:8501).

## Notes

- For best results, upload clear, text-based documents.
- Summarization uses the `facebook/bart-large-cnn` model (requires internet on first run).
- All processing is local; your documents are not uploaded to any server.



---
Made with ❤️ using [Streamlit](https://streamlit.io/)
