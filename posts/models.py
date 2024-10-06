from datetime import timezone, datetime

from account.models import User

from django.db import models


# Create your models here.

class PostCategory(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    category = models.ForeignKey(PostCategory, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.FileField(upload_to='posts/')
    date_posted = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_post(self):
        return self.save()


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    date_commented = models.DateTimeField(default=datetime.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)



