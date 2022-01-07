import time
import requests
from getuseragent import UserAgent

from bs4 import BeautifulSoup

while True:
    useragent = UserAgent()
    user = useragent.Random()

    header = {
        'user_agent': user
    }

    responce = requests.get("https://coinmarketcap.com/", headers=header).text
    soup = BeautifulSoup(responce, 'lxml')

    blocks = soup.find('tbody').find_all('tr')
    #print(len(blocks)) #Определяем какое количество блоков tr на странице

    for coin in blocks:
        coin_name = coin.find(class_='cmc-link').get('href') #Перебираем все элементы класса cmc-link

        if 'bitcoin' in coin_name:
            price_block = coin.find(class_='sc-131di3y-0')
            coin_price = price_block.find('a').text
            result = f'BITCOIN: {coin_price}'
            print(result, end='')
            time.sleep(5)
            print('\b' * len(result), end='', flush=True)

            break
