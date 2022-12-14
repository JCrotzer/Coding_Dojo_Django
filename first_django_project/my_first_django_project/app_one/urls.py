from django.urls import path     
from . import views

urlpatterns = [
    path('', views.root),
    path('blogs', views.index),	
    path('blogs/new', views.new), 
    path('blogs/create', views.create),
    path('blogs/<num>', views.show),
    path('blogs/<num>/edit', views.edit),
    path('blogs/<num>/delete', views.destroy),
    path('redirected_route', views.redirected_method)
]