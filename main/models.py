from django.db import models

class quotes(models.Model):
    text = models.TextField(max_length=200, unique=True,)

    def __str__(self):
        return self.text
