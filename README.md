# AI Financial Assistant

## Overview
**AI Financial Assistant** is a powerful tool powered by advanced AI models, combining functionalities of two agents:  
- **Web Search Agent**: For retrieving up-to-date information from the web.  
- **Finance AI Agent**: For financial data analysis, including stock prices, analyst recommendations, company news, and stock fundamentals.  

The project includes an intuitive **Streamlit web interface** to query these agents and obtain actionable insights, displayed in a user-friendly format.

---

## Features
- **Financial Data Analysis**:
  - Stock Prices
  - Analyst Recommendations
  - Company News
  - Stock Fundamentals
- **Web Search**:
  - Retrieve general information with sources.
- **Streamlit Interface**:
  - Simple UI for input queries and results.
  - Results formatted in Markdown and tables for clarity.

---

## Project Structure
```plaintext
├── financial_agent.py    # AI agents: Finance and Web Search
├── playground.py         # Test and interact with agents
├── app.py                # Streamlit application for end users
├── requirements.txt      # Dependencies for the project
├── .env                  # Environment variables (API keys)
└── README.md             # Project documentation
