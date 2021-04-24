from .utils import get_jenga_api_token, get_jenga_signature, send_request, get_jenga_gateway_token


class JengaApi(object):
    def __init__(self, api_key, merchant_code, merchant_password, private_key):
        self.api_key = api_key
        self.merchant_code = merchant_code
        self.merchant_password = merchant_password
        self.private_key = private_key

    def _get_bearer_token(self):
        response = get_jenga_api_token(
            api_key=self.api_key,
            merchant_code=self.merchant_code,
            merchant_password=self.merchant_password
        )
        return response["access_token"]

    def _get_jenga_signature(self, string):
        return get_jenga_signature(string, self.private_key)
