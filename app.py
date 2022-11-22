import streamlit as st

#NLP

#Summary Packages

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
