from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('studentviewset/<int:id>',views.studentviewset.as_view({'get':'retrieve','update':'put','post':'create','patch':'update','delete':'destroy'})),

    path('Professionviewset/<int:id>',views.Professionviewset.as_view({'get':'retrieve','put':'update','post':'create','patch':'update','delete':'destroy'}))

]