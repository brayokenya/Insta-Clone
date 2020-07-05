from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from .models import Update, Location, Category
from django.contrib.auth.decorators import login_required


# Create your views here.


# Create your views here.
def welcome(request):
    return render(request, 'index.html')
    
@login_required(login_url='/accounts/login/')
def posts_of_day(request):
    date = dt.date.today()
    insta = Update.todays_insta()
    locations = Location.objects.all()
    return render(request, 'insta-post/posts_today.html', {"date": date, "insta": insta, "locations": locations})


def location(request,location):
    locations = Location.objects.all()
    selected_location = Location.objects.get(id = location)
    insta = Update.objects.filter(location = selected_location.id)
    return render(request, 'insta-post/location.html', {"location":selected_location,"locations":locations,"insta":insta})    


def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

