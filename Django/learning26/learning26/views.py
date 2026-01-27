from django.http import HttpResponse
from django.shortcuts import render

def test(request):
    return HttpResponse("hello")
def ContactUs(request):
    return render(request,"contactus.html")
def Homepage(request):
    return render(request,"Home.html")
def AboutUs(request):
    return render(request,"About.html")
def Movies(request):
    return render(request,"movies.html")
def shows(request):
    return render(request,"shows.html")
def news(request):
    return render(request,"news.html")
