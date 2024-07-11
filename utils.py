
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chat_models import ChatOpenAI
from langchain.callbacks import get_openai_callback
from pypdf import PdfReader

def process_text(text):
    """
    This function takes a text as input, splits it into chunks, and then creates embeddings for these chunks.
    The embeddings are used to divide the text into manageable parts for further processing.
    """
    # Initialize the text splitter with specific parameters
    text_splitter = CharacterTextSplitter(
        separator="\n",  # Split text at newline characters
        chunk_size=1000,  # Each chunk will be 1000 characters long
        chunk_overlap=200,  # Each chunk will overlap with the previous chunk by 200 characters
        length_function=len  # Use the built-in len function to calculate the length of the text
    )

    # Split the text into chunks
    chunks = text_splitter.split_text(text)

    # Initialize the embeddings model
    embeddings = OpenAIEmbeddings(model="text-embedding-ada-002")
    
    # Create a knowledge base from the chunks using the embeddings
    knowledge_base = FAISS.from_texts(chunks, embeddings)

    return knowledge_base

def summarizer(pdf):
    """
    This function takes a PDF file as input, extracts the text from it, and then summarizes the text.
    It uses the process_text function to split the text into chunks and create embeddings.
    """
    # Initialize the PDF reader
    pdf_reader = PdfReader(pdf)
    text = ""

    # Extract text from each page of the PDF
    for page in pdf_reader.pages:
        text += page.extract_text()
    
    # Process the text into chunks and create embeddings
    knowledge_base = process_text(text)

    # Define the query for summarization
    query= "Summarize the document in 3-5 sentences."

    # Initialize the language model
    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k")

    # If the knowledge base is not empty, search for relevant documents
    if knowledge_base is not None:
        docs = knowledge_base.similarity_search(query)

    # Load the question answering chain
    chain = load_qa_chain(llm, chain_type="stuff")
    
    # Run the question answering chain to get the summary
    response = chain.run(input_documents=docs, question=query)

    return response
