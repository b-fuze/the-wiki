from django.shortcuts import render
from encyclopedia import util
import markdown2

topics = util.list_entries()
topics_upper = list(map(str.upper, topics))# Create your views here.
dict_topic = {}

for (a, b) in zip(topics_upper, topics):
    dict_topic[a] = b

def create(request):
    return render(request, 'create/create.html')

def save(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('textarea')

        if title.upper() in topics_upper:
            return render(request, 'create/exist.html',{
                'topic':dict_topic[title.upper()]
            })

        util.save_entry(title, body)
        body = markdown2.markdown(util.get_entry(title))
        return render(request, 'encyclopedia/topic.html',{
            'body': body,
            'topic_name':title
        })
