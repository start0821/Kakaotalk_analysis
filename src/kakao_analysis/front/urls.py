from django.urls import path,include
from . import views

urlpatterns = [
    path("1",views.analysis1,name="analysis1"),
]
