from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse
# Create your models here.
class Post(models.Model):
    tittle = models.CharField(max_length=256)
    content = models.TextField()
    dated_posted = models.DateField(default=timezone.now())
    author = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.tittle


class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self,*args,**kwargs):
        super(Profile,self).save(*args,**kwargs)

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300,300)
            img.thumbnail(output_size)