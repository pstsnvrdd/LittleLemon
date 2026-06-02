from django.urls import path
from .views import *

urlpatterns = [
    path('menu-items/', MenuView.as_view(), name='menu-items'),
    path('menu-items/<int:pk>', MenuDetailView.as_view()),
    path('message/', msg),
    path('', index, name='index')
]