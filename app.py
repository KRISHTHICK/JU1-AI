import streamlit as st
from agent_helper import ask_finance_agent
from rag_helper import ask_rag_qa
from finance_utils import get_budget_advice, load_glossary

st.set_page_config(page_title="FinAdvisor AI", layout="wide")
st.title("💰 FinAdvisor AI – Your Personal Finance Assistant")

st.sidebar.header("📄 Upload Financial Docs (PDF)")
pdfs = st.sidebar.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

st.subheader("🧠 Ask Finance AI Agent")
query = st.text_input("Ask your finance question (e.g., Should I invest in SIP or FD?)")
if query:
    st.markdown(ask_finance_agent(query))

st.divider()
st.subheader("📄 Ask About Uploaded Docs (RAG Q&A)")
if pdfs:
    rag_query = st.text_input("Ask something about the uploaded docs")
    if rag_query:
        st.markdown(ask_rag_qa(rag_query, pdfs))

st.divider()
st.subheader("📊 Budget Breakdown")
income = st.number_input("Monthly Income", min_value=0)
expense = st.number_input("Monthly Expenses", min_value=0)
if st.button("💡 Get Advice"):
    st.markdown(get_budget_advice(income, expense))

st.divider()
st.subheader("📘 Finance Glossary")
glossary = load_glossary()
term = st.text_input("Enter financial term (e.g., NAV, CAGR)")
if term:
    meaning = glossary.get(term.lower(), "Term not found.")
    st.success(meaning)

