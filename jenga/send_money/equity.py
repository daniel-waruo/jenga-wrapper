from . import (
    SendMoney as BaseSendMoney,
    Recipient as BaseRecipient,
    Transaction as BaseTransaction
)


class Recipient(BaseRecipient):
    def to_dict(self):
        return {
            "type": "bank",
            "countryCode": self.country_code,
            "name": self.full_name,
            "accountNumber": self.account_number
        }


class Transaction(BaseTransaction):
    def to_dict(self):
        return {
            "type": "InternalFundsTransfer",
            "amount": str(self.amount),
            "currencyCode": self.currency_code,
            "reference": self.transaction_reference,
            "date": self.date,
            "description": self.description
        }


class SendMoney(BaseSendMoney):
    """
    Move Funds Within Equity Bank :bank: Across Kenya, Uganda, Tanzania, Rwanda & South Sudan.
    """
    transaction_class = Transaction
    recipient_class = Recipient

    def get_signature_string(self):
        return f"{self.sender.account_number}{self.transaction.amount}" \
               f"{self.transaction.currency_code}{self.transaction.transaction_reference}"
