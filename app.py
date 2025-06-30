import os
os.environ["TF_CPP_MIN_LOG_LEVEL"] = "2"

import streamlit as st
from file_utils import load_docx, load_pdf
from model_utils import get_sentence_transformer, get_summarizer
from custom_css import set_custom_css
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import tiktoken

st.set_page_config(page_title="Document Analyzer", layout="wide")

# --- Sidebar ---
with st.sidebar:
    st.image("https://img.icons8.com/ios-filled/100/4F8BF9/document--v1.png", width=80)
    st.markdown("## 📄 Document Analyzer")
    st.markdown("**Upload a PDF or DOCX and:**")
    st.markdown("- 🔍 Search for relevant sentences\n- ✨ Summarize content\n- 🏷️ Extract keywords\n- 🔢 Count tokens")
    st.markdown("---")
    st.info("**Tip:** For best results, upload clear, text-based documents.")

# --- Custom CSS ---
set_custom_css()

st.markdown("<div style='margin-bottom:1.5rem'></div>", unsafe_allow_html=True)

uploaded_file = st.file_uploader(
    "📤 <b>Upload a PDF or DOCX file</b>",
    type=["pdf", "docx"],
    help="Supported formats: PDF, DOCX",
    label_visibility="visible"
)

if uploaded_file:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("<div class='section-title'>📝 Extracted Text</div>", unsafe_allow_html=True)
    filetype = uploaded_file.type
    if filetype == "application/pdf":
        text = load_pdf(uploaded_file)
    elif filetype == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        text = load_docx(uploaded_file)
    else:
        st.error("Unsupported file type.")
        st.stop()
    with st.expander("Show/Hide Text"):
        st.write(text)
    st.markdown("</div>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🔍 Semantic Search</div>", unsafe_allow_html=True)
        st.caption("Find the most relevant sentence in your document.")
        query = st.text_input("Enter your search query:")
        if st.button("Search", key="search"):
            if query:
                model = get_sentence_transformer()
                sentences = [s for s in text.split(". ") if s.strip()]
                embeddings = model.encode(sentences)
                query_emb = model.encode([query])[0]
                scores = np.dot(embeddings, query_emb) / (np.linalg.norm(embeddings, axis=1) * np.linalg.norm(query_emb) + 1e-8)
                top_idx = int(np.argmax(scores))
                st.success(f"**Best match:** {sentences[top_idx]}")
            else:
                st.warning("Please enter a search query.")
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🏷️ Top Keywords (TF-IDF)</div>", unsafe_allow_html=True)
        st.caption("Extract the most important keywords from your document.")
        if st.button("Extract Keywords", key="keywords"):
            vectorizer = TfidfVectorizer(stop_words='english', max_features=10)
            X = vectorizer.fit_transform([text])
            keywords = vectorizer.get_feature_names_out()
            st.success(", ".join(keywords))
        st.markdown("</div>", unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>✨ Summarize Document</div>", unsafe_allow_html=True)
        st.caption("Get a concise summary of your document.")
        if st.button("Summarize", key="summarize"):
            summarizer = get_summarizer()
            from transformers import AutoTokenizer
            tokenizer = AutoTokenizer.from_pretrained("facebook/bart-large-cnn")
            inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=1024)
            input_ids = inputs["input_ids"]
            if input_ids.shape[1] < 30:
                st.warning("Document is too short to summarize.")
            else:
                summary = summarizer(tokenizer.decode(input_ids[0], skip_special_tokens=True), max_length=130, min_length=30, do_sample=False)[0]['summary_text']
                st.success(summary)
        st.markdown("</div>", unsafe_allow_html=True)

        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.markdown("<div class='section-title'>🔢 Token Count</div>", unsafe_allow_html=True)
        st.caption("Count the number of tokens in your document.")
        if st.button("Count Tokens", key="tokens"):
            enc = tiktoken.get_encoding("cl100k_base")
            tokens = enc.encode(text)
            st.success(f"Token count: {len(tokens)}")
        st.markdown("</div>", unsafe_allow_html=True)

else:
    st.markdown(
        "<div style='color:#888; text-align:center; margin-top:2rem; font-size:1.1rem;'>⬆️ Please upload a PDF or DOCX file to begin.</div>",
        unsafe_allow_html=True
    )