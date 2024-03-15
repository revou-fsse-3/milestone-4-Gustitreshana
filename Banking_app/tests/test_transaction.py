import unittest
from decimal import Decimal
from app.models.transaction import Transaction
from app.models.account import Account
from app.models.base import Base  

class TestTransaction(unittest.TestCase):
    def test_to_dict(self):
        from_account = Account(account_number='12345', balance=Decimal('1000')) 
        to_account = Account(account_number='67890', balance=Decimal('500')) 

        transaction = Transaction(
            from_account=from_account,
            to_account=to_account,
            amount=Decimal('50.00'),
            type='Transfer',
            description='Test Transaction' 
        )

        expected_dict = {
            'id': None,
            'from_account_id': from_account.id,
            'to_account_id': to_account.id,
            'amount': '50.00',
            'type': 'Transfer',
            'description': 'Test Transaction',
            'created_at': None
        }

        self.assertEqual(transaction.to_dict(), expected_dict)

if __name__ == '__main__':
    unittest.main()
