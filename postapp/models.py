from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

# Create your models here.
#python manage.py makemigrations
#python manage.py migrate