from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.details, name='details'),
    path('evento/criar/', views.create, name='create'),
    path('evento/<int:evento_id>/editar/', views.edit, name='edit'),
    path('evento/<int:evento_id>/excluir/', views.delete, name='delete'),
]
