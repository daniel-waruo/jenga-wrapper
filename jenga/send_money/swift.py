from . import (
    SendMoney as BaseSendMoney,
    Recipient as BaseRecipient,
    Transaction as BaseTransaction
)


class Recipient(BaseRecipient):
    def __init__(self, full_name: str, account_number: str, swift_code: str, address: str, country_code: str = 'KE'):
        self.full_name = full_name
        self.account_number = account_number
        self.country_code = country_code
        self.swift_code = swift_code
        self.address = address

    def to_dict(self):
        return {
            "type": "bank",
            "countryCode": self.country_code,
            "name": self.full_name,
            "accountNumber": self.account_number,
            "bankBic": self.swift_code,
            "addressline1": self.address
        }


class Transaction(BaseTransaction):
    def __init__(self, transaction_reference: str, amount: float, description: str, currency_code: str = 'KES',
                 charge_option="SELF"):
        self.transaction_reference = transaction_reference
        self.amount = amount
        self.currency_code = currency_code
        self.description = description
        assert charge_option in ["SELF", "OTHER"]
        self.charge_option = charge_option

    def to_dict(self):
        return {
            "type": "SWIFT",
            "amount": str(self.amount),
            "currencyCode": self.currency_code,
            "reference": self.transaction_reference,
            "date": self.date,
            "description": self.description,
            "chargeOption": self.charge_option
        }


class SendMoney(BaseSendMoney):
    """
        The swift web-service enables your application to send cross-border remittances
    """
    transaction_class = Transaction
    recipient_class = Recipient

    def get_signature_string(self):
        return f"{self.transaction.transaction_reference}{self.transaction.date}" \
               f"{self.sender.account_number}{self.recipient.account_number}" \
               f"{self.transaction.amount}"
