from django.shortcuts import render
from club.models import Registration 
from django.http import HttpResponse

# Create your views here.

def login(request):
    return render(request, 'club/login.html')


def registration(request):
    return render(request, 'club/registration.html')



def home(request):
    return render(request, 'club/home.html')


def store(request):
  if request.method == 'POST':
      name = request.POST['name']
      university_mail= request.POST['university_mail']
      department = request.POST['department']
      student_id = request.POST['student_id']
      password = request.POST['password']
      division = request.POST['division']
      district = request.POST['district']
      post_code = request.POST['post_code']
      phone_number = request.POST['phone_number']
      n_card = request.POST['nid_card']

      userInfo = Registration(name=name,university_email=university_mail,
                              department=department,student_id=student_id,
                              password=password,division=division,district=district,post_code=post_code,phone_number=phone_number,
                              n_id_card=n_card) 
      userInfo.save()  
      return HttpResponse('<h1>Data Store</h1>') 