from django.urls import path

from . import views


urlpatterns = [
    path('studentviewset/',views.studentviewset.as_view({'get':'list'}),name='studentviewset'),
    # path('studentviewset/<int:id>',views.studentviewset.as_view({'get':'list'}),name='studentviewset')


]

