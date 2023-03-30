from django import forms

from .models import apply , Job

class ApplyForm(forms.ModelForm):
    class Meta:
        model=apply
        fields=['name','email','website','cv','cover_letter']

class Addjob(forms.ModelForm):
    class Meta:
        model=Job
        fields='__all__'
        exclude=('owmer','slug')