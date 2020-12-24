from django.shortcuts import render
import markdown2
from . import util
import os
from django.http import HttpResponse

topics = util.list_entries()


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })
