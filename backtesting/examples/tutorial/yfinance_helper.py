import yfinance as yf

def get_data(symbol: str):
    data = yf.download(tickers=symbol, period='5y', interval='1d')
    data.reset_index(inplace=True)
    return data