from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib import messages



def index(request):
    me = Me.objects.get(id=1)
    skills = Skill.objects.all()
    projects = Project.objects.all()
    experiences = Experience.objects.all()
    educations = Education.objects.all()


    if request.method == 'POST':
        a = request.POST['name']
        b = request.POST['email']
        c = request.POST['message']

        Message.objects.create(name=a,email=b,discription=c)
        messages.success(request, "I got your message. I'll contact you as soon as possible. Thankyou for your interest")
        return redirect('index')
    for a in skills:
        a.time = (a.id * 2)
        a.save()
    last = skills.last().time + 2
    context = {
        'me':me,
        'skills':skills,
        'last':last,
        'projects':projects,
        'experiences':experiences,
        'educations':educations,
    }
    return render(request,'core/index.html',context)
