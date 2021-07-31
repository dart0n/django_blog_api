from django.contrib import admin

from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status', 'created_date')
    list_filter = ('status',)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Post, PostAdmin)