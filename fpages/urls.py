from django.urls import path
from . import views


urlpatterns = [
    path('',views.tim,name='tim'),
    path('bnl/',views.bnl,name='bnl'),
    path('sofia/',views.sofia,name='sofia'),
    path('upload/',views.upload,name='upload'),
    path('uploaded/<int:num>/',views.uploaded,name='uploaded'),
    path('uploaded/',views.uploaded,name='uploaded'),
]