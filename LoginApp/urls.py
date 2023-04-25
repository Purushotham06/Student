from django.urls import path

from LoginApp import views

urlpatterns=[
    path('',views.home,name='home'),
    path('login',views.login_fun,name='login')

]