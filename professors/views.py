from django.shortcuts import render, redirect
from .models import * 

from .forms import ClassForm
from django.http import HttpResponseRedirect
from django.utils.crypto import get_random_string


# Create your views here.
#admin homepage
def dashboard(request, pk):
    prof = Professor.objects.get(id=pk)
    context = {'prof': prof}
    return render(request, 'professors/dashboard.html', context)

#creating class
def create_class(request, pk):
    prof = Professor.objects.get(id=pk)
    unique_id = get_random_string(length=10)
    id = int(pk)

    form = ClassForm(initial={'professor_id':prof.id, 'unique_code':unique_id})
    if request.method == 'POST': 
        form = ClassForm(request.POST)  
        if form.is_valid():
            form.save()
            #redirect with <str> url
            return HttpResponseRedirect('/professors/%d/' % id)

    context = {'prof':prof, 'form':form}
    return render(request, 'professors/create_class.html',context)

#view class list
def view_classes(request, pk):
    prof = Professor.objects.get(id=pk)
    #fetching all data with a particular key
    show_classes = Class.objects.filter(professor_id=pk)
    
    context={'prof': prof, 'show_classes':show_classes}
    return render(request, 'professors/view_classes.html', context)

#show class details
def show_class(request, pk, class_id):
    prof = Professor.objects.get(id=pk)
    current_class = Class.objects.get(id=class_id)
    #get info of a class
    class_info = Class.objects.filter(id=class_id)

    #filtering url access
    for infos in class_info:
        prof_id = infos.professor_id
     
    context={'prof': prof, 'current_class':current_class, 'class_info':class_info}

    #filtering url access
    if prof_id == pk:
        return render(request, 'professors/show_class.html', context)

#show students of a class
def show_students(request, pk, class_id):
    prof = Professor.objects.get(id=pk)
    current_class = Class.objects.get(id=class_id)


    context={'prof': prof, 'current_class':current_class}
    return render(request, 'professors/show_students.html', context)

#show feeds of professor per subject
def show_feed(request, pk, class_id):
    prof = Professor.objects.get(id=pk)
    current_class = Class.objects.get(id=class_id)

    context={'prof': prof, 'current_class':current_class}
    return render(request, 'professors/show_feed.html', context)

#show students of a class
def show_class_settings(request, pk, class_id):
    prof = Professor.objects.get(id=pk)
    current_class = Class.objects.get(id=class_id)
    #get info of a class
    class_info = Class.objects.filter(id=class_id)

    form = ClassForm(instance=current_class)
    
    id = int(pk)
    if request.method == 'POST':
        form = ClassForm(request.POST, instance=current_class)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/professors/%d/' % id)

    context={'prof': prof, 'current_class':current_class, 'class_info':class_info, 'form':form}
    return render(request, 'professors/show_class_settings.html', context)