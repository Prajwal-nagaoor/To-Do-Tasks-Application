from django.urls import path
from app1 import views
urlpatterns = [
    path('home', views.home, name='home'),
    path('add', views.add, name='add'),
    path('add', views.save_add, name='save_add'),
    path('details/<int:pk>/', views.details, name='details'),
    path('delete_/<int:pk>/', views.delete_, name='delete_'),
    path('completed/<int:pk>/', views.completed, name='completed'),
    path('uncompleted/<int:pk>/', views.uncompleted, name='uncompleted'),
    path('restore/<int:pk>/', views.restore, name='restore'),
    path('history', views.history, name='history'),
    path('comppleted', views.comppleted, name='comppleted'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete_hist/<int:pk>/', views.delete_hist, name='delete_hist'),
    path('clear_all', views.clear_all, name='clear_all'),
    path('restore_all', views.restore_all, name='restore_all')

]