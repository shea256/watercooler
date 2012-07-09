from django.db import models
from django.contrib.auth.models import User

class Interest(models.Model):
    text = models.CharField(max_length=200)

# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(User, unique=True)
    interests = models.ManyToManyField(Interest)
    
    def __unicode__(self):
        return self.user.username
