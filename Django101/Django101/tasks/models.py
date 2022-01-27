from django.db import models

class Task(models.Model):
    title = models.CharField(
        max_length=30
    )
    text = models.CharField(
        max_length=50
    )