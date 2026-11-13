from django.urls import path
from . import views 

urlpatterns = [

    path('', views.myapp),
    path('podex/api/', views.getData),
    path('podex/', views.podex)
]