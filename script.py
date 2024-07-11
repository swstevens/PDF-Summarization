import streamlit as st
import langchain
import os

def main():
    st.set_page_config(page_title="Ask your PDF")

    st.title("PDF Summarizer")
    st.write("Upload your PDF and ask questions about its content.")
    st.divider()

    pdf = st.file_uploader("Upload your PDF", type="pdf")

    submit = st.button("Generate Summary")

if __name__ == '__main__':  
    main()