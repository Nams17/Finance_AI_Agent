from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.yfinance import YFinanceTools
from phi.tools.duckduckgo import DuckDuckGo
import openai
import os






api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise EnvironmentError("GROQ_API_KEY not set. Please set the environment variable.")
print(f"Using API key: {api_key[:5]}... (hidden for security)")


## Web Search Agent
web_search_agent = Agent(
    name = "Web Search Agent",
    role = "Search the web for the information",
    model = Groq(id="llama3-8b-8192"),
    tools = [DuckDuckGo()],
    instructions = ("Always include sources"),
    show_tool_calls = True,
    markdown = True
)


## Financial Agent
finance_agent = Agent(
    name = "Finance AI Agent",
    model = Groq(id="llama3-8b-8192"),
    tools = 
        [YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True, company_news=True, technical_indicators=True)]
    ,
    instructions=["Use tables to display the data"],
    show_tool_calls = True,
    markdown = True,

)

multi_ai_agent = Agent(
    team = [web_search_agent,finance_agent],
    model = Groq(id="llama3-8b-8192"),
    instructions = ["Always include sources", "Use table to display the data"],
    show_tool_calls = True,
    markdown = True,
)

multi_ai_agent.update_model = "gpt-3.5-turbo"
multi_ai_agent.print_response("Summarize analyst recommendation and share the latest news for NVDA", stream = True)