import datetime
import json
from unittest import TestCase

from jenga.account import Account
from jenga.tests import JENGA_API_KEY, JENGA_PASSWORD, JENGA_MERCHANT_CODE, JENGA_PRIVATE_KEY


class AccountTest(TestCase):
    def setUp(self) -> None:
        self.country_code = "KE"
        self.account_id = "1160161916079"
        self.private_key = JENGA_PRIVATE_KEY.replace('\\n', '\n')
        self.account = Account(
            api_key=JENGA_API_KEY,
            merchant_code=JENGA_MERCHANT_CODE,
            merchant_password=JENGA_PASSWORD,
            private_key=self.private_key
        )

    def test_get_account_balance(self):
        response = self.account.get_account_balance(
            country_code=self.country_code,
            account_id=self.account_id
        )

        print(json.dumps(response, indent=2))

    def test_get_opening_closing_balance(self):
        response = self.account.get_opening_and_closing_balance(
            country_code=self.country_code,
            account_id=self.account_id,
            date=str(datetime.date.today())
        )
        print(response)
