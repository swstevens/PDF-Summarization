
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.chat_model import ChatOpenAI
from langchain.callbacks import get_openai_callback
from pypdf import PdfReader

def process_text(text):
    # process text into chunks and use those chunks to create embeddings to divide text
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)

    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    return knowledge_base

def summarizer(pdf):
    # function that summarizes the pdf reader
    pdf_reader = PdfReader(pdf)
    text = ""
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # process text into chunks and use those chunks to create embeddings to divide text
    knowledge_base = process_text(text)

    # load question answering chain
    query= "Summarize the document in 3-5 sentences."
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k", chain_type="stuff")

    if knowledge_base is not None:
        docs = knowledge_base.similarity_search(query)

        # load question answering chain
    chain = load_qa_chain(llm, chain_type="stuff")
    
    response = chain.run(input_documents=docs, question=query)

    return response

