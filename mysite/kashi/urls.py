from django.urls import path
from django.urls.resolvers import URLPattern
from .import views
app_name="kashi"

urlpatterns =[

    path("", views.kash_list,name="kash_list"),
    path("<int:id>/",views.kash_detail ,name="detail")
]

