from django.urls import path
from users import views as user_views
from django.contrib.auth import views as auth_views
from users import views as user_views

urlpatterns = [
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/Userlogin.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/Userlogout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
]