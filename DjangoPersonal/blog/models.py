from django.db import models

class Post(models.Model):
    STATUS_CHOICES = (
        (0, 'Rascunho'),
        (1, 'Publicado'),
    )

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS_CHOICES, default=0)

    def __str__(self):
        return self.title