import unittest
from decimal import Decimal
from app.models.account import Account
from app.models.user import User

class TestAccount(unittest.TestCase):
    def test_to_dict(self):
        user = User(username='test_user', email='test@gmail.com', password_hash='hashedpass')
        account = Account(
            user=user,
            account_type='Savings',
            account_number='12345',
            balance=Decimal('1000.00') 
        )

        expected_dict = {
            'id': None,
            'user_id': user.id,
            'account_type': 'Savings',
            'account_number': '12345',
            'balance': '1000.00',
            'created_at': None,
            'updated_at': None
        }

        self.assertEqual(account.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
