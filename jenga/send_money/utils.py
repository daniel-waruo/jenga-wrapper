import json

from jenga.utils import get_jenga_api_token, send_request


def get_pesalink_accounts(api_key, merchant_code, merchant_password, phone_number):
    """return the bank account details of the owner of the phone number """
    response = get_jenga_api_token(
        api_key=api_key,
        merchant_code=merchant_code,
        merchant_password=merchant_password
    )
    bearer_token = response["access_token"]
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',
    }
    data = {
        'mobileNumber': phone_number,
    }
    url = 'https://uat.jengahq.io/transaction/v2/pesalink/inquire'
    response = send_request(url=url, method='POST', headers=headers, body=json.dumps(data))
    return response


def get_mpesa_transaction_status(api_key, merchant_code, merchant_password, request_id, transaction_date):
    """ check status of b2c transaction"""
    response = get_jenga_api_token(
        api_key=api_key,
        merchant_code=merchant_code,
        merchant_password=merchant_password
    )
    bearer_token = response["access_token"]
    headers = {
        'Authorization': f'Bearer {bearer_token}',
        'Content-Type': 'application/json',
    }
    data = {
        "requestId": request_id,
        "destination": {
            "type": "M-Pesa"
        },
        "transfer": {
            "date": transaction_date
        }
    }
    url = 'https://uat.jengahq.io/transaction/v2/pesalink/inquire'
    response = send_request(url=url, method='POST', headers=headers, body=json.dumps(data))
    return response
