from django.db import models

# Create your models here.
class Safe(models.Model):
    username = models.CharField(max_length=64)
    website = models.CharField(max_length=64)
    userInfo = models.CharField(max_length=64)
    password = models.CharField(max_length=64)
    dateTime = models.DateField()

    def __str__(self):
        return print(f"username={self.username},website={self.website},userInfo={self.userInfo},password={self.password},datetime={self.datetime}")
