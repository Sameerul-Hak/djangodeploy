from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=1000)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Comments(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ManyToManyField(Post)
    created_at=models.DateTimeField(auto_now=True)
    message=models.CharField(max_length=100,null=True,blank=True,default=None)
    updated_at=models.DateTimeField(auto_now_add=True)
class Like(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Post, on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.post