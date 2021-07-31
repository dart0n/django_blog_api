from django.contrib.auth.models import User
from django.test import TestCase

from blog.models import Post


class PostTestCase(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='12345')

    def test_post(self):
        self.assertEquals(Post.objects.count(), 0)

        Post.objects.create(title='test post', content='test content', author=self.user)

        self.assertEquals(Post.objects.count(), 1)
