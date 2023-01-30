import random

from django.shortcuts import render, redirect, HttpResponseRedirect
from core.form import SignUpForm
from django.http import HttpResponse, Http404
from django.core.mail import EmailMessage
import booktrade.settings as site_settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from core.models import SignUp, BTUser
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
#from core.utils import crypto_utils

def signup(request):
    eror = False
    submitted = False
    if request.method == 'POST':
        signup_form = SignUpForm(request.POST)
        if signup_form.is_valid():
            if request.POST['password'] == request.POST['confirmPassword']:
                signup = signup_form.save()
                otp = random.randint(100000, 999999)
                signup.otp = otp
                signup.save()
                html_content = render_to_string('emails/signup.html',context={'signup':signup})
                msg = EmailMessage(subject='Sign Up Confirmation on BookTrade',
                                   body=html_content,
                                   from_email=site_settings.DEFAULT_FROM_EMAIL,
                                   to=[signup.email],
                                   bcc=[site_settings.ADMIN_EMAIL], )
                msg.content_subtype = "html"
                msg.send(fail_silently=False)
                submitted = True
                return redirect('/user/signup_confirm/'+str(signup.id))
            else:
                messages.add_message(request, messages.ERROR,'Password and confirm password do not match')
        else:
            eror = True
            #return HttpResponse('One of your details were wrong. Please try again')
    meta = {
        'title': 'Sign Up | HelloPage'
    }
    context = {'meta': meta, 'submitted': submitted, 'eror': eror}
    return render(request, 'signup.html', context)

def signup_confirm(request, id):
    submitted = False
    signup = SignUp.objects.get(id=id)
    # check if signup is expired
    if request.method == 'POST':
        otp = int(request.POST['otp'])
        if otp == signup.otp:
            user = User.objects.create_user(
                username=signup.email,
                email=signup.email,
                password=signup.password
            )
            bt_user = BTUser.objects.create(
                email=signup.email,
                name=signup.name,
                user=user,
            )
            return redirect('/user/login')
        else:
            return HttpResponse('Wrong Code')
            # Throw Error
    meta = {'title': 'Confirm Sign Up | HelloPage'}
    context = {'meta': meta}
    return render(request, 'confirm.html', context)

def user_login(request):
    error = False
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            error = True
    meta = {
        'title': 'Login | HelloPage'
    }
    if request.user.is_authenticated:
        usr = BTUser.objects.get(user=request.user)
    context = {'meta': meta, 'error':error}
    return render(request, 'login.html', context)

def user_logout(request):
    logedout = False
    if request.user.is_authenticated:
        logout(request)
        logedout = True
    return redirect('/user/login')