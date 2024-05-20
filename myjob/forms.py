from django import forms
from django.db.models import fields
from django.forms import TextInput
from ckeditor.widgets import CKEditorWidget
from crispy_forms.helper import FormHelper

from .models import Jobs


class JobListForm(forms.ModelForm):

# for crispy forms
    def __init__(self, *args, **kwargs):
        super(JobListForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_show_labels = True 

        
    # for ckeditor
    job_description = forms.CharField(widget=CKEditorWidget())

    class Meta:


        model = Jobs
        # select the field we need in the create form

        fields = ['application_link', 'company_name',\
            'company_logo', 'hide_company_name', 'job_title',\
                'job_description', 'gender', 'location', 'nationality',\
                    'career_level', 'employment_type', 'remote', \
                        'years_of_experience', 'educational_level', 'skill_set1', \
                            'skill_set2', 'skill_set3', 'cv_required', \
                                'category', 'city']

        widgets = {
        'title': forms.TextInput(attrs={"type":"text", "class":"form-control", "placeholder":"Title", "aria-label":"Title"}),
        'description': forms.Textarea(attrs={"class":"form-control", "placeholder":"Description", "aria-label":"Description"}),
        'image': forms.FileInput(attrs={"class":"form-control", "accept":"image/*"}),
        'advice_location': forms.Select(attrs={"class":"form-control"})
    }
    