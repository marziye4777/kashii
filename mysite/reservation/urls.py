from django.urls import path
from django.urls.resolvers import URLPattern
from . import views
app_name="reservation"
urlpatterns=[

    path('', views.reserve,name="reservation")
]