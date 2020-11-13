class User():
    """Identify different users."""

    def __init__(self, first_name, last_name):
        """First and last names."""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        """Information about the user."""
        print("\nSummary of the user information.")
        print(self.first_name.title() + ", "
              + self.last_name.title() + ".")

    def greet_user(self):
        print("Hello " + self.first_name.title() + " " +
              self.last_name.title() + ".")

    def read_login_attempts(self):
        """print login attempts."""
        print(str(self.login_attempts))

    def increment_login_attempts(self, attempts):
        """Count login attempts."""
        self.login_attempts += attempts * 1

    def reset_login_attempts(self, reset):
        """Reset the numbe rof login attempts."""
        if reset <= self.login_attempts:
            self.login_attempts = self.login_attempts * 0
            print("Reset")


boss = User('john', 'mann')
boss.describe_user()
boss.greet_user()
boss.increment_login_attempts(2)
boss.read_login_attempts()
boss.reset_login_attempts(1)

boss.read_login_attempts()
