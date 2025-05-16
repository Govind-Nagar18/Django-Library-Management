from django.db import models

class Books(models.Model):
    name = models.CharField(max_length=30, null=False)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    price = models.IntegerField()
    descriptions = models.TextField()
    booktype = models.CharField(max_length=10, null=False, blank=False)
