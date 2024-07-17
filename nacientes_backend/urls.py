from django.urls import path
from . import views

urlpatterns = [
    path("nacientes/", views.NacienteLista.as_view(), name=views.NacienteLista.name)
]