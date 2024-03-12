from django.shortcuts import render
import calendar
from  calendar import HTMLCalendar
from datetime import datetime

# Create your views here.
def home(request, year=None, month=None):
    if year is None:
        year = datetime.now().year
    if month is None:
        month = datetime.now().strftime('%B')
    month = month.title()
    #convert month name to number
    month_num=list(calendar.month_name).index(month)
    month_num=int(month_num)
    #creating a calender for you guyz don't you worry
    cal=HTMLCalendar().formatmonth(year,month_num)

    return render(request,'events/base.html',{
        'month':month,
        'year':year,
        'month_num':month_num,
        'cal':cal,
    })