from django.http import HttpResponse
from django.template import Context, Template
from django.shortcuts import render

def home(request):
    
    projects = [
       """ project_info("Andreslab 1", "dev group"),
       project_info("Andreslab 2", "dev group"),
       project_info("Andreslab 3", "dev group"),
       project_info("Andreslab 4", "dev group"),
   """  ]

    news = [
    ]

    """ page = open("../porfolio/templates/home.html")
    template = Template(page.read())
    page.close() 
    context = Context({
        "title":"home",
        "projects": projects,
        "news": news
    })
    return HttpResponse(template.render(context))
    """

    return render(request, "home.html") 


def about(request):
    return render(request, "about.html")