from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('studentviewset/',views.studentviewset.as_view({'get': 'list'})),
    
    path('Professionviewset/',views.Professionviewset.as_view({'post': 'create'})),

    

    
]