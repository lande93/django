from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib import messages


# Create your views here.
def index(request):
    return HttpResponse('Welcome to my homepage')


def love(request):
    return render(request, 'mysite/love.html')


def signup(request):
    return render(request, 'mysite/signup.html')


def signout(request):
    if request.method == 'POST':
        username = request.POST['username']
        fname = request.POST['fname']
        email = request.POST['email']
        lname = request.POST['lname']

        myuser = User.objects.create_user(username,fname, email, lname)

        myuser.first_name = fname
        myuser.last_name = lname



        myuser.save()
        messages.success(request, 'Your account is  successful')

        return redirect('signup')


    return render(request, 'mysite/signout.html')
