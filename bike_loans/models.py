from django.db import models
from django.contrib.auth.models import AbstractBaseUser


class Bike(models.Model):
    STATUS_AVAILABLE = 'AVA'
    STATUS_BROKEN = 'BRK'
    STATUS_IN_USE = 'USE'
    STATUS_UNAVAILABLE = 'UNA'  # if the bike is in reparation

    BIKE_STATUS = (
        (STATUS_AVAILABLE, 'Available'), (STATUS_BROKEN, 'Broken'),
        (STATUS_IN_USE, 'In use'), (STATUS_UNAVAILABLE, 'Unavailable'))

    status = models.CharField(
        max_length=3, choices=BIKE_STATUS, default=STATUS_UNAVAILABLE)


class User(AbstractBaseUser):
    rfid = models.CharField(max_length=20)


class Loan(models.Model):
    STATUS_FINISHED = 'FIN'
    STATUS_IN_PROGRESS = 'IPG'

    LOAN_STATUS = (
        (STATUS_FINISHED, 'Finished'), (STATUS_IN_PROGRESS, 'In progress'))

    bike = models.ForeignKey(Bike)
    user = models.ForeignKey(User)
    status = models.CharField(
        max_length=3, choices=LOAN_STATUS, default=STATUS_IN_PROGRESS)
    duration = models.DurationField()
    data_time = models.DateTimeField()
