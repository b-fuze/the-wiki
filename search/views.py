from django.shortcuts import render
from encyclopedia import util
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
import re

topics = util.list_entries()
topics_upper = list(map(str.upper, topics))
dict_value = {}
for (a, b) in zip(topics_upper, topics):
    dict_value[a] = b

def search(request):
    search_title = request.GET.get('q')
    if search_title.upper() in topics_upper:
        return HttpResponseRedirect(reverse("topic", args=[dict_value[search_title.upper()]]))

    researh_list = []
    for t in topics_upper:
        for letter in search_title:
            if letter.upper() in t:
                researh_list.append(dict_value[t])

    if researh_list:
        return render(request,'search/search.html',{
            'header':'Search Results',
            'Result':set(researh_list)
        })

    return render(request,'search/search.html',{
                'header':'Your search topic is not found',
                'masge':"This is the list of all topic we have",
                'Result':topics
            })
