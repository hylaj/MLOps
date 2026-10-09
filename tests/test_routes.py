import unittest
from app import health_check, welcome_root


class TestAppRoutes(unittest.TestCase):
    def test_welcome_root(self):
        response = welcome_root()
        self.assertEqual(response, {"message": "Welcome to the ML API"})

    def test_health_check(self):
        response = health_check()
        self.assertEqual(response, {"status": "ok"})


if __name__ == "__main__":
    unittest.main()
