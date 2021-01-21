from django.shortcuts import render
import datetime
from .models import Vacancy


def home_view(request):
    qs = Vacancy.objects.all()

    return render(request,
                  'home.html', {
                      'object_list': qs,
                  })


def home(request):
    context = {
        'name_theme': "Work",
        'date_theme': datetime.datetime.now()
    }

    return render(request,
                  'home.html',
                  context)
