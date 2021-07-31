from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

import blog.views as views


urlpatterns = [
    path('users/', views.UserList.as_view(), name='api_users'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='api_user_detail'),

    path('posts/', views.PostList.as_view(), name='api_posts'),
    path('posts/<slug:slug>/', views.PostDetail.as_view(), name='api_post_detail'),

    path('comments/', views.CommentList.as_view(), name='api_comments'),
    path('comments/<int:pk>/', views.CommentDetail.as_view(), name='api_comment_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
