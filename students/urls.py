from django.urls import path
from . import views


urlpatterns = [
    path('<str:pk>', views.home, name='student_home'),
    path('profile/<str:pk>', views.update_profile, name='user_profile'),
    path('enroll_class/<str:pk>', views.enroll_class, name='enroll_class')
]