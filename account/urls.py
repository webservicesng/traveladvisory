

from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static




app_name = 'account'


urlpatterns = [
    path('dashboard/', views.user_dashbaord, name='userdashboard_' ),

    path('register/', views.register_user, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout')
    
    
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

