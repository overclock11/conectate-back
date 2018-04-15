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


class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    objective = models.TextField(null=True)
    url =  models.URLField(max_length=400)
    tool = models.ForeignKey(Tool, null=True, on_delete=models.CASCADE)


class Strategy(models.Model):
    name = models.CharField(max_length=100)


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Example(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    state = models.CharField(max_length=100)
    strategy = models.ForeignKey(Strategy, null=False, on_delete=models.CASCADE, related_name='examples')
    discipline = models.ForeignKey(Discipline, null=False, on_delete=models.CASCADE, related_name='examples')


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    example = models.ForeignKey(Example, null=False, on_delete=models.CASCADE, related_name='resources')
