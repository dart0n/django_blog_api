from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status

from blog.models import Post


user_data = {'username': 'testuser', 'password': '12345'}


class PostCreateAPIView(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(**user_data)
        self.client.force_authenticate(user=self.user)
        self.url = reverse('api_posts')

    def test_create_post(self):
        self.assertEquals(Post.objects.count(), 0)
        data = {
            'title': 'title',
            'content': 'content'
        }
        response = self.client.post(self.url, data=data, format='json')
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(Post.objects.count(), 1)
        post = Post.objects.first()
        self.assertEquals(post.title, data['title'])
        self.assertEquals(post.content, data['content'])


class PostDetailAPIViewTest(APITestCase):
    def setUp(self) -> None:
        self.user = User.objects.create_user(**user_data)
        self.post = Post.objects.create(
            title='test title', content='test content', author=self.user
        )
        self.url = reverse('api_post_detail', kwargs={'slug': self.post.slug})

    def test_get_post_details(self):
        response = self.client.get(self.url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        data = response.json()
        self.assertEquals(data['id'], self.post.id)
        self.assertEquals(data['title'], self.post.title)
        self.assertEquals(data['content'], self.post.content)
