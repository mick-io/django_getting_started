from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404
# from django.forms import modelform_factory

from .models import Meeting, Room
from .forms import MeetingForm


def detail(request: HttpRequest, id) -> HttpResponse:
    meeting = get_object_or_404(Meeting, pk=id)
    ctx = {"meeting": meeting}
    return render(request, "meetings/detail.html", ctx)


def rooms_list(request: HttpRequest) -> HttpResponse:
    ctx = {"rooms": Room.objects.all()}
    return render(request, "meetings/rooms_list.html", ctx)


# MeetingForm = modelform_factory(Meeting, exclude=[])


def new(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = MeetingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = MeetingForm()
    return render(request, "meetings/new.html", {"form": form})
