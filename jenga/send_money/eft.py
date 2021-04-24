from . import (
    SendMoney as BaseSendMoney,
    Recipient as BaseRecipient,
    Transaction as BaseTransaction
)


class Recipient(BaseRecipient):
    def __init__(self, full_name: str, account_number: str, bank_code: str, branch_code: str, country_code: str = 'KE'):
        self.full_name = full_name
        self.account_number = account_number
        self.country_code = country_code
        self.bank_code = bank_code
        self.branch_code = branch_code

    def to_dict(self):
        return {
            "type": "bank",
            "countryCode": self.country_code,
            "name": self.full_name,
            "accountNumber": self.account_number,
            "bankCode": self.bank_code,
            "branchCode": self.branch_code,
        }


class Transaction(BaseTransaction):
    def to_dict(self):
        return {
            "type": "EFT",
            "amount": str(self.amount),
            "currencyCode": self.currency_code,
            "reference": self.transaction_reference,
            "date": self.date,
            "description": self.description
        }


class SendMoney(BaseSendMoney):
    """
    Send Money To Other Banks Via Electronic Funds Transfer (EFT)
    """
    transaction_class = Transaction
    recipient_class = Recipient

    def get_signature_string(self):
        return f"{self.transaction.transaction_reference}{self.sender.account_number}" \
               f"{self.recipient.account_number}{self.transaction.amount}" \
               f"{self.recipient.bank_code}"
