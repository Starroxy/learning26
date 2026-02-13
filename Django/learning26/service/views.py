from django.shortcuts import render,redirect,HttpResponse
from .form import serviceform
from .models import serivce
# Create your views here.

def servicelist(request):
    list=serivce.objects.all().order_by('id')
    return render(request,"service/servicelist.html",{"list":list})

def CreateService(request):
    if request.method == "POST":
        form = serviceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("servicelist")
    else:
        form = serviceform()
    return render(request, "service/service.html", {"form": form})

def updateservice(request,id):
    service=serivce.objects.get(id=id)
    if request.method == "POST":
        form = serviceform(request.POST,instance=service)
        if form.is_valid():
            form.save()
            return redirect("servicelist")
    else:
        form = serviceform(instance=service)
    return render(request, "service/service.html", {"form": form})

def deleteservice(request,id):
    service=serivce.objects.get(id=id)
    service.delete()
    return redirect("servicelist")