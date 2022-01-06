from django.shortcuts import render
from .models import Reservation


def reserve (request):

    context= {}


    return render(request, 'reservation/reservation.html',context)
