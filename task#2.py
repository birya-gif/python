import requests
from bs4 import BeautifulSoup


url = 'https://twitter.com/elonmusk'
proxy_host = '95.164.201.30'
proxy_port = '9577'
proxy_username = 'zBt7cr'
proxy_password = 'zRX5Cz'
proxies = {
    'http': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}',
    'https': f'http://{proxy_username}:{proxy_password}@{proxy_host}:{proxy_port}'
}


response = requests.get(url, proxies)


if response.status_code == 200:

    soup = BeautifulSoup(response.text, 'html.parser')


    tweets = soup.find_all('span', class_='css-1qaijid r-bcqeeo r-qvutc0 r-poiln3')


    for tweet in tweets[:10]:
        print(tweet.text.strip())
else:
    print(f'Ошибка №: {response.status_code}')
