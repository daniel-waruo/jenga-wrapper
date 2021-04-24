import json
from datetime import date

from jenga import JengaApi
from jenga.utils import send_request


class Sender(object):
    def __init__(self, full_name: str, account_number: str, country_code: str = 'KE'):
        self.full_name = full_name
        self.account_number = account_number
        self.country_code = country_code

    def to_dict(self):
        return {
            "countryCode": self.country_code,
            "name": self.full_name,
            "accountNumber": self.account_number
        }


class Recipient(object):
    def __init__(self, full_name: str, account_number: str, country_code: str = 'KE'):
        self.full_name = full_name
        self.account_number = account_number
        self.country_code = country_code

    def to_dict(self):
        """
        Converts the object to a dictionary payload
        Returns {
            "destination": {
                "type": "bank",
                "countryCode": self.country_code,
                "name": self.full_name,
                "accountNumber": self.full_name
            }
        }
        """
        raise NotImplementedError("The type of recipient is different for most transacitons")


class Transaction(object):
    def __init__(self, transaction_reference: str, amount: float, description: str, currency_code: str = 'KES',
                 **kwargs):
        self.transaction_reference = transaction_reference
        self.amount = amount
        self.currency_code = currency_code
        self.description = description

    def to_dict(self):
        """ return a dict version ready for returning """
        raise NotImplementedError("One must implement.")

    @property
    def date(self):
        return date.today().strftime("%Y-%m-%d")


class Credentials(object):
    def __init__(self, api_key, merchant_code, merchant_password, private_key):
        self.api_key = api_key
        self.merchant_code = merchant_code
        self.merchant_password = merchant_password
        self.private_key = private_key


class SendMoney(JengaApi):
    sender_class = Sender
    recipient_class = Recipient
    transaction_class = Transaction
    credentials_class = Credentials

    def __init__(self, sender: Sender, recipient: Recipient, transaction: Transaction, credentials: Credentials):
        assert isinstance(credentials, self.credentials_class)
        super().__init__(
            credentials.api_key,
            credentials.merchant_code,
            credentials.merchant_password,
            credentials.private_key
        )
        assert isinstance(sender, self.sender_class)
        self.sender = sender
        assert isinstance(recipient, self.recipient_class)
        self.recipient = recipient
        assert isinstance(transaction, self.transaction_class)
        self.transaction = transaction

    def get_signature_string(self):
        raise NotImplementedError("Implement for every!")

    def get_payload(self):
        return {
            "source": self.sender.to_dict(),
            "destination": self.recipient.to_dict(),
            "transfer": self.transaction.to_dict()
        }

    def get_headers(self):
        return {
            'Authorization': f'Bearer {self._get_bearer_token()}',
            'Content-Type': 'application/json',
            'signature': self._get_jenga_signature(self.get_signature_string())
        }

    def get_response(self):
        url = "https://uat.jengahq.io/transaction/v2/remittance"
        response = send_request(
            url=url,
            method='POST',
            headers=self.get_headers(),
            body=json.dumps(self.get_payload())
        )
        return response
