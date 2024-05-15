from django import forms
from .models import Reports, Signup



class NewsletterForm(forms.ModelForm):
    class Meta:
        model = Signup
        fields = ['email']
        widgets= {"email":forms.TextInput(attrs={"type":"email", "name" :'email', "class":"form-control", "placeholder":"Enter your email", "aria-label":"email"})}


class ContactForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = ['name', 'email', 'message']
        widgets={'name':forms.TextInput(attrs={"type":"text", "name" :'name', "class":"form-control", "placeholder":"name", "aria-label":"name"}),
                 'email':forms.TextInput(attrs={"type":"email", "name" :'email', "class":"form-control", "placeholder":"email", "aria-label":"email"}),
                 'message':forms.Textarea(attrs={"type":"textarea", "name" :'message', "class":"form-control", "placeholder":"message", "aria-label":"with textarea"}),
                 
                 }
        