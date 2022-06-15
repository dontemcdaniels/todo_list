from django.db import models


class ToDoListItem(models.Model):
    content = models.TextField()

# Create your models here.
