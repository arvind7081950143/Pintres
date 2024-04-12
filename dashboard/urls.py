from django.urls import path
from . import views
app_name='dashboard'
urlpatterns = [
    path('dashboard/',views.dashboard,name='dashboard'),
    path('new/',views.new,name='new'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('profile/',views.profile,name='profile'),

    path('profile_user/',views.profile_user,name='profile_user'),
    path('edit_profile/',views.edit_profile,name='edit_profile'),
]