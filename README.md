# JU1-AI
Gen Ai

💰📊 FinAdvisor AI – Personal Finance Assistant with RAG
🧠 Project Idea:
FinAdvisor AI is a personalized finance assistant that helps users understand and manage their finances using conversational AI. It includes:

An AI chat agent for personal finance queries

A RAG-powered Q&A system over financial policy documents (PDFs)

Spend analysis & basic financial planning tips based on user inputs

Built-in finance glossary for user education

🔑 Key Features:
Feature	Description
🧠 AI Agent Chat	Chat with an AI assistant for queries on loans, savings, mutual funds, etc.
📄 PDF RAG Q&A	Upload policy documents or T&Cs and ask specific questions
📊 Budget Breakdown	Enter income & expenses → get suggestions on saving vs. spending
🧾 Financial Glossary	Look up financial jargon in simple terms
📅 Monthly Planner (Optional)	Suggests budget allocations and reminders

# 1. Clone the repo
git clone https://github.com/yourusername/FinAdvisor-AI.git
cd FinAdvisor-AI

# 2. Install dependencies
pip install -r requirements.txt

# 3. Pull Ollama model
ollama pull tinyllama

# 4. Run app
streamlit run app.py
