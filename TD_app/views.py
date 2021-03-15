from django.shortcuts import render
from time import gmtime, strftime
import datetime

def display_time(request):
    context = {
        "date": strftime("%m-%d-%Y", gmtime()),
        "time": strftime("%I:%M %p", gmtime()),
    }
    return render(request,'display_time.html', context)

def time_display(request):
    context = {
        "date_time": datetime.datetime.now(),
    }
    return render(request,'time_display.html', context)
