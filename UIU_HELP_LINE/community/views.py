from django.shortcuts import render

# Create your views here.


def cisco(request):
    return render(request,'community/cisco.html')


def community(request):
    return render(request,'community/community.html')