from django import forms
from .models import Lectures

class LecturesForm(forms.ModelForm):
    class Meta:
        model = Lectures
        fields = ['course', 'lecture_no', 'lecture_na', 'pdf', 'ppt', 'word', 'video']