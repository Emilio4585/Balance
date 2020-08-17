from django.test import TestCase, SimpleTestCase


# Create your tests here.
class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get('/pages/')
        self.assertEqual(response.status_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get('/pages/about/')
        self.assertEqual(response.status_code, 200)
