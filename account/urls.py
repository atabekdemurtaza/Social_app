from django.urls import path, include
from . import views

urlpatterns = [
    # Предыдущий url входа
    #path('login/', views.user_login, name='login'),

    # url-адреса входа и выхода
    path('', include('django.contrib.auth.urls')),
    path('', views.dashboard, name='dashboard'),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    
]

