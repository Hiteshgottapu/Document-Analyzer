import streamlit as st

def set_custom_css():
    st.markdown("""
        <style>
        body {
            background-color: #f5f7fa;
            font-family: 'Segoe UI', 'Roboto', Arial, sans-serif;
        }
        .stApp {
            background: linear-gradient(120deg, #f5f7fa 0%, #c3cfe2 100%);
            min-height: 100vh;
        }
        .stButton>button {
            background-color: #4F8BF9;
            color: #fff;
            border-radius: 10px;
            padding: 0.6em 2em;
            border: none;
            font-weight: 700;
            font-size: 1rem;
            box-shadow: 0 2px 8px rgba(79,139,249,0.10);
            transition: background 0.2s, box-shadow 0.2s, transform 0.1s;
            cursor: pointer;
        }
        .stButton>button:hover {
            background-color: #2563eb;
            color: #fff;
            box-shadow: 0 4px 16px rgba(37,99,235,0.15);
            transform: translateY(-2px) scale(1.03);
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            border: 1.5px solid #4F8BF9;
            padding: 0.6em 1em;
            font-size: 1rem;
            background: #fafdff;
            transition: border 0.2s;
        }
        .stTextInput>div>div>input:focus {
            border: 1.5px solid #2563eb;
            outline: none;
            background: #f0f7ff;
        }
        .stExpander {
            background: #e3eafc;
            border-radius: 10px;
            border: 1.5px solid #b6c6e3;
            margin-bottom: 1rem;
            box-shadow: 0 1px 4px rgba(79,139,249,0.05);
        }
        .stExpanderHeader {
            font-weight: 700;
            color: #2563eb;
            font-size: 1.1rem;
        }
        .stSubheader, .stMarkdown h2 {
            color: #2563eb;
            font-weight: 800;
            letter-spacing: 0.5px;
        }
        .stSuccess {
            background: #e6ffed;
            color: #256029;
            border-radius: 10px;
            padding: 1.2em;
            border-left: 5px solid #34c759;
            margin-bottom: 1rem;
        }
        .card {
            background: #fff;
            border-radius: 14px;
            box-shadow: 0 4px 16px rgba(79,139,249,0.10);
            padding: 2rem 1.5rem 1.5rem 1.5rem;
            margin-bottom: 2rem;
            border: 1.5px solid #e3eafc;
            transition: box-shadow 0.2s;
        }
        .card:hover {
            box-shadow: 0 8px 32px rgba(79,139,249,0.15);
        }
        .section-title {
            font-size: 1.4rem;
            font-weight: 800;
            color: #2563eb;
            margin-bottom: 0.7rem;
            letter-spacing: 0.5px;
        }
        /* Custom scrollbar for webkit browsers */
        ::-webkit-scrollbar {
            width: 8px;
            background: #e3eafc;
        }
        ::-webkit-scrollbar-thumb {
            background: #c3cfe2;
            border-radius: 8px;
        }
        </style>
    """, unsafe_allow_html=True)
