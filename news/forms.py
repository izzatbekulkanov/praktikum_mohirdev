from django.forms import ModelForm
from .models import Project

class AddAboutForm(ModelForm):
    class Meta:
        model = Project
        fields = '__all__'