from django.shortcuts import render
import markdown2
from encyclopedia import util
import os
from django.http import HttpResponse

topics = util.list_entries()


def wiki(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })




def topic(request, name):
    dict_topic = {}

    for top in topics:
        html_page = markdown2.markdown(util.get_entry(top))
        dict_topic[top] = str(html_page)

    if name in topics:
        return render(request,"encyclopedia/topic.html",{
            'topic_name': name,
            'body':dict_topic[name]
        })
    return HttpResponse('<h1 style="font-size:40px">Page not found</h1><br>Sorry, requested page was not found.')
