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

class Bill(models.Model):
    Title =  models.CharField(max_length=30)
    type_choices = (
    ('CZYNSZ', 'Czynsz'),
    ('PRAD', 'Prąd'),
    ('ZRZUTKA','Zrzutka na sprzęt'),
    ('NET','Internet'),
    )
    Type = models.CharField(max_length=20, choices=type_choices)
    #Creator = models.ForeignKey('SiteUser', on_delete=models.CASCADE,
    #verbose_name='Twórca płatności')
    Founder = models.ForeignKey('SiteUser', on_delete=models.CASCADE,
    related_name='foudedBills')
    Obligors = models.ManyToManyField('SiteUser', related_name='billsToPay')
    #Payments = models.ManyToManyField('Payments', verbose_name="Platnosc")
    status_choices = (
    ('OPEN', 'Otwarty'),
    ('CLOSE', 'Zamknięty'),
    ('BLOCKED','Zawieszony'),
    )
    Status = models.CharField (max_length=20, choices=status_choices)
