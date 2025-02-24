from pybithumb import Bithumb
import time
import hmac
import json
import dotenv
import os
import jwt
import uuid
import time
import requests
import dbconn
from urllib.parse import urlencode
import hashlib

dotenv.load_dotenv()


bidcnt = 1
svrno = os.getenv("server_no")
mainver = "bt241117001"

# Set API parameters
apiUrl = 'https://api.bithumb.com'
keys = dbconn.getuserkey(1)
accessKey = keys[0]
secretKey = keys[1]
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

def bidlimitprice(coinn, bidvol, bidprice):
    requestBody = dict(market=coinn, side='bid', volume=bidvol, price=bidprice, ord_type='limit')
    query = urlencode(requestBody).encode()
    hash = hashlib.sha512()
    hash.update(query)
    query_hash = hash.hexdigest()
    payload = {
        'access_key': accessKey,
        'nonce': str(uuid.uuid4()),
        'timestamp': round(time.time() * 1000),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }
    jwt_token = jwt.encode(payload, secretKey)
    authorization_token = 'Bearer {}'.format(jwt_token)
    headers = {
        'Authorization': authorization_token,
        'Content-Type': 'application/json'
    }
    try:
        # Call API
        resp = requests.post(apiUrl + '/v1/orders', data=json.dumps(requestBody), headers=headers)
        # handle to success or fail
        print(resp.status_code)
        print(resp.json())
    except Exception as err:
        # handle exception
        print(err)


def asklimitprice(coinn, bidvol, bidprice):
    requestBody = dict(market=coinn, side='ask', volume=bidvol, price=bidprice, ord_type='limit')
    query = urlencode(requestBody).encode()
    hash = hashlib.sha512()
    hash.update(query)
    query_hash = hash.hexdigest()
    payload = {
        'access_key': accessKey,
        'nonce': str(uuid.uuid4()),
        'timestamp': round(time.time() * 1000),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }
    jwt_token = jwt.encode(payload, secretKey)
    authorization_token = 'Bearer {}'.format(jwt_token)
    headers = {
        'Authorization': authorization_token,
        'Content-Type': 'application/json'
    }
    try:
        # Call API
        resp = requests.post(apiUrl + '/v1/orders', data=json.dumps(requestBody), headers=headers)
        # handle to success or fail
        print(resp.status_code)
        print(resp.json())
    except Exception as err:
        # handle exception
        print(err)


def checkmarketchance(coinn):
    param = dict(market=coinn)
    # Generate access token
    query = urlencode(param).encode()
    hash = hashlib.sha512()
    hash.update(query)
    query_hash = hash.hexdigest()
    payload = {
        'access_key': accessKey,
        'nonce': str(uuid.uuid4()),
        'timestamp': round(time.time() * 1000),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }
    jwt_token = jwt.encode(payload, secretKey)
    authorization_token = 'Bearer {}'.format(jwt_token)
    headers = {
        'Authorization': authorization_token
    }
    try:
        # Call API
        response = requests.get(apiUrl + '/v1/orders/chance', params=param, headers=headers)
        # handle to success or fail
        print(response.status_code)
        print(response.json())
    except Exception as err:
        # handle exception
        print(err)


def checkmyorders(coinn):
    param = dict(market=coinn, limit=100, page=1, order_by='desc')
    uuids = [
        'C0106000032400700021', 'C0106000043000097801'
    ]
    query = urlencode(param)
    uuid_query = '&'.join([f'uuids[]={uuid}' for uuid in uuids])
    query = query + "&" + uuid_query
    # Generate access token
    hash = hashlib.sha512()
    hash.update(query.encode())
    query_hash = hash.hexdigest()
    payload = {
        'access_key': accessKey,
        'nonce': str(uuid.uuid4()),
        'timestamp': round(time.time() * 1000),
        'query_hash': query_hash,
        'query_hash_alg': 'SHA512',
    }
    jwt_token = jwt.encode(payload, secretKey)
    authorization_token = 'Bearer {}'.format(jwt_token)
    headers = {
        'Authorization': authorization_token
    }
    try:
        # Call API
        response = requests.get(apiUrl + '/v1/orders?' + query, headers=headers)
        # handle to success or fail
        print(response.status_code)
        print(response.json())
    except Exception as err:
        # handle exception
        print(err)


def get_orders(market="KRW-XRP", limit=100, page=1, order_by="desc"):
    endpoint = "/v1/orders"
    url = apiUrl + endpoint
    # 요청 파라미터 설정
    params = {
        "market": market,    # 거래 시장 (예: "KRW-BTC", "KRW-ETH")
        "limit": limit,      # 조회할 주문 개수
        "page": page,        # 페이지 번호
        "order_by": order_by # 정렬 기준 ("desc" or "asc")
    }
    # 현재 타임스탬프 (밀리초 단위)
    nonce = str(int(time.time() * 1000))
    # 쿼리 스트링 생성
    query_string = urlencode(params)
    # HMAC-SHA512 서명 생성
    data = f"{endpoint}\0{query_string}\0{nonce}"
    signature = hmac.new(secretKey.encode(), data.encode(), hashlib.sha512).hexdigest()

    # 요청 헤더 설정
    headers = {
        "Api-Key": accessKey,
        "Api-Sign": signature,
        "Api-Nonce": nonce,
        "Content-Type": "application/x-www-form-urlencoded"
    }
    # API 요청 실행
    response = requests.get(url + "?" + query_string, headers=headers)
    print(response.status_code)
    return response.json()

# 주문 목록 조회 실행
orders = get_orders('KRW-XRP')
print(orders)