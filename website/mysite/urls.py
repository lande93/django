from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path('love/', views.love, name='love'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout')

]
