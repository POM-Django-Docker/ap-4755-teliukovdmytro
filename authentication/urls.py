from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register_user'),
    path('login/', views.login_user, name='login_user'),
    path('logout/', views.logout_user, name='logout_user'),

    path('users/', views.user_list, name='user_list'),
    path('users/<int:user_id>/', views.user_detail, name='user_detail'),
]
