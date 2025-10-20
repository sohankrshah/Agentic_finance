from crewai import Task
from finance_crew import create_analysis_agent

def company_info_task(symbol, llm=None):
    agent = create_analysis_agent(llm=llm)
    return Task(
        description=(
            f"Provide a comprehensive company profile for the Indian stock '{symbol}'. "
            f"Include the full company name, sector, industry classification, headquarters location, "
            f"key executives, and a detailed business summary explaining what the company does, "
            f"its core operations, and its role in the Indian economy."
        ),
        expected_output=(
            "A structured company profile containing: full name, sector, industry, headquarters, "
            "CEO or key executives, and a detailed business summary of operations and market role."
        ),
        agent=agent
    )

def fundamental_task(symbol, llm=None):
    agent = create_analysis_agent(llm=llm)
    return Task(
        description=(
            f"Analyze the fundamental financial metrics for the Indian stock '{symbol}'. "
            f"Include current price, market capitalization, trading volume, P/E ratio, EPS, dividend yield, "
            f"return on equity, profit margins, total revenue, revenue growth, net income, beta, debt-to-equity ratio, "
            f"enterprise value, and free cash flow. Provide insights on valuation and financial health."
        ),
        expected_output=(
            "A detailed breakdown of key financial metrics with interpretation: valuation ratios, profitability, "
            "growth indicators, leverage, and cash flow strength."
        ),
        agent=agent
    )

def technical_task(symbol, llm=None):
    agent = create_analysis_agent(llm=llm)
    return Task(
        description=(
            f"Perform technical analysis for the Indian stock '{symbol}' using historical price data. "
            f"Generate a chart showing price trends over time, and include indicators such as moving averages (SMA/EMA), "
            f"Relative Strength Index (RSI), MACD, Bollinger Bands, and support/resistance levels. "
            f"Summarize the current technical outlook and potential trading signals."
        ),
        expected_output=(
            "A technical chart with annotated indicators and a summary of trend direction, momentum, and trading signals."
        ),
        agent=agent
    )

def sentiment_task(symbol, llm=None):
    agent = create_analysis_agent(llm=llm)
    return Task(
        description=(
            f"Conduct a sentiment analysis for the Indian stock '{symbol}' based on recent news articles, analyst reports, "
            f"and social media discussions. Identify whether the sentiment is predominantly positive, negative, or neutral. "
            f"Highlight key events or narratives driving sentiment and estimate the buzz level or investor attention."
        ),
        expected_output=(
            "A sentiment summary with polarity (positive/negative/neutral), key drivers of sentiment, and buzz intensity."
        ),
        agent=agent
    )
