from django.db import models

# Create your models here.
class Tool(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    url_site = models.CharField(max_length=120, default='', null=True)
    url_download = models.CharField(max_length=300, default='')
    usage_restrictions = models.CharField(max_length=1000, default='')
    license_type = models.CharField(max_length=100, default='Abierta')
    version = models.CharField(max_length=100, default='1.0')
    key_words = models.CharField(max_length=100, default='')
    state = models.CharField(max_length=100, default='')
    integration_lms = models.CharField(max_length=100, default='', null=True)


class PedagogicStrategy(models.Model):
    name = models.CharField(max_length=100, null=True)



class Tutorial(models.Model):
    name = models.CharField(max_length=100)
    objective = models.TextField(null=True)
    url =  models.URLField(max_length=400)
    tool = models.ForeignKey(Tool, null=True, on_delete=models.CASCADE, related_name='tutorials')


class Discipline(models.Model):
    name = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True)



class Example(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    instructions = models.TextField()
    state = models.CharField(max_length=100)
    pedagogic_strategy = models.ForeignKey(PedagogicStrategy, null=False, on_delete=models.CASCADE, related_name='examples')
    discipline = models.ForeignKey(Discipline, null=False, on_delete=models.CASCADE, related_name='examples')
    tool = models.ForeignKey(Tool, null=True, on_delete=models.CASCADE, related_name='examples')


class Resource(models.Model):
    name = models.CharField(max_length=100)
    link = models.URLField()
    example = models.ForeignKey(Example, null=False, on_delete=models.CASCADE, related_name='resources')
