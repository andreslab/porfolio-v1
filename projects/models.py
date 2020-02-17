from django.db import models

# Create your models here.
""" class project_info(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description """

class Project(models.Model):
    name = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    #en la shell devuelve el nombre del objeto representado por el "name"
    def __str__(self):
        return self.name

    def short_detail(self):
        return self.description[:50]

