from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Group(models.Model):
    """Класс модели группы."""
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=40, unique=True)
    description = models.TextField(null=True)

    def __str__(self) -> str:
        return f'{self.title}'


class Post(models.Model):
    """Класс модели поста."""
    text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='posts'
    )
    group = models.ForeignKey(
        Group,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='posts'
    )


# Create your models here.
