from django import forms
from django.contrib.admin.widgets import AdminDateWidget

from .models import Event


class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'type', 'date', 'place', 'memo']
        widgets = {
                    'name': forms.TextInput(attrs={'placeholder': '例：多摩川練習'}),
                    'type': forms.RadioSelect(),
                    'date': AdminDateWidget(),
                    'place': forms.TextInput(attrs={'placeholder': '例：多摩川コート'}),
                    'memo': forms.Textarea(attrs={'rows': 6}),
                  }
