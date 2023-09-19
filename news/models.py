import uuid
from django.db import models
from django.utils.translation import gettext as _

# Create your models here.
# class ReviewBallManager(models.Manager):
#     def get_queryset(self):
#         return super().get_queryset().filter(rewiew=Review.Vote.yaxshi)

class Project(models.Model):
    title = models.CharField(_("Nomi"), max_length=200)
    description = models.TextField(_("Izoh"),)
    image = models.ImageField(_("Rasm"), upload_to='images/', null=True, blank=True, default='images/Apple.png')
    joined = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    creator = models.ForeignKey('Creator', on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = 'Telefonlar'
        verbose_name_plural = 'Telefonlar'

    def __str__(self):
        return self.title
class Review(models.Model):
    VOTE_TYPE = (
        ("+", "yaxshi"),
        ("-", "yomon")
    )
    project = models.ForeignKey(Project, on_delete=models.CASCADE, null=True, blank=True, related_name = "project_review")
    value = models.CharField(max_length=50, choices=VOTE_TYPE)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)
    body = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Ball'
        verbose_name_plural = 'Ball'

    def __str__(self):
        return self.project.title
class Creator(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(unique=True, primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        verbose_name = 'Yaratuvchi'
        verbose_name_plural = 'Yaratuvchilar'

    def __str__(self):
        return self.name
