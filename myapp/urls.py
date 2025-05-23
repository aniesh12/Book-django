from django.urls import URLPattern

from django.urls import path
from . import views


urlpatterns=[
    path('',views.home,name='home'),
    path('send/',views.send,name='send'),
    path('data/',views.ListView,name='data'),
    path('upadte/<int:pk>/',views.Upadte,name='upadte'),
    path('book/<int:pk>/delete/', views.delete_it, name='delete_it'),
]