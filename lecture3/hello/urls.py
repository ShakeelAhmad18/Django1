from django.urls import path
from . import views

urlpatterns=[
    path("",views.index,name="index"),
    path("some",views.some,name="some"),
    path("<str:greet>",views.greet,name="greet")
]