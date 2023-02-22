from django.urls import path
from . import views
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('studentviewset/',views.studentviewset.as_view({'get':'list','put':'update','post':'create','patch':'update','delete':'destroy'})),

    path('Professionviewset/',views.Professionviewset.as_view({'get':'list','put':'update','post':'create','patch':'update','delete':'destroy'})),
    path('api_token_auth/',obtain_auth_token), 
         


]