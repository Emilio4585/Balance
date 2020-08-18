from django.test import TestCase, TransactionTestCase


# Create your tests here.


class PagesTests(TestCase):
    def test_home_post_status_code(self):
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, 200)
