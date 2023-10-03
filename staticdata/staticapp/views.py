from django.shortcuts import render
from . models import Place
from . models import Mentors


# Create your views here.


def start(request):
    obj = Place.objects.all()
    obj2 = Mentors.objects.all()
    return render(request, 'index.html', {'value':obj, 'result': obj2})