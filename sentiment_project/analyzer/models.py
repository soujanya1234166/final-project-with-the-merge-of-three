from urllib import request
from django.db import models
from django.contrib.auth.models import User

class SentimentHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    sentiment = models.CharField(max_length=10)
    polarity = models.FloatField()
    subjectivity = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    