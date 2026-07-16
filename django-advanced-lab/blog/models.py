from django.db import models
from django.conf import settings


class Post(models.Model):

    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="posts"
    )

    image = models.ImageField(
        upload_to="posts/images/",
        null=True,
        blank=True
    )

    title = models.CharField(max_length=255)

    content = models.TextField()

    status = models.BooleanField(default=False)


    category = models.ForeignKey(
    'Category',
    on_delete=models.SET_NULL,
    related_name='posts',
    null=True,
    blank=True
    )

    created_date = models.DateTimeField(auto_now_add=True)

    updated_date = models.DateTimeField(auto_now=True)

    published_date = models.DateTimeField(
        null=True,
        blank=True
    )




class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name