from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('template/<int:template_id>/', views.template, name='template'),
]