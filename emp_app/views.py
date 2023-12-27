from django.shortcuts import render,HttpResponse
from emp_app.models import Employee,Role,Department

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    return render(request,'all_emp.html',{'emps':emps})

def add_emp(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        phone=request.POST['phone']
        Department=request.POST['dept']
        Role=request.POST['role']
        new_emp=Employee(first_name=first_name,last_name=last_name,salary=salary,bonus=bonus,phone=phone,Department=Department,Role=Role)
        new_emp.save()
        return HttpResponse('Employee Added successfully')

    elif request.method=='GET':
       return render(request,'add_emp.html')
    else:
        return HttpResponse('An exception occured')

def remove_emp(request):
    return render(request,'remove_emp.html')

def filter_emp(request):
    return render(request,'filter_emp.html')