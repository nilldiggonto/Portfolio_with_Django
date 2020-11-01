from django.db import models

# Create your models here.
class Skill(models.Model):
    images  = models.ImageField(upload_to='skill/')
    summary = models.CharField(max_length=200)
    score   = models.IntegerField(default=10)

    def __str__(self):
        return self.summary

