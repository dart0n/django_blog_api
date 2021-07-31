from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('hidden-admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include('blog.urls')),
]
