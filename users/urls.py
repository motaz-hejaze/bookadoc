from django.urls import path
from . import views

urlpatterns = [
    path('hello/' , views.HomeView.as_view() , name='home'),
]