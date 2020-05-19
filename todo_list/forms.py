from django import forms
from .models import eventList

class eventForm(forms.ModelForm):
    class Meta:
        model = eventList
        fields = ['lastname','firstname','level','course','gender','event','completed','time']
class editForm(forms.ModelForm):
    class Meta:
        model = eventList
        fields = ['lastname','firstname','level','course','gender','event']