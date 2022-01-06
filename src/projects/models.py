from django.db import models

# Create your models here.
class Project(models.Model):
    user_id = models.CharField(max_length=150);
    title = models.CharField(max_length=120);
    description = models.CharField(max_length=400);