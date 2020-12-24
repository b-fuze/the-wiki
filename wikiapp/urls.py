from django.urls import path

from . import views

from encyclopedia import util

topics = util.list_entries()

urlpatterns = [
    path("", views.wiki, name="wiki"),
    path("<str:name>/",views.topic, name = "topic")
]

# for topic in topics:
#     urlpatterns.append(path(<str:name>topic+'/',views.topic, name = topic))
