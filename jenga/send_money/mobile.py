from . import (
    SendMoney as BaseSendMoney,
    Recipient as BaseRecipient,
    Transaction as BaseTransaction
)


class Recipient(BaseRecipient):

    def __init__(self, full_name: str, phone_number: str, wallet: str, country_code: str = 'KE'):
        self.full_name = full_name
        self.phone_number = phone_number
        self.country_code = country_code
        assert wallet in ["Airtel", "Equitel", "Mpesa"]
        self.wallet = wallet

    def to_dict(self):
        return {
            "type": "mobile",
            "countryCode": self.country_code,
            "name": self.full_name,
            "mobileNumber": self.phone_number,
            "walletName": self.wallet
        }


class Transaction(BaseTransaction):
    def to_dict(self):
        return {
            "type": "MobileWallet",
            "amount": str(self.amount),
            "currencyCode": self.currency_code,
            "reference": self.transaction_reference,
            "date": self.date,
            "description": self.description
        }


class SendMoney(BaseSendMoney):
    transaction_class = Transaction
    recipient_class = Recipient

    def get_signature_string(self):
        if self.recipient.wallet == "Equitel":
            return f"{self.sender.account_number}{self.transaction.amount}" \
                   f"{self.transaction.currency_code}{self.transaction.transaction_reference}"
        return f"{self.transaction.amount}{self.transaction.currency_code}" \
               f"{self.transaction.transaction_reference}{self.sender.account_number}"
