from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('vote/<str:pk>', views.vote, name='vote'),
    path('result/<str:pk>', views.result, name='result'),
    # path('links/<str:pk>', views.links, name='links')
]
