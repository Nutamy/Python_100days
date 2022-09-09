import requests
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "QZ3HPQDTWMIF9GYZ"
NEWS_API_KEY = "c5b1aed00f8f4d668c0044e4c4707841"
stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY
}
stock_response = requests.get(STOCK_ENDPOINT, params=stock_params).json()
stock_data = stock_response["Time Series (Daily)"]
data_list = [value for (key, value) in stock_data.items()]
yesterday = list(stock_response["Time Series (Daily)"])[0]
day_before_yesterday = list(stock_response["Time Series (Daily)"])[1]

print(yesterday)
yesterday_close = float(stock_response["Time Series (Daily)"][yesterday]["4. close"])
day_before_yesterday_close = float(stock_response["Time Series (Daily)"][day_before_yesterday]["4. close"])
difference = abs(yesterday_close - day_before_yesterday_close)
percentage = round(difference*100/yesterday_close, 2)
print(f"""yesterday_close = {yesterday_close}
day_before_yesterday_close = {day_before_yesterday_close}
difference = {difference}
percentage = {percentage}%""")

news_params = {
    "q": COMPANY_NAME,
    "language": "ru",
    "sortBy": "relevance",
    "apiKey": NEWS_API_KEY
}
news_response = requests.get(NEWS_ENDPOINT, params=news_params).json()["articles"][:3]

for news in news_response:
    print(f"""
    Title: {news["title"]}
    {news["description"]}
    link: {news["url"]}
    """)