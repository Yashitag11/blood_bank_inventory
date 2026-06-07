from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('success/', views.success_view, name='success'),
    path('records/', views.records_view, name='records'),
    path('edit/<str:pk>/', views.edit_view, name='edit'),
    path('delete/<str:pk>/', views.delete_view, name='delete'),
]