from django.test import TestCase, TransactionTestCase
from .models import Post
from django.urls import reverse


# Create your tests here.


class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(text="Just a text")

    def test_text_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.text}'
        self.assertEqual(expected_object_name, 'Just a text')


class HomePageView(TestCase):
    def setUp(self):
        Post.objects.create(text='This is another text')

    def text_view_url_exists_at_proper_location(self):
        resp = self.client.get('/posts/')
        self.assertEqual(resp.status_code, 200)

    def test_view_url_by_name(self):
        resp = self.client.get(reverse('home_post'))
        self.assertEqual(resp.status_code, 200)

    def test_view_uses_correct_template(self):
        resp = self.client.get(reverse('home_post'))
        self.assertEqual(resp.status_code, 200)
        self.assertTemplateUsed(resp, 'posts/main.html')
