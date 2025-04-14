import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from tests.test_user_controller import TestUserController

if __name__ == '__main__':
    unittest.main()
