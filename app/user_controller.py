import re
import hashlib

class UserController:
    def __init__(self):
        self.users = {}  # username: hashed_password
        self.MIN_LENGTH = 3

    def register_user(self, username, password):
        if not username or not password:
            raise ValueError("Username and password required")
        
        if len(username) < self.MIN_LENGTH or len(password) < self.MIN_LENGTH:
            raise ValueError(f"Username and password must be at least {self.MIN_LENGTH} characters")

        if not re.match("^[a-zA-Z0-9_]+$", username):
            raise ValueError("Username can only contain letters, numbers and underscore")

        if username in self.users:
            return False
            
        # Hash password before storing
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.users[username] = hashed_password
        return True

    def login_user(self, username, password):
        if not username or not password:
            raise ValueError("Missing credentials")
            
        stored_hash = self.users.get(username)
        if not stored_hash:
            return False
            
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return stored_hash == hashed_password

