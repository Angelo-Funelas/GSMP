from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def index(request):
    requestsent = ""
    form = new_member(request.POST or None)
    if form.is_valid():
        form.save()
        requestsent = True
    return render(request, "smp/index.html", {
        "members": Member.objects.filter(Approved=True),
        "form": form,
        "requestsent": requestsent
    })
    