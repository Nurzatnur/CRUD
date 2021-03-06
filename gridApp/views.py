from django.shortcuts import render, redirect
from gridApp.forms import EmployeeForm
from gridApp.models import Employee


def addnew(request):
    if request.method == "POST":
        form = EmployeeForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/')
            except:
                pass
    else:
        form = EmployeeForm()
    return render(request, 'gridApp/index.html', {'form': form})


def index(request):
    employees = Employee.objects.all()
    return render(request, "gridApp/show.html", {'employees': employees})


def edit(request, id):
    employee = Employee.objects.get(id=id)
    return render(request, 'gridApp/edit.html', {'employee': employee})


def update(request, id):
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(request.POST, instance=employee)
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'gridApp/edit.html', {'employee': employee})


def destroy(request, id):
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect("/")
