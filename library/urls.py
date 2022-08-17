from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('', views.top, name='top'),
    path('upload/', views.upload, name="upload"),
]