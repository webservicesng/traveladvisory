from django import forms
from .models import TravelAdvice


class TravelAdviceForm(forms.ModelForm):
    class Meta:
        model = TravelAdvice
        fields = ('title', 'description', 'image', 'advice_location')

        widgets = {
        'title': forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Title", "aria-label":"Title"}),
        'description': forms.Textarea(attrs={"class":"form-control", "placeholder":"Description", "aria-label":"Description"}),
        'image': forms.FileInput(attrs={"class":"form-control", "accept":"image/*"}),
        'advice_location': forms.Select(attrs={"class":"form-control"})
    }

        # widgets={
        #          'first_name':forms.TextInput(attrs={"type":"text", "class":"form-control ",'name':'last_name', "placeholder":"Last name", "aria-label":"Last name"}),
        #          'last_name':forms.TextInput(attrs={"type":"text", "class":"form-control ",'name':'last_name', "placeholder":"Last name", "aria-label":"Last name"}),
        #          'username':forms.TextInput(attrs={"type":"text", "class":"form-control ",'name':'username', "placeholder":"Username", "aria-label":"Username"}),
        #          'email':forms.TextInput(attrs={"type":"email", "class":"form-control ",'name':'email', "placeholder":"email", "aria-label":"email"}),
        #          'password1':forms.TextInput(attrs={"type":"password", "class":"form-control ", 'name':'password1', "placeholder":"password", "aria-label":"password"}),
        #          'password2':forms.TextInput(attrs={"type":"password", "class":"form-control ", 'name':'password2', "placeholder":" re-enter password", "aria-label":"password comfirmation"})
        #          }
        