import unittest
import sys
import os

# Thêm đường dẫn root vào PYTHONPATH
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.user_controller import UserController

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.controller = UserController()
        self.controller.register_user("test", "1234")

    def test_register_success(self):
        self.assertTrue(self.controller.register_user("new", "pass"))

    def test_register_existing(self):
        self.assertFalse(self.controller.register_user("test", "1234"))

    def test_login_success(self):
        self.assertTrue(self.controller.login_user("test", "1234"))

    def test_login_wrong_password(self):
        self.assertFalse(self.controller.login_user("test", "0000"))

if __name__ == "__main__":
    unittest.main()
