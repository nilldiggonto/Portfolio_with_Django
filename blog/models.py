from django.db import models

# Create your models here.
class Blog(models.Model):
    title           = models.CharField(max_length=200)
    publish_date    = models.DateTimeField()
    body            = models.TextField()
    image           = models.ImageField(upload_to='blog/')

    def __str__(self):
        return self.title
    
    def data_polish(self):
        return self.publish_date.strftime('%b-%e-%Y')