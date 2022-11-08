from django.db import models
from django.contrib.auth import get_user_model



class Train(models.Model):
    name = models.CharField(max_length=50)
    from_station = models.CharField(max_length=50)
    to_station = models.CharField(max_length= 50)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    total_seats = models.IntegerField(default=0)
    available_seats = models.IntegerField(default=0)
    price = models.IntegerField(default=0)


class Booking(models.Model):
    user = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    train = models.ForeignKey(Train,on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    status = models.PositiveBigIntegerField(default=0)

