from django.conf.urls import url

from . import views

urlpatterns=[
    url('^StudHome/$',views.StudHome,name='StudHome'),
    url('^StudHome/signout/$',views.signout,name='signout'),
    url('^profile/$',views.profile,name='profile'),
    url('^update/$',views.ProfileUpdate,name='ProfileUpdate'),
    url('^viewinfo/$',views.info,name='info'),
    url('^enrolled/$',views.EnrolledCourses,name='EnrolledCourses'),
    url('^completed/$',views.completed,name='completed')
]


