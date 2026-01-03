from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ChaiVarity(models.Model):
    CHAI_TYPES_CHOICE = [
        ('ML','MASALA'),
        ('GR','GINGER'),
        ('KL','KIWI'),
        ('PL','PLAIN'),
        ('EL','ELACHI'),
    ]

    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='chais/')
    date_added = models.DateTimeField(default=timezone.now)
    type = models.CharField(max_length=2, choices=CHAI_TYPES_CHOICE)
    description = models.TextField(default='')

    def __str__(self):
        return self.name


class ChaiReview(models.Model):
    CHAI_RATING = [
        (1, "1 Star"),
        (2, "2 Star"),
        (3, "3 Star"),
        (4, "4 Star"),
        (5, "5 Star"),
    ]

    chai = models.ForeignKey(
        ChaiVarity,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=CHAI_RATING)
    comment = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.user.username} review for {self.chai.name}'


class Store(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    chai_varieties = models.ManyToManyField(ChaiVarity, related_name='stores')

    def __str__(self):
        return self.name


class ChaiCertificate(models.Model):
    chai = models.OneToOneField(
        ChaiVarity,
        on_delete=models.CASCADE,
        related_name='certificate'
    )
    certificate_number = models.CharField(max_length=100)
    issued_date = models.DateTimeField(default=timezone.now)
    valid_until = models.DateTimeField()

    def __str__(self):
        return f'Certificate for {self.chai.name}'
