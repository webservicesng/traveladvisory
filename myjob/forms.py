from django import forms
from django.db.models import fields
from django.forms import TextInput
from ckeditor.widgets import CKEditorWidget


from .models import Jobs


class JobListForm(forms.ModelForm):
    
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


