from django.shortcuts import render
import random
from encyclopedia import util
import markdown2

# Create your views here.
topics = util.list_entries()

def random_func(request):
    random_num = random.randint(0,len(topics) - 1)
    html_page = markdown2.markdown(util.get_entry(topics[random_num]))
    return render(request,"encyclopedia/topic.html",{
        'topic_name': topics[random_num],
        'body': html_page
    })
