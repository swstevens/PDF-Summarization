import streamlit as st
import langchain
import os
from utils import *
from dotenv import load_dotenv

def main():
    load_dotenv()
    st.set_page_config(page_title="Summarize Your PDF")

    st.title("PDF Summarizer")
    st.write("Upload your PDF and ask questions about its content.")
    st.divider()

    pdf = st.file_uploader("Upload your PDF", type="pdf")

    submit = st.button("Generate Summary")

    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    if submit:
        response = summarizer(pdf)
        st.subheader("Summary of File: ")
        st.write(response)

if __name__ == '__main__':  
    main()