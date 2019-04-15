from django.shortcuts import render
from polls.forms import PollsForm
from polls.models import Polls

def polls_create(request):
    form = PollsForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request,"polls/pollscreate.html", context)


def index(request):
    return render(request=request, template_name="polls/index.html")
