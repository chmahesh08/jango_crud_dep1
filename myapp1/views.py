from django.shortcuts import render

# Create your views here.

from myapp1.models import employee

def employee_details(request):
    data = employee.objects.all()
    context = {'data': data}
    return render(request, 'ap1_template/home.html', context)