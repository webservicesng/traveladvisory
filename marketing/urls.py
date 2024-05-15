
from django.urls import path
from . import views




app_name = "myjob"

urlpatterns = [
    path('contact_form', views.contact_form, name="contact"),
    path('signup', views.Signup, name="subscript"),
    
]


# from django.conf import settings
# from django.conf.urls.static import static


# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
#     urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )



