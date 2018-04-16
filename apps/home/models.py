from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    urlSite = models.CharField(max_length=120, default='', null=True)
    urlDownload = models.CharField(max_length=300, default='')
    usageRestrictions = models.CharField(max_length=1000, default='')
    licenseType = models.CharField(max_length=100, default='Abierta')
    version = models.CharField(max_length=100, default='1.0')
    keyWords = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    integrationLms = models.CharField(max_length=100, default='', null=True)


class PedagogicStrategy(models.Model):
    name = models.CharField(max_length=100)


class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    objective = models.TextField(null=True)
    url =  models.URLField(max_length=400)
    tool = models.ForeignKey(Tool, null=True, on_delete=models.CASCADE)


class Discipline(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()


class Example(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    state = models.CharField(max_length=100)
    pedagogic_strategy = models.ForeignKey(PedagogicStrategy, null=False, on_delete=models.CASCADE, related_name='examples')
    discipline = models.ForeignKey(Discipline, null=False, on_delete=models.CASCADE, related_name='examples')

class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    example = models.ForeignKey(Example, null=False, on_delete=models.CASCADE, related_name='resources')
