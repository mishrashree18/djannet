from django.urls import path, include

from . import views


app_name = 'djannet_app'
urlpatterns = [
    path('home', views.home_page, name='home'),
]
