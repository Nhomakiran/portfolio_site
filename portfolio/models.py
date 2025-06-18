from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length = 100)
    description = models.TextField()
    technologies = models.CharField(max_length = 255)
    duration = models.CharField(max_length=100)
    result = models.TextField(blank=True)
    image = models.ImageField(upload_to='projects/', blank=True)
    link = models.URLField(blank=True)

    def __str__(self):
        return self.title
