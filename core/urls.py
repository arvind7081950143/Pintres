from django.urls import path
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from . import views
app_name='core'
urlpatterns = [
    path('',views.index,name='index'),
    path('brows/',views.brows,name='brows'),
    path('login/',views.login,name='login'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('inbox/',views.contact_inbox,name='contact_inbox'),
    path('logout/',views.logout,name='logout'),
    path('singnup/',views.singnup,name='singnup'),
    path('details/<int:pk>',views.details,name='details'),
]
