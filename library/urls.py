from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('upload/', views.upload, name="upload"),
    path('', views.top, name='top'),
]