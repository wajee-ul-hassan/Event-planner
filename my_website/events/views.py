from django.shortcuts import render
import calendar
from  calendar import HTMLCalendar
from datetime import datetime
from .models import *

# Create your views here.
def home(request):
    name="view the events here ..."
    event_list=Event.objects.all()
    return render(request,'events/base.html',{
        'name':name,
        'event_list':event_list
    })