from django.contrib.auth.models import User
from django.utils.text import slugify
from rest_framework import serializers

from blog.models import Post, Comment


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.SlugRelatedField(many=True, read_only=True, slug_field='slug')
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'posts', 'comments']


class PostSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')
    status = serializers.CharField(source='get_status_display', required=False)
    slug = serializers.SerializerMethodField()
    comments = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    def get_slug(self, instance):
        return slugify(instance.title)

    class Meta:
        model = Post
        fields = '__all__'
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = '__all__'
