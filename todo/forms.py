from django import forms
from .models import Task


class TaskUpdateForm(forms.ModelForm):
    title = forms.CharField(max_length=300)

    class Meta:
        model = Task
        fields = ("title",)
