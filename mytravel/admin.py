from django.contrib import admin
from django.db import models
from ckeditor.widgets import CKEditorWidget
from .models import TravelAdvice,\
    TourService, JobListing,\
    Application, Location, Category,\
    Country



class TravelAdviceAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {'widget': CKEditorWidget},
    }



admin.site.register(TravelAdvice, TravelAdviceAdmin)
admin.site.register(TourService)
admin.site.register(JobListing)
admin.site.register(Location, TravelAdviceAdmin)
admin.site.register(Category)
admin.site.register(Application)
admin.site.register(Country)