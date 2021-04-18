from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    return render(request, 'main/home.html')

def register(request):
    form = UserCreationForm()

    #when submit is clicked / when creating new user
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form' : form}
    return render(request, 'main/register.html', context)

def login(request):
    context = {}
    return render(request, 'main/login.html', context)
