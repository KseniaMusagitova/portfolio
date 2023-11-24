from django.shortcuts import render
from .models import Project, Contact
from django.http import HttpResponse

def home(request):
    projects = Project.objects.all()

    context = {
        'projects': projects,
    }

    if request.method=="POST":
        contact = Contact()
        email = request.POST.get('email')
        name = request.POST.get('name')
        message = request.POST.get('message')
        contact.email=email
        contact.name=name
        contact.message=message
        contact.save()

    return render(request, 'base/home.html', context)
