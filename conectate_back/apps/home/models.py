from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    technicalDetails = models.CharField(max_length=100)
    description = models.TextField()
    keyWords = models.CharField(max_length=100)
    associatedProjects = models.TextField() #texto rico - html
    examplesAndActivities = models.TextField() #texto rico - html
    pedagogicStrategy = models.CharField(max_length=100) # mas adelante deberia ir a una tabla con todas las estrategias
    officialDocs = models.CharField(max_length=100)
    associatedTutorials = models.TextField() #debe incluir el enlace al ejemplo

