from django.urls import path
from .views import login_user, logout_user, register_user

urlpatterns = [
    path('login', login_user, name='login-view'),
    path('logout', logout_user, name='logout_user-view'),
    path('register', register_user, name='register_user-view')
]