from django.db import models

# Create your models here.


class Local(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100, default='street address')
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=2)
    zipCode = models.CharField(max_length=5)
    photo_url = models.TextField()
    description = models.CharField(max_length=280)
    website = models.CharField(max_length=100, default='N/A')
    resturaunt = models.BooleanField(null=True)
    shopping = models.BooleanField(null=True)
    social = models.BooleanField(null=True)

    def __str__(self):
        return self.name


