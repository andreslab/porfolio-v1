from django.shortcuts import render
from projects.models import Project
#from projects.models import project_info

def gallery_projects(request):
    projects = Project.objects.all().order_by('created')
    return render(request, 'projects/gallery.html', {
        "projects" : projects
    })

def detail_project(request, name):
    #project = project_info("Andreslab", "dev group")
    return render(request, 'projects/detail.html')

def contact_projects(request, name):
    return render(request, 'projects/contact.html')
