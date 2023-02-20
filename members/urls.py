from django.urls import path
from . import views

urlpatterns = [
    path('studentviewset/<id>',views.studentviewset.as_view({'get':'list','put':'update','post':'create','patch':'update','delete':'destroy'})),

    path('Professionviewset/',views.Professionviewset.as_view({'get':'list','put':'update','post':'create','patch':'update','delete':'destroy'}))

]