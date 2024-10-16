import unittest
import app.controller.user_controller as uc

class EndPointTests(unittest.TestCase):
    async def test_get_user(self):
        admin = {
            'user_id': '1',
            'username': 'admin',
            'email': 'admin@admin.com'
        }
        self.assertEqual(await uc.get_user(1), admin)

    async def test_get_user_not_founded(self):
        self.assertIsNone(await uc.get_user(2))

    async def test_get_user_invalid_id(self):
        self.assertIsNone(await uc.get_user('3'))

if __name__ == '__main__':
    unittest.main()
