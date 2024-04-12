from django.urls import path
from . import views
app_name='comment'
urlpatterns = [
    path('inbox/',views.inbox,name="inbox"),
    path('details/<int:pk>',views.details,name="details"),
    path('comment/<int:pk>',views.comment,name="comment"),
]
