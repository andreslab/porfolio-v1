from django.urls import path
from . import views

urlpatterns = [
    path('', views.gallery_projects, name="projects"),
    path('<name>/', views.detail_project, name="detail"),
    path('<name>/contact/', views.contact_projects, name="contact"),
]

