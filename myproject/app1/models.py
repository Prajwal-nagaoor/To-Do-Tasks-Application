from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class tasklist(models.Model):
    title = models.CharField(max_length=50)
    desc = models.TextField()
    is_del=models.BooleanField(default=0)
    completed = models.BooleanField(default=0)
    host = models.ForeignKey(User,on_delete=models.CASCADE)
