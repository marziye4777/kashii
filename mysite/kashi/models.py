from django.db import models
from django.utils.translation import gettext as _

class Kash(models.Model):
    name = models.CharField(_("نام"),max_length=100)
    discription=models.CharField(_("نوضیحات"),max_length=50)
    price=models.IntegerField(_("قیمت"),)
    time_pup=models.DateField(_("تاریخ انتشار"),auto_now=False,auto_now_add=True)
    photo=models.ImageField(upload_to='kashi/')


    def __str__(self):
        return self.price
  