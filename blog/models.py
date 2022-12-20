from django.db import models
from django.conf import settings

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericRelation


class Tag(models.Model):
    """Tag model"""

    value = models.CharField(max_length=100)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = "Tag"
        verbose_name_plural = "Tags"


class Comment(models.Model):
    """Comment model."""

    creator = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")


class Post(models.Model):
    """Post model"""

    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    published_at = models.DateTimeField(blank=True, null=True)
    title = models.TextField(max_length=100)
    slug = models.SlugField()
    summary = models.TextField(max_length=500)
    content = models.TextField()

    comments = GenericRelation(Comment)

    tags = models.ManyToManyField(Tag, related_name="posts")

    def __str__(self):
        return self.title
