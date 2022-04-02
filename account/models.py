from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Person(models.Model):
    MALE = 'ML'
    FEMALE = 'FM'
    OTHER = 'OT'
    SEX_CHOICES = (
        (MALE, 'MALE'),
        (FEMALE, 'FEMALE'),
        (OTHER, 'OTHER')
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(
        default=21,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(1)
        ]
    )
    sex = models.CharField(max_length=2, choices=SEX_CHOICES, default=MALE)
    job = models.CharField(max_length=20, blank=True)
    about = models.TextField(blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
