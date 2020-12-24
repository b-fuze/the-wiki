from django.urls import  path
from . import views

app_name = "editpage"
urlpatterns = [
    path("", views.edit, name='edit'),
    path("save/", views.save, name='save'),
]
