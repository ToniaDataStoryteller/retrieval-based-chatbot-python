"""
Project Title: 🤖 Simple Retrieval-Based Chatbot

Developed by: Tonia M. Ethuakhor | 📅 Date: March 2026

Description: A web interface for a knowledge-retrieval chatbot 
             featuring a dashboard sidebar and p project glossary
"""

# --- Import necessary libraries ---
import streamlit as st
import nltk
import pickle
import os
import string
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# --- Essential NLTK data downloads for cloud deployment ---
nltk.download("punkt", quiet=True)
nltk.download("punkt_tab", quiet=True) 
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

# --- Page Configuration ---
st.set_page_config(page_title="AI Chatbot Portal", page_icon="🤖", layout="wide")

# --- Tool Initialisation ---
lemmatizer = WordNetLemmatizer()

def clean_input(text):
    """Standardises user input for keyword matching."""
    tokens = word_tokenize(text)
    # Punctuation removal to ensure clean matching with the saved model
    cleaned = [lemmatizer.lemmatize(w.lower()) for w in tokens if w not in string.punctuation]
    return cleaned

# --- Data Loading ---
@st.cache_resource
def load_chatbot_model():
    """Loads the saved sentences and processed keywords from the research phase."""
    model_path = "chatbot_model.pkl" 
    try:
        with open(model_path, "rb") as f:
            sentences, cleaned_corpus = pickle.load(f)
        return sentences, cleaned_corpus
    except FileNotFoundError:
        return None, None

sentences, cleaned_corpus = load_chatbot_model()

# --- Chatbot Logic ---
def get_best_match(user_query):
    query_words = clean_input(user_query)
    
    if not query_words or not sentences:
        return "Please enter a valid question.", 0.0

    best_score = 0.0
    best_index = 0
    
    for i, sentence_words in enumerate(cleaned_corpus):
        # Calculate Jaccard Similarity (Intersection over Union)
        shared = set(query_words).intersection(sentence_words)
        total = set(query_words).union(sentence_words)
        score = len(shared) / float(len(total)) if total else 0

        if score > best_score:
            best_score = score
            best_index = i

    # Return the retrieved sentence and the numerical score
    if best_score > 0:
        return sentences[best_index], round(best_score, 2)
    else:
        return "No relevant answer was found in the knowledge base.", 0.0

# --- Sidebar Configuration ---
with st.sidebar:
    st.title("⚙️ Project Dashboard")
    
    # 1. Project Context
    st.markdown("### About")
    st.info("This is a Retrieval-Based AI system designed to provide factual answers from a local knowledge base.")
    
    # 2. Guided Interaction 
    st.markdown("### Quick Start Questions")
    prepared_questions = [
        "Select a question...",
        "What is a chatterbot?",
        "How does a chatbot help customers?",
        "Can a chatbot simulate human conversation?",
        "Tell me about messenger."
    ]
    selected_question = st.selectbox("Choose a common query:", prepared_questions)
    
    # 3. Informational Glossary (Collapsible)
    with st.expander("📖 Project Glossary"):
        st.markdown("""
        * **Tokenisation:** Breaking text into single words.
        * **Lemmatisation:** Simplifying words to their root form.
        * **Intersection:** The specific words found in both the question and the answer.
        * **Union:** All the unique words found in both the question and answer combined.
        * **Confidence Score:** A measure of match accuracy (0.0 to 1.0).
        * **NLTK:** The Natural Language Toolkit for Python.
        * **Corpus:** The collection of text data used for answers.
        """)
    
    # 4. External Verification
    st.markdown("### Source Code")
    st.markdown("[🔗 GitHub Repository](https://github.com/ToniaDataStoryteller/retrieval-based-chatbot-python)")
    st.markdown("[🔗 LinkedIn Profile](https://linkedin.com/in/tonia-ethuakhor)") 

# --- Main User Interface ---
st.title("🤖 Knowledge-Based Chatbot")
st.markdown("#### Developed by Tonia M. Ethuakhor")

# Determining Input Method (Typed vs. Selected)
if selected_question != "Select a question...":
    query = selected_question
else:
    query = st.text_input("Type your query below:", placeholder="e.g. What is a chatterbot?")

# Processing User Query
if query:
    if sentences:
        answer, score = get_best_match(query)
        st.write("---")
        
        # Displaying the Confidence Score for transparency
        st.write(f"**Confidence Score:** `{score}`")
        
        # Displaying the retrieved response in a success box
        st.success(f"**Bot:** {answer}")
    else:
        st.error("Model not found. Please ensure 'chatbot_model.pkl' is in the application folder.")

# --- Footer ---
st.divider()
st.caption("March 2026 | Built with Python, NLTK & Streamlit")