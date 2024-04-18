from django.shortcuts import render
from enroll.models import User
# Create your views here.


def userinfo(request):
    stud=User.objects.all()
    return render(request,'enroll/userdetails.html',{'stu':stud})
