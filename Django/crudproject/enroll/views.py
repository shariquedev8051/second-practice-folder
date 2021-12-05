from django.shortcuts import render , HttpResponseRedirect
from .forms import StudentRegistration
from .models import Extended_user
# Create your views here.

def add_show(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pw = fm.cleaned_data['password']
            reg = Extended_user(name =nm, email=em, password = pw)
            reg.save()
            fm = StudentRegistration()
            # fm.save()
    else:
        fm = StudentRegistration()
    stud = Extended_user.objects.all()

    return render(request, 'enroll/addandshow.html',{'form':fm,'stu':stud})


def delete_data(request ,id):
    if request.method == "POST":
        pi = Extended_user.objects.get(pk = id ) 
        pi.delete()
        return HttpResponseRedirect('/')


def update_data(request, id):
    if request.method == "POST":
        pi = Extended_user.objects.get(pk =id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid:
            fm.save()
    else:
        pi = Extended_user.objects.get(pk =id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'enroll/updatestudent.html' , {'form':fm})