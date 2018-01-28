from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # department = models.CharField(max_length=100)

    def __str__(self):
        return self.user.username


class Post(models.Model):
    author = models.ForeignKey('SiteUser', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.title