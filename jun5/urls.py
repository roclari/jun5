from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('templates/details/', views.details, name='details'),
    path('templates/create/', views.create, name='create'),
    path('templates/edit/', views.edit, name='edit'),
    path('templates/delete/', views.delete, name='delete'),
]
