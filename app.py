import streamlit as st

#NLP
import spacy
from spacy import displacy
nlp = spacy.load("en_core_web_sm")
HTML_WRAPPER = """<div style="overflow-x: auto; border: 1px solid #e6e9ef; border-radius: 0.25rem; padding: 1rem">{}</div>"""

##Summary Packages
# Gensim Packages
from gensim.summarization import summarize
# Sumy Packages
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lex_rank import LexRankSummarizer
# URL Summarize Packages
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Function Prediction Summary
def sumy_summarizer(docx):
	parser = PlaintextParser.from_string(docx, Tokenizer("english"))
	lex_summarizer = LexRankSummarizer()
	summary = lex_summarizer(parser.document, 3)
	summary_list = [str(sentence) for sentence in summary]
	result = ' '.join(summary_list)
	return result

#Function Analyze entity text
# @st.cache(allow_output_mutation=True)
def analyze_text(text):
	return nlp(text)

# Function Fetch text from URL
@st.cache
def get_text(raw_url):
	page = urlopen(raw_url)
	soup = BeautifulSoup(page)
	fetched_text = ' '.join(map(lambda p: p.text, soup.find_all('p')))
	return fetched_text


# Styling
hide_menu = """
<style>
#MainMenu {
  visibility: hidden;
}
footer {
  visibility: visible;
  position: relative;
  margin: auto;
  text-align: center;
  font-weight: 600;
}
footer:after {
  content: 'Develop by Fajar Pambudhi ⚡';
  display: block;
  position: relative;
  color: tomato;
  padding: 5px 0;
  top: 3px;
  font-weight: 800;
}
</style>
"""

#Web Scrapping
def main():

  st.title("Summary and Entity Prediction")
  st.markdown(hide_menu, unsafe_allow_html=True)
  activities = ["Summarize", "NER Checker", "NER URL"]
  choice = st.sidebar.selectbox("Select Activity", activities)


  # Summarize text
  if choice == "Summarize":
    st.subheader("Summary Prediction")
    raw_text = st.text_area("Enter text here")
    summary_choice = st.selectbox(
        "Summary Choice", ["Gensim", "Sumy Lex Rank"])
    if st.button("Summarize"):
      if summary_choice == "Gensim":
        summary_result = summarize(raw_text)

      elif summary_choice == "Sumy Lex Rank":
        summary_result = sumy_summarizer(raw_text)

      st.write(summary_result)

  #Entity check from text
  if choice == 'NER Checker':
    st.subheader("Entity Recognition")
    raw_text = st.text_area("Enter Text Here")

    if st.button("Analyze"):
    #NLP
        docx = analyze_text(raw_text)
        html = displacy.render(docx,style="ent")
        html = html.replace("\n\n","\n")
        st.write(HTML_WRAPPER.format(html),unsafe_allow_html=True)

  # Summarize text from URL
  if choice == 'NER URL':
    st.subheader("Analyze Text From URL")
    raw_url = st.text_input("Enter URL Here")
    text_preview_length = st.slider("Length to Preview", 50, 100)
    if st.button("Analyze"):
      if raw_url != "Type here":
        result = get_text(raw_url)
        len_of_full_text = len(result)
        len_of_short_text = round(len(result)/text_preview_length)
        st.success("Full Text Length = {}".format(len_of_full_text))
        st.info(result[:len_of_short_text])
        summarized_docx = sumy_summarizer(result)
        docx = analyze_text(summarized_docx)
        html = displacy.render(docx, style="ent")
        html = html.replace("\n\n", "\n")
        st.success("Summarize Text Length = {}".format(len_of_short_text))
        st.write(html,unsafe_allow_html=True)


# Main Function
if __name__ == '__main__':
  main()
