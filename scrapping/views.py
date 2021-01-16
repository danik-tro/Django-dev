from django.shortcuts import render
import datetime


# Create your views here.
def home(request):
    context = {
        'name_theme': "Work",
        'date_theme': datetime.datetime.now()
    }

    return render(request,
                  'home.html',
                  context)