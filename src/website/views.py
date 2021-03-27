from datetime import datetime

from django.shortcuts import render
from django.http import HttpResponse

from meetings.models import Meeting


def welcome(request):
    ctx = {"meetings": Meeting.objects.all()}
    return render(request, "website/welcome.html", ctx)


def date(request):
    return HttpResponse("This page was served at " + str(datetime.now()))


def about(request):
    return HttpResponse("I'm Mick, I'm a programmer.")
