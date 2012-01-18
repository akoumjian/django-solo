from django.contrib import admin
from solo.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified')

admin.site.register(Post, PostAdmin)
