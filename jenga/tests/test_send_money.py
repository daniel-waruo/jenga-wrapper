import json
from unittest import TestCase

from jenga.send_money import Sender, Credentials
from jenga.tests import JENGA_API_KEY, JENGA_PASSWORD, JENGA_MERCHANT_CODE, JENGA_PRIVATE_KEY
from jenga.utils import get_jenga_ref


class SendMoneyTest(TestCase):
    def setUp(self) -> None:
        self.private_key = JENGA_PRIVATE_KEY
        self.sender = Sender(
            full_name="Makinika Tech",
            account_number="1160161916079",
            country_code="KE"
        )
        self.credentials = Credentials(
            api_key=JENGA_API_KEY,
            merchant_code=JENGA_MERCHANT_CODE,
            merchant_password=JENGA_PASSWORD,
            private_key=self.private_key
        )
        self.amount = 100

    def test_get_ref(self):
        self.assertEqual(len(get_jenga_ref()), 12)

    def test_send_money_equity(self):
        from jenga.send_money.equity import SendMoney, Recipient, Transaction
        transaction_ref = get_jenga_ref()
        send_money = SendMoney(
            sender=self.sender,
            recipient=Recipient(
                full_name="Tom Doe",
                account_number="0060161911111",
                country_code="KE"
            ),
            transaction=Transaction(
                transaction_reference=transaction_ref,
                amount=self.amount,
                currency_code="KES",
                description="Remitance to equity bank account"
            ),
            credentials=self.credentials,
        )
        response = send_money.get_response()
        status = response.get("status")
        error_message = f"EQUITY Error \n {json.dumps(response, indent=2)}"
        self.assertEqual(status, "SUCCESS", error_message)

    def test_send_money_mobile(self):
        from jenga.send_money.mobile import SendMoney, Recipient, Transaction
        transaction_ref = get_jenga_ref()
        send_money = SendMoney(
            sender=self.sender,
            recipient=Recipient(
                full_name="Jonh Doe",
                phone_number="0797792447",
                wallet="Mpesa",
                country_code="KE"
            ),
            transaction=Transaction(
                transaction_reference=transaction_ref,
                amount=self.amount,
                currency_code="KES",
                description="Remitance to mobile phone"
            ),
            credentials=self.credentials,
        )
        response = send_money.get_response()
        status = response.get("status")
        error_message = f"MOBILE Error \n {json.dumps(response, indent=2)}"
        self.assertEqual(status, "SUCCESS", error_message)

    def test_send_money_eft(self):
        from jenga.send_money.eft import SendMoney, Recipient, Transaction
        transaction_ref = get_jenga_ref()
        send_money = SendMoney(
            sender=self.sender,
            recipient=Recipient(
                full_name="Daniel Waruo Kingangai",
                bank_code="01",
                branch_code="01100",
                account_number="1276805594",
                country_code="KE",
            ),
            transaction=Transaction(
                transaction_reference=transaction_ref,
                amount=self.amount,
                currency_code="KES",
                description="Remitance to eft"
            ),
            credentials=self.credentials,
        )
        response = send_money.get_response()
        status = response.get("status")
        error_message = f"EFT Error \n {json.dumps(response, indent=2)}"
        self.assertEqual(status, "SUCCESS", error_message)

    def test_send_money_rtgs(self):
        from jenga.send_money.rtgs import SendMoney, Recipient, Transaction
        transaction_ref = get_jenga_ref()
        send_money = SendMoney(
            sender=self.sender,
            recipient=Recipient(
                full_name="Jonh Doe",
                bank_code="01",
                account_number="1276805594",
                country_code="KE",
            ),
            transaction=Transaction(
                transaction_reference=transaction_ref,
                amount=self.amount,
                currency_code="KES",
                description="Remittance to rtgs"
            ),
            credentials=self.credentials,
        )
        response = send_money.get_response()
        status = response.get("status")
        error_message = f"RTGS Error \n {json.dumps(response, indent=2)}"
        self.assertEqual(status, "SUCCESS", error_message)

    def test_send_money_swift(self):
        from jenga.send_money.swift import SendMoney, Recipient, Transaction
        transaction_ref = get_jenga_ref()
        send_money = SendMoney(
            sender=self.sender,
            recipient=Recipient(
                full_name="Jonh Doe",
                swift_code="KCBLKENX017",
                account_number="1276805594",
                country_code="KE",
                address="19010-00501 Nairobi, Kenya"
            ),
            transaction=Transaction(
                transaction_reference=transaction_ref,
                amount=self.amount,
                currency_code="USD",
                description="Remitance to swift"
            ),
            credentials=self.credentials,
        )
        response = send_money.get_response()
        status = response.get("status")
        error_message = f"SWIFT Error \n {json.dumps(response, indent=2)}"
        self.assertEqual(status, "SUCCESS", error_message)

    def test_send_money_pesalink_bank(self):
        from jenga.send_money.pesalink.bank import SendMoney, Recipient, Transaction
        transaction_ref = get_jenga_ref()
        send_money = SendMoney(
            sender=self.sender,
            recipient=Recipient(
                full_name="Tom Doe",
                account_number="8323524545",
                bank_code="01",
                country_code="KE",
                phone_number="0722000000"
            ),
            transaction=Transaction(
                transaction_reference=transaction_ref,
                amount=self.amount,
                currency_code="KES",
                description="Remitance to pesalink bank"
            ),
            credentials=self.credentials,
        )
        response = send_money.get_response()
        status = response.get("status")
        error_message = f"PESALINK BANK Error \n {json.dumps(response, indent=2)}" \
                        f"\n{json.dumps(send_money.get_payload(), indent=2)}"
        self.assertEqual(status, "SUCCESS", error_message)

    def test_send_money_pesalink_mobile(self):
        from jenga.send_money.pesalink.mobile import SendMoney, Recipient, Transaction
        transaction_ref = get_jenga_ref()
        send_money = SendMoney(
            sender=self.sender,
            recipient=Recipient(
                full_name="Jonh Doe",
                phone_number="0797792447",
                bank_code="01",
                country_code="KE",
            ),
            transaction=Transaction(
                transaction_reference=transaction_ref,
                amount=self.amount,
                currency_code="KES",
                description="Remitance to pesalink mobile"
            ),
            credentials=self.credentials,
        )
        response = send_money.get_response()
        status = response.get("status")
        error_message = f"PESALINK MOBILE Error \n {json.dumps(response, indent=2)}"
        self.assertEqual(status, "SUCCESS", error_message)

    def test_get_pesalink_banks(self):
        from jenga.send_money.utils import get_pesalink_accounts
        response = get_pesalink_accounts(
            self.credentials.api_key,
            self.credentials.merchant_code,
            self.credentials.merchant_password,
            "0722000000"
        )
        print(json.dumps(response, indent=2))
