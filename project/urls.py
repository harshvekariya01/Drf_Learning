from django.contrib import admin
from django.urls import path,include
# from rest_framework import routers
# from members.views import studentviewset,Professionviewset

# router = routers.DefaultRouter()
# router.register('studentviewset', studentviewset,basename="student"),
# router.register('Professionviewset', Professionviewset,basename="Profession")





urlpatterns = [
    # path('api/', include(router.urls)), 
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('',include("members.urls"))

    
]
