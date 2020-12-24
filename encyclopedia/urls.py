from django.urls import path

from . import views



urlpatterns = [
    path("", views.index, name="index"),
]

# for topic in topics:
#     urlpatterns.append(path(<str:name>topic+'/',views.topic, name = topic))
