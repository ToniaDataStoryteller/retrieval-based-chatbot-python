# 🤖 Simple Retrieval-Based Chatbot: Research & Development


### Developed by: Tonia M. Ethuakhor | Date: March 2026


**Project Type:** Natural Language Processing (NLP) / Retrieval-Based Chatbot  

**Framework:** Python & NLTK (Natural Language Toolkit)  

**GitHub Repository:** [retrieval-based-chatbot-python](https://github.com/ToniaDataStoryteller/retrieval-based-chatbot-python)

---


## 📝 **Executive Summary**
This project documents the development of a retrieval-based chatbot using Natural Language Processing (NLP). It tracks the transition from raw text data to a searchable corpus using mathematical similarity to ensure reliable, grounded responses.


## 🎯 **Project Overview & Objective**
The goal is to build a reliable system that finds the best answer from a specific text file. This chatbot identifies exact word matches between a user's question and the provided knowledge base.


### **How it works:**
1.  **Preparation:** The system reads a text file and breaks it down into individual sentences.

2.  **Cleaning:** It removes common filler words (stopwords) and simplifies words to their roots (lemmatisation).

3.  **Matching:** The bot identifies the Intersection (shared words) and Union (total unique words) between the query and the data.

4.  **Scoring:** It calculates a confidence score using Jaccard Similarity. The bot only displays the highest-scoring sentence if it is above zero.

By following this logic, the chatbot avoids hallucinations, ensuring every response is factual and grounded in the source data.


## 📚 **Data Source & Model Attribution**
*   **Data Source:** A custom knowledge base (`chatbot.txt`) containing facts about chatbot history and technology. 

*   **Dataset Access:** [View chatbot.txt here](./chatbot.txt)

*   **Tools Used:** Python 3.12, NLTK, and Streamlit.


## 🚀 **Key Technical Achievements**
*   **Modular NLP Pipeline:** Engineered a system that cleans and standardises text for efficient processing.

*   **Mathematical Retrieval:** Implemented a transparent Jaccard Similarity scoring system for predictable results.

*   **Input Safeguards:** Added validation to handle "noisy" or empty inputs (e.g., `???`), ensuring system stability.

*   **Data Persistence:** Utilised **Pickle** to save the processed corpus, enabling near-instant loading for the web application.


## 🚧 **Technical Challenges**
*   **Semantic Variance:** As the bot uses exact word matching, it may not recognise synonyms (e.g., "helper" vs "chatbot").

*   **Encoding Errors:** Resolved a `UnicodeDecodeError` by switching to **Latin-1** encoding to handle special characters in the source text.

*   **Data Limits:** The bot's intelligence is strictly bounded by the information contained in the provided text file.

## 📖 **Glossary**
*   **Tokenisation:** Breaking paragraphs into individual sentences or words.

*   **Lemmatisation:** Changing a word back to its simplest form (e.g., "talking" to "talk").

*   **Jaccard Similarity:** A mathematical measure of how similar two sets of words are.

*   **Corpus:** The collection of text data used to inform the chatbot.

*   **Stopwords:** Common words (like "the", "is") that the bot ignores to focus on key terms.

*   **Data Persistence:** Saving the bot's "learning" to a file so it isn't lost when the program closes.


## 🏁 **Summary & Next Steps**
This project serves as a strong foundation for building factual AI tools.


### **Immediate Next Step:**
*   **Create the Streamlit App:** Launch the standalone `app.py` to provide a user-friendly web interface.


### **Future Next Steps:**
*   **Improve Semantic Matching:** Upgrade to **TF-IDF** or **Sentence Embeddings** to understand synonyms.

*   **Web Deployment:** Host the application live via Streamlit Community Cloud.
