import logging
import requests
import base64
import os
from pprint import pprint
# install requests in Ec2 also pip install requests
def getPrice():
    priceUrl = 'https://api.coingecko.com/api/v3/coins/bitcoin'
    headers = {
    "username": "x-cg-pro-api-key",
    "password": "CG-cn3bi3Uo9bNSy8RUNCzBgFLW",
    "Content-Type": "application/json"
    }
    priceResponse = requests.get(priceUrl,headers=headers)
    if(priceResponse.status_code==200):
        logging.info(priceResponse.json())
        return priceResponse;
    else:
        logging.error("Cannot retrive data from Price API {}",priceResponse.text)

def getNews():
    newsUrl = 'https://data-api.coindesk.com/news/v1/article/list?lang=EN&limit=100'
    headers = {
        "password":'8fac26384798ab67b7194c47c12bd642a2be948b5d997aa62b9f56220629ddf3',
        "Content-Type" : 'application/json'
    }
    newsResponse = requests.get(newsUrl,headers=headers)
    if newsResponse.status_code == 200:
        logging.info(newsResponse.json())
        return newsResponse
    else:
        logging.error("Cannot retrive data from News API {}",newsResponse.text)

def getTweets():
    bearer_token = "AAAAAAAAAAAAAAAAAAAAAGP23wEAAAAAtNhZMsmIE6%2BES5cqmFrQxptD0yM%3D6gwhBTBn520noLGje5vCPrkQY5rBrEL8OsxzL9WBcYr1UZWZae";
    url = "https://api.twitter.com/2/tweets/search/recent"

    query_params = {
        'query': "bitcoin OR BTC OR 'bitcoin price' lang:en -is:retweet",
        'max_results': 100,
        'tweet.fields': 'created_at,lang,author_id'
    }

    headers = {"Authorization": f"Bearer {bearer_token}"}

    response = requests.get(url, headers=headers, params=query_params)

    if response.status_code == 200:
        data = response.json()
        pprint(data);
        for tweet in data['data']:
            print(f"{tweet['created_at']} - {tweet['text']}\n")
        return data;
    else:
        print("Error:", response.status_code, response.text)



