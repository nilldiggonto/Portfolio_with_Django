from django.shortcuts import render
from .models import Skill

# Create your views here.
def home(request):
    return render(request,'info/home.html')


def all_skills(request):
    skills = Skill.objects.all
    context= {
        'skills':skills,
        'value':80,
    }
    return render(request,'info/skill.html',context)