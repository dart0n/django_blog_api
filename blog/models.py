from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify


class Post(models.Model):
    STATUS = (
        (0, 'Draft'),
        (1, 'Published'),
    )

    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    status = models.IntegerField(choices=STATUS, default=0)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self) -> str:
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title, allow_unicode=True)

        return super(Post, self).save(*args, **kwargs)


class Comment(models.Model):
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']

    def __str__(self) -> str:
        return self.text
