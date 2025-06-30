from sentence_transformers import SentenceTransformer
from transformers import pipeline

def get_sentence_transformer():
    return SentenceTransformer('all-MiniLM-L6-v2')

def get_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")
