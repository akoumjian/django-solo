from django.db import models
from django.contrib import admin
from solo.models import Post
from markitup.widgets import AdminMarkItUpWidget


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'modified')
    # formfield_overrides = {models.TextField: {'widget': AdminMarkItUpWidget}}

    def formfield_for_dbfield(self, db_field, **kwargs):
        if db_field.name == 'body':
            kwargs['widget'] = AdminMarkItUpWidget(auto_preview=True)
        return super(PostAdmin, self).formfield_for_dbfield(db_field, **kwargs)

admin.site.register(Post, PostAdmin)
