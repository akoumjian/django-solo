from django.db import models
from markdown import markdown
from autoslug import AutoSlugField
import datetime


class Post(models.Model):
    """
    An article or page.
    """
    pubdate = models.DateTimeField(blank=True)
    modified = models.DateTimeField(blank=True)
    public = models.BooleanField(default=False)
    title = models.CharField(max_length=100)
    tagline = models.CharField(max_length=100)
    body = models.TextField()
    body_html = models.TextField(editable=False, blank=True, null=True)
    slug = AutoSlugField(populate_from='title', unique=True,
                         always_update=True)

    def save(self):
        """
        Render markdown and save datetime fields.
        """
        self.body_html = markdown(self.body, ['codehilite'])
        if not self.id:
            self.pubdate = datetime.datetime.today()
        self.modified = datetime.datetime.today()
        super(Post, self).save()

    class Meta:
        ordering = ('-pubdate', )
