from django.shortcuts import render

from .models import Kash

def kash_list(request):
    kash_list=Kash.objects.all()
    context= {
        "kashi": kash_list
    }
    return render(request,"kashi/list.html",context)

def kash_detail (request,id):
    kash = Kash.objects.get(id = id)
    context = {
        "kash":kash

    }
    return render(request,"kashi/detail.html",context)