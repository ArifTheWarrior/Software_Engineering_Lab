from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse

from club.models import User as StudentInfo


# Create your views here.


# data = [
#   {
#     "userId": 1,
#     "id": 1,
#     "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
#     "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
#   },
#   {
#     "userId": 1,
#     "id": 2,
#     "title": "qui est esse",
#     "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"
#   },
#   {
#     "userId": 1,
#     "id": 3,
#     "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut",
#     "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et velit aut"
#   },
#   {
#     "userId": 1,
#     "id": 4,
#     "title": "eum et est occaecati",
#     "body": "ullam et saepe reiciendis voluptatem adipisci\nsit amet autem assumenda provident rerum culpa\nquis hic commodi nesciunt rem tenetur doloremque ipsam iure\nquis sunt voluptatem rerum illo velit"
#   },
#   {
#     "userId": 1,
#     "id": 5,
#     "title": "nesciunt quas odio",
#     "body": "repudiandae veniam quaerat sunt sed\nalias aut fugiat sit autem sed est\nvoluptatem omnis possimus esse voluptatibus quis\nest aut tenetur dolor neque"
#   },
#   {
#     "userId": 1,
#     "id": 6,
#     "title": "dolorem eum magni eos aperiam quia",
#     "body": "ut aspernatur corporis harum nihil quis provident sequi\nmollitia nobis aliquid molestiae\nperspiciatis et ea nemo ab reprehenderit accusantium quas\nvoluptate dolores velit et doloremque molestiae"
#   }
# ]

def home(request,fs,stringvar):
    print(fs)
    print(stringvar)
    return render(request,'home.html')

def sports_club(request):
    name=request.GET.get('name')
    # print(name)
    id=request.GET.get('id')
    print(id)
    # return render(request,'sports_club.html', {'name':name, 'id':id})
    return HttpResponse("Dynamic URLs")
    # return JsonResponse({'name':name, 'id':id})
    # newdata = data[1]['title']
    # print(newdata)
    # dataval=[{'title':item['title'],'body':item['body'],'id':item['id']} for item in data ]
    # # return HttpResponse('<h1>Send Data </h1>')
    # return JsonResponse(dataval, safe=False)




def App_forum(request):

    # insert data to the database
    
    # studentInfo = StudentInfo(name="arif",email="albertarif@gmail.com",contact="01521755418",password="xyz",user_type="student",school_division="Dhaka",status=122,cgpa="4.00",official_id="011191031",designation="Student",subscription=1222,created_id="2022-12-27 08:26:49.219717")
    # # return render(request,'app_forum.html')
    # studentInfo.save()
    # return HttpResponse('<p> save data</p>')

    # read data from the database and show the front-end 

    studentInfo = StudentInfo.objects.all().filter(id=8).values()
    return render(request,'app_forum.html',{'name':studentInfo[0]['name'],
                                            'email':studentInfo[0]['email'],
                                            'contact':studentInfo[0]['contact'],
                                            'password':studentInfo[0]['password'],
                                            'user_type':studentInfo[0]['user_type'],
                                            'school_division':studentInfo[0]['school_division'],
                                            'status':studentInfo[0]['status'],
                                            'cgpa':studentInfo[0]['cgpa'],
                                            'official_id':studentInfo[0]['official_id'],
                                            'designation':studentInfo[0]['designation'],
                                            'subscription':studentInfo[0]['subscription'],
                                            'created_id':studentInfo[0]['created_id'],
                                        
                                            })

    



def userLogin(request):
#get data form the login page and save data to the sqlit db 
    if request.method == 'POST':
        
        id = request.POST.get('id')
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact = request.POST.get('contact')
        password = request.POST.get('password')
        user_type = request.POST.get('user_type')
        school_division = request.POST.get('school_division')
        status = request.POST.get('status')
        cgpa = request.POST.get('cgpa')
        official_id = request.POST.get('official_id')
        designation = request.POST.get('designation')
        subscription = request.POST.get('subscription')
        created_id = request.POST.get('created_id')
        
        studentInfo = StudentInfo(id=id, name=name, email=email, contact=contact, 
                        password=password,user_type=user_type, 
                        school_division=school_division,status=status,cgpa=cgpa,official_id=official_id,designation=designation,
                        subscription=subscription,created_id=created_id)
        studentInfo.save()
        return HttpResponse('<p>Data save Successfully!</p>')
    else:
        return render(request, 'userlogin.html')
