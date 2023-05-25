from django.urls import path
from . import views
from .views import save_and_convert

urlpatterns = [
    path('', views.home, name='home'),
    path('template/<int:template_id>/', views.template, name='template'),
    path('save_and_convert/', save_and_convert, name='save_and_convert'),
]