from django.db import models
from autoslug import AutoSlugField
from django.db.models.signals import pre_save
from django.dispatch import receiver
import datetime


class Post(models.Model):
    """
    An article or page.
    """
    pubdate = models.DateTimeField(blank=True)  # For ordering
    modified = models.DateTimeField(blank=True, editable=False)  # Last edit
    public = models.BooleanField(default=False)  # Display true/false
    title = models.CharField(max_length=100, blank=True)  # auto-populated from post
    body_markdown = models.TextField(blank=True)
    body_html = models.TextField(blank=True)
    slug = AutoSlugField(populate_from='title', unique=True)

    def set_timestamps(self):
        """
        Because auto_now and auto_now_add don't play nice with admin
        """
        if not (self.id or self.pubdate):
            print "setting pubdate"
            self.pubdate = datetime.datetime.today()
        self.modified = datetime.datetime.now()

    class Meta:
        ordering = ('-pubdate', )


@receiver(pre_save, sender=Post)
def auto_fields(sender, instance, **kwargs):
    instance.set_timestamps()
