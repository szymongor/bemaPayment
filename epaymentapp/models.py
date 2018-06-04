from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class SiteUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

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

class subPost(models.Model):
    post = models.ForeignKey('Post', related_name='subposts', on_delete=models.CASCADE,)
    author = models.ForeignKey('SiteUser', on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)

    def __str__(self):
        return self.text

class Bill(models.Model):
    type_choices = (
        ('CZYNSZ', 'Czynsz'),
        ('PRAD', 'Prąd'),
        ('ZRZUTKA', 'Zrzutka na sprzęt'),
        ('NET', 'Internet'),
    )

    status_choices = (
        ('OPEN', 'Otwarty'),
        ('CLOSE', 'Zamknięty'),
        ('BLOCKED', 'Zawieszony'),
    )

    title =  models.CharField(max_length=30, unique=True)
    type = models.CharField(max_length=20, choices=type_choices)
    amount = models.PositiveIntegerField(default=0)
    founder = models.ForeignKey('SiteUser', on_delete=models.CASCADE,
    related_name='fouded_bills')
    obligors = models.ManyToManyField('SiteUser', related_name='bills_to_pay')
    status = models.CharField (max_length=20, choices=status_choices)


    def __str__(self):
        return self.title

class Payment(models.Model):
    amount = models.PositiveIntegerField()
    bill = models.ForeignKey('Bill', related_name='payments', on_delete=models.CASCADE,)
    founder = models.ForeignKey('SiteUser', on_delete=models.CASCADE,
                                related_name='payments')
    created_date = models.DateTimeField(
        default=timezone.now)

    def __str__(self):
        return self.founder.__str__() + ":" + str(self.amount)
