from crewai import Agent, LLM
import os
from tools.stock_research_tool import get_stock_price
from dotenv import load_dotenv
load_dotenv()

# initialize the llm
llm = LLM(
    model="groq/llama-3.3-70b-versatile",
    api_key=os.getenv("GROQ_API_KEY"),
    temperature=0.0
)

analyst_agent = Agent(
    role="Financial Market Analyst",
    goal=("Perform in-depth evaluation of publicly traded stocks using real-time data,"
          "identifying trends, performance insights, and key financial signals to support"
          "decision-making"),
    backstory=("You are a veteran financial analyst with deep expertise in interpreting stock"
               "market data, technical trends, and fundamentals. You specialize in producing"
               "well-structures reports that evaluate stock performance using live market indicators."),
    llm=llm,
    tools=[get_stock_price],
    verbose=True  # show us what the agent is thinking, we see all the steps
)
