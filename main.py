import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS
from langchain_openai.embeddings import OpenAIEmbeddings

from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_text_splitters import RecursiveCharacterTextSplitter

load_dotenv()

def setup_qa_system(file_path):
    loader = PyPDFLoader(file_path)
    docs = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    chunks = text_splitter.split_documents(docs)

    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(chunks, embeddings)
    
    retriever = vector_store.as_retriever()
    llm = ChatOpenAI(temperature=0, model_name='gpt-4o')

    system_prompt = (
    "Use the given context to answer the question. "
    "If you don't know the answer, say you don't know. "
    "Use three sentence maximum and keep the answer concise. "
    "Context: {context}"
    )
    prompt = ChatPromptTemplate.from_messages(
        [ ("system", system_prompt), ("human", "{input}")]
    )
    question_answer_chain = create_stuff_documents_chain(llm, prompt)
    chain = create_retrieval_chain(retriever, question_answer_chain)
    return chain


if __name__ == '__main__':
    EN_DOCUMENT = "data/RAG_Evaluation_Survey.pdf"
    HU_DOCUMENT = "data/hatarozatok_249.pdf"

    DOCUMENT = EN_DOCUMENT
    print(f"Using document: {DOCUMENT}")
    qa_chain = setup_qa_system(DOCUMENT)

    while True:
        question = input("\n\n####Ask a question (or type exit): ")
        if question.lower() == 'exit':
            break
    
        answer = qa_chain.invoke({"input": question})
        # Print the context in a structured format
        print("\n\n####Retrieved Context:")
        for doc in answer.get('context', []):
            print(f"\tDocument source: {doc.metadata.get('source', 'No source found')}")
            print(f"\tDocument page: {doc.metadata.get('page', 'No page found')}")
            print(f"\tDocument text: {doc.page_content}")
            print("-" * 80)

        print('\n\n####Answer: ')
        print(answer.get('answer', 'No answer found'))     