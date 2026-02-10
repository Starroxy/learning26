from django.shortcuts import render
from .models import employee
# Create your views here.
def employeelist(request):
    emp=employee.objects.all().values()
    emp1=employee.objects.all().values_list()
    print("emp",emp)
    print("emp1",emp1)
    return render(request,"employee/employee.html",{'emp':emp})

def employeefilter(request):
    emp=employee.objects.all().values()
    emp2=employee.objects.filter(age__exact=23).values()
    emp3=employee.objects.filter(post="Data Scientist").values()
    emp4=employee.objects.filter(salary__gt=29000).values()
    emp5=m=employee.objects.filter(name__icontains="It").values()
    emp6=employee.objects.filter(age__range=(25,30)).values()
    emp7=employee.objects.order_by("salary").values()
    print("emp2",emp2)
    print("emp3",emp3)
    print("emp4",emp4)
    print("emp5",emp5)
    print("emp6",emp6)
    print("emp7",emp7)

    return render(request,"employee/employee.html",{'emp':emp})