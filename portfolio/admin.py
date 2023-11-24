from django.contrib import admin
from .models import Project, Contact

class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'link']  

admin.site.register(Project, ProjectAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['email', 'name', 'message'] 

admin.site.register(Contact, ContactAdmin)