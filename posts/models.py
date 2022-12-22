from django.db import models


# Create your models here.

class Tweet(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.author} - {self.title}'


class Comment(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title} - {self.text} - {self.date}'


class Mark(models.Model):
    mark_value = models.IntegerField()
    tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name='tweets')

