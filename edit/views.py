from django.shortcuts import render
from encyclopedia import util
import markdown2


def edit(request):
    topic_name = request.GET.get('topic_name')
    body = util.get_entry(topic_name)
    return render(request, 'edit/edit.html',{
        'topic_title': topic_name,
        'body': body
    })

def save(request):
    if request.method == "POST":
        title = request.POST.get('title')
        body = request.POST.get('textarea')
        txt = ""
        c  = 0
        for i in body.split('\n'):
            if i == '\r' and body.split('\r')[c + 1] == '\n':
                continue
            txt += i
            c += 1
        util.save_entry(title, txt)
        body = markdown2.markdown(util.get_entry(title))
        return render(request, 'encyclopedia/topic.html',{
            'body': body,
            'topic_name':title
        })
