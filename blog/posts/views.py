from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Location, Employee, Device
from .forms import DeviceForm
from django.db.models import Count
from datetime import date
import datetime
from django.http import HttpResponse


def welcome_view(request):
    now = datetime.datetime.now()
    html = f"""
        <html><body>
        Witaj użytkowniku! </br>
        Aktualna data i czas na serwerze: {now}.
        </body></html>"""
    return HttpResponse(html)


# Widoki listy
def category_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})

def location_list(request):
    locations = Location.objects.all()
    return render(request, 'location_list.html', {'locations': locations})

def employee_list(request):
    employees = Employee.objects.all()
    return render(request, 'employee_list.html', {'employees': employees})

def device_list(request):
    devices = Device.objects.all()
    return render(request, 'device_list.html', {'devices': devices})

# Szczegóły jednego urządzenia
def device_detail(request, pk):
    device = get_object_or_404(Device, pk=pk)
    return render(request, 'device_detail.html', {'device': device})

# Edycja urządzenia
def device_edit(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        form = DeviceForm(request.POST, instance=device)
        if form.is_valid():
            form.save()
            return redirect('device_detail', pk=device.pk)
    else:
        form = DeviceForm(instance=device)
    return render(request, 'device_edit.html', {'form': form})

# Usunięcie urządzenia
def device_delete(request, pk):
    device = get_object_or_404(Device, pk=pk)
    if request.method == "POST":
        device.delete()
        return redirect('device_list')
    return render(request, 'device_delete.html', {'device': device})

# Widok dodatkowy: lista urządzeń w danej kategorii
def devices_by_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    devices = Device.objects.filter(category=category)
    return render(request, 'devices_by_category.html', {'devices': devices, 'category': category})

# Widok dodatkowy: urządzenia przypisane do danego pracownika
def devices_by_employee(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    devices = Device.objects.filter(assigned_to=employee)
    return render(request, 'devices_by_employee.html', {'devices': devices, 'employee': employee})


