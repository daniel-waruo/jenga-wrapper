import json

from . import JengaApi
from .utils import send_request


class Account(JengaApi):
    is_live = False

    def get_account_balance(self, country_code, account_id):
        # get jenga bearer token
        bearer_token = self._get_bearer_token()
        # get string to be signed
        signature_string = f"{country_code}{account_id}"
        # get the signature that will be sent in headers
        signature = self._get_jenga_signature(signature_string)
        # prepare the headers
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'signature': signature
        }
        # url to be used
        url = f"https://uat.jengahq.io/account/v2/accounts/balances/{country_code}/{account_id}"
        response = send_request(url=url, method='GET', headers=headers)
        return response

    def get_opening_and_closing_balance(self, country_code, account_id, date):
        bearer_token = self._get_bearer_token()
        # get signature
        signature_string = f"{account_id}{country_code}{date}"
        signature = self._get_jenga_signature(signature_string)
        headers = {
            'Authorization': f'Bearer {bearer_token}',
            'Content-Type': 'application/json',
            'signature': signature
        }
        data = {
            'countryCode': country_code,
            'accountId': account_id,
            'date': date
        }
        url = 'https://uat.jengahq.io/account/v2/accounts/accountbalance/query'
        response = send_request(url=url, method='POST', headers=headers, body=json.dumps(data))
        return response
