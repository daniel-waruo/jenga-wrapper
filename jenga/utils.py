import json
import urllib.parse
from base64 import b64encode

import urllib3
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.serialization import load_pem_private_key

http = urllib3.PoolManager()

base_path = '/home/daniel/PycharmProjects/jenga-wrapper'

from random import randint


def send_request(url, data=None, method='POST', body=None, headers=None):
    """send a request with data to a given url """
    r = http.request(method, url, fields=data, headers=headers, body=body)
    try:
        return json.loads(r.data.decode())
    except json.decoder.JSONDecodeError:
        return r.data


def get_jenga_signature(string: str, private_key: str):
    string = string.encode()
    private_key = load_pem_private_key(private_key.encode(), password=None, backend=default_backend())
    signature = private_key.sign(
        data=string,
        padding=padding.PKCS1v15(),
        algorithm=hashes.SHA256()
    )
    signature = b64encode(signature).decode()
    return signature


def get_jenga_gateway_token(api_key, merchant_code, merchant_password):
    url = "https://api-test.equitybankgroup.com/v1/token"
    data = {
        "merchantCode": merchant_code,
        "password": merchant_password
    }
    encoded_data = urllib.parse.urlencode(data)
    headers = {
        "Authorization": f"Basic {api_key}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    r = http.request(
        method="POST",
        url=url,
        body=encoded_data,
        headers=headers
    )
    try:
        data = json.loads(r.data.decode())
    except json.decoder.JSONDecodeError:
        data = r.data
    return data


def get_jenga_api_token(api_key, merchant_code, merchant_password):
    url = "https://uat.jengahq.io/identity/v2/token"
    data = {
        "username": merchant_code,
        "password": merchant_password
    }
    encoded_data = urllib.parse.urlencode(data)
    headers = {
        "Authorization": f"Basic {api_key}",
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    r = http.request(
        method="POST",
        url=url,
        body=encoded_data,
        headers=headers
    )
    try:
        data = json.loads(r.data.decode())
    except json.decoder.JSONDecodeError:
        data = r.data
    return data


def get_jenga_ref():
    return str(randint(100000000000, 999999999999))
