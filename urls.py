"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
# myproject/urls.py
from django.contrib import admin
from django.urls import path
from resume_app import views
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.resume_form, name='resume_form'),
    path("", include("resume_app.urls")), 
    path('preview/<int:resume_id>/', views.resume_preview, name='resume_preview'),
]
