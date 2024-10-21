from django.db import models

# Create your models here.
class Udata(models.Model):
    message = models.TextField(max_length=300)
    name = models.CharField(max_length=70)
    email = models.CharField(max_length=70)
    sub = models.CharField(max_length=90)

    def __str__(self):
        return self.name