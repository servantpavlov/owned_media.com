from django.urls import path
from . import views

app_name = 'library'

urlpatterns = [
    path('upload/', views.upload, name='upload'),
    path('detail/<int:pk>/', views.book_detail, name='book_detail'),
    path('', views.book_list, name='book_list'),
]