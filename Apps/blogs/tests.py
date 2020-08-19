from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import PostBlog


# Create your tests here.

class BlogTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='test@email.com',
            password='secret',
        )
        self.post = PostBlog.objects.create(
            title='titulo',
            body='body',
            author=self.user
        )

    def set_string_representation(self):
        post = PostBlog(title='otro titulo')
        self.assertEqual(str(post), post.title)

    def test_post_content(self):
        self.assertEqual(f'{self.post.title}', 'titulo')
        self.assertEqual(f'{self.post.author}', 'testuser')
        self.assertEqual(f'{self.post.body}', 'body')

    def test_post_list_view(self):
        response = self.client.get(reverse('home_blogs'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'body')
        self.assertTemplateUsed(response, 'blog/main.html')

    def test_post_detail_view(self):
        response = self.client.get('/blogs/aut/1')
        no_response = self.client.get('/post/100000')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, 'titulo')
        self.assertTemplateUsed(response, 'blog/blog_detail.html')
