class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"{self.first_name} {self.last_name}")

    def greet_user(self):
        print(f"Hello {self.first_name} {self.last_name}")
    
    def increment_login_attempts(self):
        self.login_attempts += 1
    
    def reset_login_attempts(self):
        self.login_attempts = 0


user1 = User('Gerard', 'Cada')
user2 = User('Bryan', 'Bayona')
user3 = User('Kent', 'De Asis')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()

print(user1.login_attempts)

user1.reset_login_attempts()

print(user1.login_attempts)
        