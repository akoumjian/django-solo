from django.forms import ModelForm
from solo.models import Post


class PostForm(ModelForm):

    readonly_fields = ('modified', )

    class Meta:
        model = Post
