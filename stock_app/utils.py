import requests

def get_stock_price(symbol):
    api_key = 'E99XMHGICFXXSFFJ'  # Alpha Vantage API key
    url = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol={symbol}&interval=1min&apikey={api_key}'
    response = requests.get(url)
    data = response.json()

    if "Time Series (1min)" not in data:
        return None

    latest_data = data['Time Series (1min)']
    latest_timestamp = list(latest_data.keys())[0]  # Get the latest timestamp
    latest_price = latest_data[latest_timestamp]['4. close']  # Get the latest closing price
    return latest_price
