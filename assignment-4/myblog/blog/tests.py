from django.test import TestCase

from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Post, Comment

class BlogAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client.login(username='testuser', password='password')
        self.post = Post.objects.create(title='Test Post', content='Test Content', author=self.user)

    def test_create_post(self):
        data = {'title': 'New Post', 'content': 'Some content'}
        response = self.client.post('/api/posts/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_list_posts(self):
        response = self.client.get('/api/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_comment(self):
        data = {'content': 'Nice post!', 'post': self.post.id}
        response = self.client.post('/api/comments/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

