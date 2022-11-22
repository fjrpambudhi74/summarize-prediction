import streamlit as st

#NLP

#Summary Packages
from gensim.summarization import summarize
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer

#Function Summarize

#Web Scrapping

def main():

  st.title("Summary and Entity Checker")
  activities = ["Summarize", "NER Checker", "NER for URL"]
  choice = st.sidebar.selectbox("Select Activity", activities)

  if choice == "Summarize":
    st.subheader("Summary with NLP")
    raw_text = st.text_area("Enter text here")
    st.write(raw_text)


if __name__ == '__main__':
  main()
