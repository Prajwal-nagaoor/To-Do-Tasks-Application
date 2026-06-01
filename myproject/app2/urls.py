from django.urls import path
from app2 import views

urlpatterns = [
    path('', views.login_, name='login_'),
    path('reg', views.reg, name='reg'),
    path('logout', views.logout_, name='logout'),
    path('profile', views.profile, name='profile'),
    path('reser_pass', views.reser_pass, name='reser_pass'),
    path('update_profile/<int:pk>', views.update_pro, name='update_pro'),
]   