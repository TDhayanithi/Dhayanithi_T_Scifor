import streamlit as st
from txtai.pipeline import Summary, Textractor
from PyPDF2 import PdfReader

st.set_page_config(layout="wide")

@st.cache_resource
def text_summary(text, maxlength=None):
    #create summary instance
    summary = Summary()
    text = (text)
    result = summary(text)
    return result

choice = st.sidebar.selectbox("Select your choice", ["Summarize Text", "Summarize Document"])

if choice == "Summarize Text":
    st.subheader("Summarize Text using txtai")
    input_text = st.text_area("Enter your text here")
    if input_text is not None:
        if st.button("Summarize Text"):
            col1, col2 = st.columns([1,1])
            with col1:
                st.markdown("**Your Input Text**")
                st.info(input_text)
            with col2:
                st.markdown("**Summary Result**")
                result = text_summary(input_text)
                st.success(result)

   
                
