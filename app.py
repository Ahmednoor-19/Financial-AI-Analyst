import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize agents
# Web Search Agent
web_search_agent = Agent(
    name="Web Search Agent",
    role="Search the web for information",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=["Always include sources"],
    show_tools_calls=True,
    markdown=True,
)

# Financial Agent
finance_agent = Agent(
    name="Finance AI Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[
        YFinanceTools(
            stock_price=True,
            analyst_recommendations=True,
            stock_fundamentals=True,
            company_news=True,
        )
    ],
    instructions=["Use tables to display the data"],
    show_tool_calls=True,
    markdown=True,
)

# Streamlit App UI
def main():
    st.title("AI Assistant for Financial Advices")
    st.write("This app lets you query financial informations.")

    # User Input Section
    st.header("Query the AI Agent")
    user_query = st.text_area(
        "Enter your query:",
        placeholder="e.g., Summarize analyst recommendations and share the latest news for NVDA",
    )
    
    if st.button("Submit Query"):
        st.write("Processing your query...")
        
        agent = finance_agent
        
        
        try:
            # Display agent's response
            response = agent.print_response(user_query)
            st.markdown(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()