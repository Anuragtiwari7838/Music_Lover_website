from email import message
from unicodedata import name
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout as auth_logout
from django.http import HttpResponse
from django.shortcuts import redirect,HttpResponse
from django.shortcuts import render
from musicbeats.models import Song,watchlater,History
from django.contrib import messages
from django.contrib.messages import constants



def history(request):
    if request.method == "POST":
        user=request.user
        music_id=request.POST['music_id']
        history= History(user=user,music_id=music_id)
        history.save()
        
        return redirect(f"/musicbeats/songs/{music_id}")

    return render(request, 'musicbeats/history.html')


def watchlater(request):
    
    if request.method == "POST":
        user=request.user
        video_id=request.POST['video_id']
        
        watchlater = watchlater.objects.filter(user=user,video_id=video_id)
        watchlater.save()
        return render(request,f"/musicbeats/songs/{video_id}")

    return render(request,"musicbeats/watchlater.html")

def index(request):
    song = Song.objects.all()
    return render(request, 'index.html' , {'song': song})

def songs(request):
    song = Song.objects.all()
    return render(request,'musicbeats/songs.html' , {'song': song})

def singer(request):
    song = Song.objects.all()
    return render(request,'musicbeats/singer.html' , {'song': song})

def dhillon(request):
    song = Song.objects.all()
    return render(request,'musicbeats/dhillon.html' , {'song': song})

def neha(request):
    song = Song.objects.all()
    return render(request,'musicbeats/neha.html' , {'song': song})

def sonu(request):
    song = Song.objects.all()
    return render(request,'musicbeats/sonu.html' , {'song': song})

def songpost(request,id):
    song = Song.objects.filter(song_id=id).first()
    return render(request,'musicbeats/songpost.html' , {'song': song})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        if user is not None:
            from django.contrib.auth import login
            login(request,user)
            messages.success(request,"successfully logged in")
            redirect('/')
        else:
            messages.success(request,"Invalid Credenials,Please try again")
            redirect('/')

    return render(request,'musicbeats/songpost.html')


def logout(request):
    auth_logout(request)
    messages.success(request,"Successfully logged out")
    return redirect('/')

    return render(request,'musicbeats/logout.html')

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        first_name = request.POST["firstname"]
        last_name = request.POST["lastname"]
        email = request.POST['email']
        pass1 = request.POST['pass1']
        
        myuser = User.objects.create_user(username,email,pass1)
        myuser.first_name=first_name
        myuser.last_name=last_name
        myuser.save()
        user=authenticate(username=username,password=pass1)
        from django.contrib.auth import login
        login(request,user)

        return redirect('/')

    return render(request,'musicbeats/songpost.html')

def search(request):
    query=request.GET['query']
    allsong = Song.objects.filter(name__icontains=query)
    params = {'allsong':allsong}
    return render(request,'musicbeats/search.html',params)
    

       
