from . import (
    SendMoney as BaseSendMoney,
    Recipient as BaseRecipient,
    Transaction as BaseTransaction
)


class Recipient(BaseRecipient):
    def __init__(self, full_name: str, account_number: str, bank_code: str, country_code: str = 'KE'):
        self.full_name = full_name
        self.account_number = account_number
        self.country_code = country_code
        self.bank_code = bank_code

    def to_dict(self):
        return {
            "type": "bank",
            "countryCode": self.country_code,
            "name": self.full_name,
            "accountNumber": self.account_number,
            "bankCode": self.bank_code,
        }


class Transaction(BaseTransaction):
    def to_dict(self):
        return {
            "type": "RTGS",
            "amount": str(self.amount),
            "currencyCode": self.currency_code,
            "reference": self.transaction_reference,
            "date": self.date,
            "description": self.description
        }


class SendMoney(BaseSendMoney):
    """
    The Real Time Gross Settlement (RTGS) web-service enables an application to send money intra-country to other bank accounts.
    """
    transaction_class = Transaction
    recipient_class = Recipient

    def get_signature_string(self):
        return f"{self.transaction.transaction_reference}{self.transaction.date}" \
               f"{self.sender.account_number}{self.recipient.account_number}" \
               f"{self.transaction.amount}"
