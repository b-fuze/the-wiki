from . import views
from django.urls import path

urlpatterns = [
    path('rondom/', views.random_func, name='rondom'),
]
