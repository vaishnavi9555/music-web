from django.db import models
from django.contrib.auth.models import User

class Audio(models.Model):
    file=models.FileField(upload_to='audio/')
    user=models.ForeignKey(User , on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='thumbnail/',blank=True,null=True)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.file.url

