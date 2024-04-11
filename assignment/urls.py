from django.urls import path
from assignment import views

urlpatterns = [
    path('v1/assigment', views.assigment)
]
