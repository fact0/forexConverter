from app import app
from unittest import TestCase


class FlaskTests(TestCase):

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_home_page(self):
        """Check if home page returns status code when rendering correctly"""
        with self.client:
            response = self.client.get('/')
            self.assertEqual(response.status_code, 200)
            self.assertIn(
                b'Welcome to the Forex Currency Converter!', response.data)
            self.assertIn(b'Continue to Converter', response.data)

    def test_render_form(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client:
            response = self.client.get('/form')
            self.assertEqual(response.status_code, 200)
            self.assertIn(b'Converting From:', response.data)
            self.assertIn(b'Converting to:', response.data)
            self.assertIn(b'Amount:', response.data)

    def test_convert_currency(self):
        """Test if arguments passed in return correctly"""
        with self.client:
            response = self.client.get(
                '/convert?currency-from=USD&currency-to=USD&currency-amnt=1')
            self.assertIn(b'US$ 1', response.data)
            self.assertIn(b'US$ 1.00', response.data)
