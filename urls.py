from django.contrib import admin
from django.urls import path
from resume_app import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home / Resume Form
    path('', views.resume_form, name='resume_form'),

    # Preview page with optional template choice
    path('resume/<int:resume_id>/', views.resume_preview, name='resume_preview'),

    # PDF download
    path('download_pdf/<int:resume_id>/', views.download_resume_pdf, name='download_resume_pdf'),
]
