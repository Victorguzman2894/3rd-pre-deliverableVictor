from django.urls import path
from . import views


"""The most important part of this code is urlpatterns tuple. This tuple is where the views and URLs are connected or mapped. As you can see, we've imported our views.py file so we can use it within the urlpatterns line"""
urlpatterns = [
    path('', views.index, name='index'), 
]