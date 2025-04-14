import unittest
from app.user_controller import UserController

class TestUserController(unittest.TestCase):
    def setUp(self):
        self.controller = UserController()
        self.controller.register_user("test", "1234")

    def test_register_success(self):
        self.assertTrue(self.controller.register_user("new", "pass"))

    def test_register_existing(self):
        self.assertFalse(self.controller.register_user("test", "1234"))

    def test_register_missing_username(self):
        with self.assertRaises(ValueError):
            self.controller.register_user("", "123")

    def test_register_missing_password(self):
        with self.assertRaises(ValueError):
            self.controller.register_user("user", "")

    def test_login_success(self):
        self.assertTrue(self.controller.login_user("test", "1234"))

    def test_login_wrong_password(self):
        self.assertFalse(self.controller.login_user("test", "0000"))

    def test_login_no_username(self):
        with self.assertRaises(ValueError):
            self.controller.login_user("", "")

    def test_login_nonexistent_user(self):
        self.assertFalse(self.controller.login_user("nonexistent", "pass"))
    
    def test_login_missing_password(self):
        with self.assertRaises(ValueError):
            self.controller.login_user("test", "")

# Chạy test
if __name__ == "__main__":
    unittest.main()
