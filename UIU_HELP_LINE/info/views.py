from django.shortcuts import render

# Create your views here.


def faq(request):
    return render(request,'info/faq.html')


def chat(request):
    return render(request,'info/chat.html')