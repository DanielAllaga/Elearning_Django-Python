from django.urls import path
from . import views

urlpatterns = [
    path('<str:pk>/', views.dashboard, name='professor_dashboard'),
    path('<str:pk>/create_class', views.create_class, name='professor_create_class'),
    path('<str:pk>/view_classes', views.view_classes, name='professor_view_classes'),
    path('<str:pk>/view_classes/<str:class_id>/', views.show_class, name='professor_show_class'),
    path('<str:pk>/view_classes/<str:class_id>/show_students', views.show_students, name='professor_show_students'),
    path('<str:pk>/view_classes/<str:class_id>/show_feed', views.show_feed, name='professor_show_feed'),
    path('<str:pk>/view_classes/<str:class_id>/show_class_settings', views.show_class_settings, name='professor_show_class_settings'),
]