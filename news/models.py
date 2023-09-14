import uuid
from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='images/' ,null=True , blank=   True)
    joined = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True,primary_key=True,default=uuid.uuid4, editable=False)
    creator = models.ManyToManyField('Tag',blank=True)

    def __str__(self):
        return self.title
class Review(models.Model):
    VOTE_TYPE = (
        ('1', 'Yaxshi'),
        ('2', 'Yomon'),
        ('3', 'Alo'),
        ('4', 'Qoniqarli'),
        ('5', 'Qoniqarsiz'),
    )
    body = models.CharField(max_length=200)
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    id = models.UUIDField(unique=True,primary_key=True,default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True , blank=True)


    def __str__(self):
        return self.body
class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True,primary_key=True,default=uuid.uuid4, editable=False)

    def __str__(self):
        return self.name