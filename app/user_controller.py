class UserController:
    def __init__(self):
        self.users = {}  # username: password

    def register_user(self, username, password):
        if not username or not password:
            raise ValueError("Username and password required")
        if username in self.users:
            return False
        self.users[username] = password
        return True

    def login_user(self, username, password):
        if not username or not password:
            raise ValueError("Missing credentials") 
        return self.users.get(username) == password

    def get_user(self, username):
        """Lấy thông tin user theo username"""
        return self.users.get(username)

    def user_exists(self, username):
        """Kiểm tra user có tồn tại không"""
        return username in self.users

    def get_all_users(self):
        """Lấy danh sách tất cả users"""
        return list(self.users.keys())

