from django.db import models

# Create your models here.

class BlogDb(models.Model):
    title=models.CharField(max_length=100)
    date=models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title