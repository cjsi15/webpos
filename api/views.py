from django.shortcuts import render
from . import views

urlpatterns = [

    path('', views.apiOverview, name="api-overview"),
]
