
from django.contrib import admin
from django.urls import path, include
from porfolio.views import home, about
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('about/', about, name="about"),
    path('projects/', include("projects.urls"), name="projects"),
]

urlpatterns += staticfiles_urlpatterns()

