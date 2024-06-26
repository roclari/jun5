from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('evento/<int:evento_id>/', views.details, name='details'),
    path('evento/criar/', views.create, name='create'),
    path('evento/<int:evento_id>/editar/', views.edit, name='edit'),
    path('evento/<int:evento_id>/deletar/', views.delete, name='delete'),

    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),

    path('chat/', views.chat_view, name='chat'),
]
