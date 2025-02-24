from pybithumb import Bithumb
import time
import dotenv
import os
import jwt
import uuid
import time
import requests

dotenv.load_dotenv()


bidcnt = 1
svrno = os.getenv("server_no")
mainver = "bt241117001"
conkey = "b9858a715f322bd851eef2cf952928d3"
seckey = "e726fdb7a7b2ee1f89b6b7b1d97dbda1"

# Set API parameters
accessKey = 'da8c907047d63e4f43b3e7a1d5ac5d4e4d99503f4a708b'
secretKey = 'M2MxOTkxMzAxOTFjYzhmNTliNzI0MGQzM2Q0ZDMwYzNlMWE1ZDRhYzVmNGU0YTk5NTczNjQzNzQ4OTIwNg=='
apiUrl = 'https://api.bithumb.com'

# Generate access token
payload = {
    'access_key': accessKey,
    'nonce': str(uuid.uuid4()),
    'timestamp': round(time.time() * 1000)
}
jwt_token = jwt.encode(payload, secretKey)
authorization_token = 'Bearer {}'.format(jwt_token)
headers = {
  'Authorization': authorization_token
}

def checkwallet():
    try:
        # Call API
        response = requests.get(apiUrl + '/v1/accounts', headers=headers)
        # handle to success or fail
        print(response.status_code)
        resp = response.json()
        for item in resp:
            print(item)
    except Exception as err:
        # handle exception
        print(err)
    finally:
        print('done')

def getmarketcode():
    url = "https://api.bithumb.com/v1/market/all?isDetails=true"

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)

def getcandlem(coinn,cnt):
    url = "https://api.bithumb.com/v1/candles/minutes/1?market="+coinn+"&count="+str(cnt)

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)


def getcandled(coinn,cnt):
    url = "https://api.bithumb.com/v1/candles/days?market="+coinn+"&count="+str(cnt)

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)


def getcandlew(coinn,cnt):
    url = "https://api.bithumb.com/v1/candles/weeks?market="+coinn+"&count="+str(cnt)

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)


def gettrticks(coinn,cnt):
    url = "https://api.bithumb.com/v1/trades/ticks?market="+coinn+"&count="+str(cnt)

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)


def getmarketprice(coinn):
    url = "https://api.bithumb.com/v1/ticker?markets="+coinn

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)


def getorderbook(coinn):
    url = "https://api.bithumb.com/v1/orderbook?markets="+coinn

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)
        for order in item['orderbook_units']:
            print(order)


def getalarm():
    url = "https://api.bithumb.com/v1/market/virtual_asset_warning"

    headers = {"accept": "application/json"}

    resp = requests.get(url, headers=headers)

    for item in resp.json():
        print(item)

def apicheck():
    try:
        # Call API
        resp = requests.get(apiUrl + '/v1/api_keys', headers=headers)
        # handle to success or fail
        print(resp.status_code)
        for item in resp.json():
            print(item)
    except Exception as err:
        # handle exception
        print(err)

apicheck()