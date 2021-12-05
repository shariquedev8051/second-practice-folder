# Building logic
USERNAME = "Sharique"
PASSWORD = "Python@123"

def login(username, password):
    """Checking credentials"""
    if username == USERNAME and password == PASSWORD:
        return "LoggedIn"
    elif len(username) == 0 and len(password) == 0:
        return "Empty credentials"
    else:
        return "Invalid credentials"


# Writting unit test cases
import unittest

class LoginTest(unittest.TestCase):
    """Unit test class"""

    def test_login_with_valid_credentials(self):
        res = login("Sharique", "Python@123")
        self.assertEqual(res, "LoggedIn") #assertEqual test will fail if values differ

    def test_login_with_empyt_credentials(self):
        res = login("", "")
        self.assertEqual(res, "Empty credentials")

    def test_login_with_invalid_credentials(self):
        res = login("Sharique", "Django@123")
        self.assertEqual(res, "Invalid credentials")


# run using main methode
if __name__ == "__main__":  
    unittest.main()