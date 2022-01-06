from django.db import models

from django.utils.translation import gettext as _

class Reservation(models.Model):
    name = models.CharField( max_length=200)
    email = models.EmailField( max_length=250)
    mobile = models.CharField( max_length=15)
    number = models.IntegerField()
    date = models.DateField(auto_now=False, auto_now_add=False)
    time = models.TimeField( auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.email


