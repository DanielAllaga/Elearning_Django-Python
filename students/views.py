from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.contrib import messages
from .forms import StudentForm
from .models import *

# Create your views here.
def home(request,pk):
    student = Student.objects.get(id=pk)
    enrolled = student.enroll_set.all()


    # class_enrolled = Enroll.objects.filter(student=student)
    context = {'student':student, 'enrolled': enrolled}
    return render(request, 'students/student_dashboard.html', context)

def update_profile(request,pk):
    student = Student.objects.get(id=pk)

    form = StudentForm()
    context = {'form':form, 'student': student}
    return render(request, 'students/user_profile.html',context)


def enroll_class(request,pk):

    student = Student.objects.get(id=pk)
    code = request.GET['class_code'] #GET CLASS CODE FROM TEMPLATE
    class_info = Class.objects.get(unique_code=code)
    class_exist = student.enroll_set.filter(class_enrolled=class_info)

    if class_exist:
        print("class already exist")
    else:
        new_enroll = Enroll(student=student, class_enrolled = class_info)
        new_enroll.save()

    id = int(pk)
    return HttpResponseRedirect('/students/%d' % id)

