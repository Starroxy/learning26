# Create your views here
from django.shortcuts import render,redirect,get_object_or_404
from .models import Student,service
from .form import StudentForm,ServiceForm
from django.contrib import messages

 
def marks(request):
    return render(request,"student/marks.html")

def info(request):
    data={"name":"sumit","std":"10th","DOB":10-5,"result":80}
    return render(request,"student/info.html",data)

def faculty(request):
    data={'sub1':'Maths','teacher1':'Dr. Meera Nair',"qual1":"Ph.D. Mathematics",
          'sub2':'English','teacher2':'Piyush Patel',"qual2":"M.A. English  Literatuer",
          'sub3':'Science','teacher3':'Harish singh',"qual3":"Msc. Physics"
          }
    return render(request,"student/faculty.html",data)


def studentlist(request):
    data=Student.objects.all().order_by('id')
    return render(request,"student/studentlist.html",{'data':data})

def creatprofile(request):
    if request.method=="POST":
        form=StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form=StudentForm()
    return render(request,"student/creatprofile.html",{'form':form})

def deleteprofile(request,id):
    Student.objects.filter(id=id).delete()
    return redirect('studentlist')

def updateprofile(request,id):
    student=Student.objects.get(id=id)
    if request.method=="POST":
        form=StudentForm(request.POST,instance=student)
        if form.is_valid():
            form.save()
            return redirect('studentlist')
    else:
        form=StudentForm(instance=student)
    return render(request,"student/creatprofile.html",{'form':form})

def servicelist(request):
    service_list=service.objects.all().order_by('id').values()
    return render(request,"student/servicelist.html",{'services':service_list})

def createservice(request):
    if request.method=="POST":
        form=ServiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('servicelist')
        else:
            return render(request,"student/createservice.html",{'form':form})
    else:
        form=ServiceForm()
    return render(request,"student/createservice.html",{'form':form})

def updateservice(request,id):
    update_service=service.objects.get(id=id)
    if request.method=="POST":
        form=ServiceForm(request.POST,instance=update_service)
        if form.is_valid():
            form.save()
            return redirect('servicelist')
    else:
        form=ServiceForm(instance=update_service)
    return render(request,"student/createservice.html",{'form':form})

def deleteservice(request,id):
   obj = get_object_or_404(service, id=id)
   obj.delete()
   messages.success(request,"Service deleted successfully!")
   return redirect('servicelist')

    