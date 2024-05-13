from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
# Register your models here.
from django.contrib import admin
from .models import EducationalLevel, Jobs, \
    JobCategory,\
        JobAdmin, \
            EmploymentType, \
                CareerLevel, \
                    MonthlySalary, \
                        EducationalLevel, \
                            City



class JobListFoamAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }



admin.site.register(City)
admin.site.register(Jobs, JobListFoamAdmin)
admin.site.register(JobCategory)
admin.site.register(JobAdmin)
admin.site.register(EmploymentType)
admin.site.register(CareerLevel)
admin.site.register(MonthlySalary)
admin.site.register(EducationalLevel)

