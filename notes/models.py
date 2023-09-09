from django.db import models


# Create your models here.
class Notes(models.Model):
    title = models.CharField(max_length=225)
    body = models.CharField(max_length=225)

    def __str__(self):
        return self.title
