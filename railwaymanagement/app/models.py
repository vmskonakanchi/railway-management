from django.db import models
from django.contrib.auth import get_user_model


_TRAIN_CHOICES = (
    ("STOPPED","STOPPED"),
    ("STARTED","STARTED"),
    ("RUNNING","RUNNING"),
    ("DELAYED" , "DELAYED")
)


class Train(models.Model):
    name = models.CharField(max_length=50)
    from_station = models.CharField(max_length=50)
    to_station = models.CharField(max_length= 50)
    status = models.CharField(choices=_TRAIN_CHOICES ,default=_TRAIN_CHOICES[1][0] , max_length=50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_seats = models.IntegerField(default=0)
    available_seats = models.IntegerField(default=0)
    price = models.IntegerField(default=0)
    booked_by = models.ManyToManyField(get_user_model())