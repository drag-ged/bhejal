from django_urls import include,path
from . import views
from django.contrib import admin

urlspatterns = [path('',include('bhejal.urls')),path('admin/',admin.site.urls),]

urlspatterns = [path('jason/',views.view_json,name='view_json')]
