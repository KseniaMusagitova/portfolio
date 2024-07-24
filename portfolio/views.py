from django.shortcuts import render
from .models import Project, Contact
from django.http import HttpResponse

def home(request):
    projects = Project.objects.all()

    if request.method == "POST":
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        Contact.objects.create(email=email, name=name, message=message)

    context = {
        'projects': projects,
    }

    return render(request, 'base/index.html', context)