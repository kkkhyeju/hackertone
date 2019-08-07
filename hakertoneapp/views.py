from django.shortcuts import render , redirect, get_object_or_404
from django.contrib.auth.models import User
from django.utils import timezone
from django.contrib import auth
from .models import Team
from .models import Question
# Create your views here.

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password2']:
            user = User.objects.create_user(username= request.POST['username'], password = request.POST['password'])
            auth.login(request, user)
            return redirect('index')
    return redirect('index')

def login(request):
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(request, username=username , password = password)
            if user is not None and username == "kimhyeju":
                auth.login(request,user)
                return render(request,'ad_page.html')
            elif user is not None:
                auth.login(request,user)
                return render(request,'index.html')    
            else:
                return redirect('index')
        else:
            return redirect('index')

# def delete(request, account_id):
#         account = Account.objects.get(id=account_id)
#         account.delete()
#         return redirect('index')

def loginhome(request):
    return render(request,'login.html')

def maketeam(request):
	return render(request,'maketeam.html')

def findteam(request):
	return render(request,'maketeam.html')
    
def index(request):
    return render(request,'index.html')
    
def ad_page(request):
    questions = Question.objects
    return render(request,'ad_page.html',{'questions':questions})
    #return render(request,'ad_page.html')

def create(request):
    question = Question()
    question.title = request.GET['title']
    question.body = request.GET['body']
    question.save()
    return redirect('ad_page')