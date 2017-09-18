from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^student/signup/$',views.signup,name='signup'),
    url(r'^student/login/$',views.login,name='login'),
    url(r'^faculty/signup/$',views.facultysignup,name='facultysignup'),
    url(r'^faculty/signup/auth/$',views.AfterFacultySignup,name='AfterFacultySignup'),
    url(r'^student/signup/auth/$',views.AfterSignup,name='AfterSignup'),
    url(r'^student/login/auth/$', views.Afterlogin, name='Afterlogin'),
    url(r'^/$',views.home,name='home'),
    url(r'$',views.signout,name='signout'),



]


