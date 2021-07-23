from django.shortcuts import render
from .models import *
from .forms import *
# Create your views here.

def index(request):
    if request.method == "POST":
        form = new_member(request.POST or None)
        if form.is_valid():
            form.save()
            return render(request, "smp/index.html", {
                "members": Member.objects.all(),
                "form": form,
                "requestsent": True
            })
    else:
        form = new_member()
        return render(request, "smp/index.html", {
            "members": Member.objects.all(),
            "form": form
        })