
from django.urls import path
from . import views




app_name = "myjob"

urlpatterns = [
    path('create-job', views.createJob, name="create-job"),
    path('jobview', views.jobhome, name="home"),
    
]


from django.conf import settings
from django.conf.urls.static import static


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )



