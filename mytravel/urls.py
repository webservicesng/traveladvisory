
from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static



app_name= 'mytravel'
urlpatterns = [
    path('', views.index, name = 'index'),
    path('travel_advice/', views.travel_advise, name = 'travel_advice'),
    path('travel_advice/<advice_id>', views.travel_advice_detail, name = 'advice'),
    path('destinations', views.destinations, name = 'destinations'),
    path('tour_services', views.tourServices, name = 'tour_services'),
    path('jobs', views.jobs, name = 'jobs'),
    path('about-us', views.aboutUs, name = 'about_us'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT )
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT )

