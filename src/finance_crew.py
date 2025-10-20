from crewai import Crew, Agent
from finance_tasks import (
    company_info_task,
    fundamental_task,
    technical_task,
    sentiment_task
)

def create_analysis_agent(llm=None):
    return Agent(
        role="Financial Analyst",
        goal="Analyze Indian stocks and provide insights.",
        backstory="You are an expert in equity research and financial modeling. You understand company fundamentals, technical indicators, and market sentiment.",
        llm=llm,
        verbose=False
    )

def create_stock_analysis_crew(symbol, options, llm=None):
    tasks = []

    if "company" in options:
        tasks.append(company_info_task(symbol, llm=llm))

    if "fundamental" in options:
        tasks.append(fundamental_task(symbol, llm=llm))

    if "technical" in options:
        tasks.append(technical_task(symbol, llm=llm))

    if "sentiment" in options:
        tasks.append(sentiment_task(symbol, llm=llm))

    if not tasks:
        raise ValueError("No valid analysis options selected.")

    agents = [task.agent for task in tasks]

    crew = Crew(
        agents=agents,
        tasks=tasks,
        verbose=True
    )

    return crew
