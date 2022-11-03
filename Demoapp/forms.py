from django import forms

from Demoapp.models import todo


class todoForm(forms.ModelForm):
    class Meta:
        model = todo
        fields = "__all__"