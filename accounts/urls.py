from django.urls import path
from . import views

urlpatterns = [
    path('signup-account/', views.signup_account, name='signup-account'),
    path('logout/', views.logout_account, name='logout-account'),
    path('login/', views.login_account, name='login-account'),
]
