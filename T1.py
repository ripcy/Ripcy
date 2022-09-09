import requests
TOKEN = "1583975560:AAEdeLNKEYYWOAXJZHJ37eu7SFJh-U_n8eQ"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
print(requests.get(url).json())
