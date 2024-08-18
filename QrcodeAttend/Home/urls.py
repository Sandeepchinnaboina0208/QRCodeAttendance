from django.urls import path
from .import views

urlpatterns=[
    path('',views.home,name='home'),
    path('home/',views.home,name='Home-home'),
    path('login/',views.login,name='Home-login'),
    path('register/',views.register,name='Home-register'),
    path('home2/',views.home2,name='Home-home2'),
    path('contact/',views.contactus,name='Home-contactus'),
    path('about/',views.about,name='Home-about'),

    path('checklogin/',views.checklogin,name='checklogin'),
    path('addregister/',views.addregister,name='register'),
    path('contactsave/',views.contactsave,name='Home-contact'),
]