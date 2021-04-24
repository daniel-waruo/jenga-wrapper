from jenga.send_money import (
    SendMoney as BaseSendMoney,
    Recipient as BaseRecipient,
    Transaction as BaseTransaction
)


class Recipient(BaseRecipient):
    def __init__(self, full_name: str, account_number: str, phone_number: str, bank_code: str,
                 country_code: str = 'KE'):
        self.full_name = full_name
        self.account_number = account_number
        self.country_code = country_code
        self.bank_code = bank_code
        self.phone_number = phone_number

    def to_dict(self):
        return {
            "type": "bank",
            "countryCode": self.country_code,
            "name": self.full_name,
            "accountNumber": self.account_number,
            "mobileNumber": self.phone_number,
            "bankCode": self.bank_code
        }


class Transaction(BaseTransaction):
    def to_dict(self):
        return {
            "type": "PesaLink",
            "amount": str(self.amount),
            "currencyCode": self.currency_code,
            "reference": self.transaction_reference,
            "date": self.date,
            "description": self.description
        }


class SendMoney(BaseSendMoney):
    """
    This web service enables an application to send money to a PesaLink participating bank.
    It is restricted to Kenya.
    """
    transaction_class = Transaction
    recipient_class = Recipient

    def get_signature_string(self):
        return f"{self.transaction.amount}{self.transaction.currency_code}" \
               f"{self.transaction.transaction_reference}{self.recipient.full_name}" \
               f"{self.sender.account_number}"
