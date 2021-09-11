from django import forms
from .models import Local


class LocalForm(forms.ModelForm):
   
    class Meta:
        model = Local
        fields = ('name', 'address', 'city','state','zipCode','photo_url','description','website',)

    resturaunt = forms.NullBooleanField()
    shopping = forms.NullBooleanField()
    social = forms.NullBooleanField()
        
