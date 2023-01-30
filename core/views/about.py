from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
from django.core.mail import EmailMessage
import booktrade.settings as site_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from core.models import BTUser, Inventory
#from core.form import ContactForm
from django.contrib.auth.models import User
#from django.contrib.gis.geoip2 import GeoIP2




def get_ip_address(request):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def home(request):
    if request.user.is_authenticated:
        usr=BTUser.objects.get(user=request.user)
    user_ip = get_ip_address(request)
    query2 = Inventory.objects.all()
#    g = GeoIP2() 
#   lat,lng = g.lat_lon(user_ip)
    meta = {'title': 'something here bro'}
    context = {'meta': meta, 'user_ip':user_ip, 'usr':usr, 'query2':query2}
    return render(request, 'home.html', context)

    # create temp = []. use for loop to Keep appending values such that books and user model come from each object of 
    # the inventory to be extracted and put into this array. Send this array to the frontend and print using a for loop. 
    