
from django.urls import path
from contact import views

urlpatterns = [
  
    path('reg/',views.reg),
    path('log/',views.log),
    path('prdv/',views.prdv),
    path('logm/',views.logm),
    path('g/',views.g),
    path('rdv/<str:nom>',views.rd),
    path('s/<int:pk>/',views.jj),
    path('rdm/<str:nom>',views.rdm),
    path('up/<int:pk>/',views.up),
    path('m/',views.m),
    path('msg/<str:n>',views.message),
    path('mm/',views.mm),
    path('msgm/<str:n>',views.messagem),
    path('em/<int:pk>/',views.em),
    path('pem/<int:pk>/',views.pem),
    path('nop/',views.nop),
    path('nom/',views.nom),
    path('gnm/<str:n>',views.gnm),
    path('gnp/<str:n>',views.gnp),
        
   




   
]






