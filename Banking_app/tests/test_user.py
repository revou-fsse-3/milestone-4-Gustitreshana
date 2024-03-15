import unittest
from app.models.user import User
from app.models.base import Base

class TestUser(unittest.TestCase):
    def test_to_dict_returns_correct_representation(self):
        user = User(
            id=None,
            username='test_user',
            email='test@gmail.com',
            password_hash='hashedpass'
        )
        expected_dict = {
            'id': None,
            'username': 'test_user',
            'email': 'test@gmail.com',
            'created_at': None,
            'updated_at': None
        }
        self.assertEqual(user.to_dict(), expected_dict)

    def test_repr_returns_correct_string(self):
        user = User(
            username='test_user',
            email='test@gmail.com',
            password_hash='hashedpass'
        )
        self.assertEqual(str(user), '<User test_user>')

if __name__ == '__main__':
    unittest.main()