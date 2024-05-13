"""
URL configuration for travelsite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myjob.views import city_job, catjobs, createJob, jobDetail, updateJob, delete_job


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mytravel.urls') ),
    path('', include('account.urls') ),
    


    path('city/<id>/', city_job, name='city-job'),
    path('category/<id>/', catjobs, name='job-cats'),
       
    path('<id>/job_detail/', jobDetail, name='job-detail'),
    path('update-job<id>/', updateJob, name='job-update'),
    path('delete-job/<id>/', delete_job, name='delete-job'),
    path('', include('myjob.urls') ),
]
