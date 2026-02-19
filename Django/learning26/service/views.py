from django.shortcuts import render,redirect,HttpResponse
from .form import serviceform
from .models import serivce
# Create your views here.

def service_list(request):
    list=serivce.objects.all().order_by('id')
    return render(request,"service/service_list.html",{"list":list})

def create_service(request):
    if request.method == "POST":
        form = serviceform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("service_list")
    else:
        form = serviceform()
    return render(request, "service/service.html", {"form": form})

def update_service(request,id):
    service=serivce.objects.get(id=id)
    if request.method == "POST":
        form = serviceform(request.POST,instance=service)
        if form.is_valid():
            form.save()
            return redirect("service_list")
    else:
        form = serviceform(instance=service)
    return render(request, "service/service.html", {"form": form})

def delete_service(request,id):
    service=serivce.objects.get(id=id)
    service.delete()
    return redirect("service_list")