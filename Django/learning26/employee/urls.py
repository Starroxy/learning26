from django.urls import path
from . import views

urlpatterns = [
    path("employeelist/",views.employeelist),
    path("employeefilter/",views.employeefilter),
    path("createemployee/",views.createEmployee),
    path("createcourse/",views.createcourse),
    path("createcollege/",views.createcollege),
    path("createproduct/",views.createproduct)
]