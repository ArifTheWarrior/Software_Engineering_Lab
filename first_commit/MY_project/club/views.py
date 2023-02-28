from django.shortcuts import render

# Create your views here.


def home(request,fs,stringvar):
    print(fs)
    print(stringvar)
    return render(request,'home.html')

def sports_club(request,a):
    return render(request,'sports_club.html')


def App_forum(request,fs):
    return render(request,'app_forum.html')