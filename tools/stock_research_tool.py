import yfinance as yf
from crewai.tools import tool


@tool("Live Stock Information Tool")  # Live ... is the name of the tool
def get_stock_price(stock_symbol: str) -> str:
    """
    Retrieves the latest stock price and other relevant info for a given stock symbol
    using Yahoo Finance.
    Parameters:
        stock_symbol (str): The ticker symbol of the stock(AAPL, TSLA, MSFT).
    Returns:
        str: A summary of the stock's current price, daily change, and other key data.
    """
    stock = yf.Ticker(stock_symbol)  # give us the stock info
    info = stock.info

    current_price = info.get("regularMarketPrice")
    change = info.get("regularMarketChange")
    change_percent = info.get("regularMarketChangePercent")
    # if currency is not given get the USD
    currency = info.get("currency", "USD")

    if current_price is None:
        return f"Could not fetch price for {stock_symbol}. Please check the symbol"

    return (
        f"Stock: {stock_symbol.upper()}\n"
        f"Price: {current_price} {currency}\n"
        f"Change: {change} ({round(change_percent, 2)}%)"
    )


# print(get_stock_price("AAPL"))
# it only a test of the function, before to make it as a tool
