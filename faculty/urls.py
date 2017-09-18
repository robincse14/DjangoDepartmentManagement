from django.conf.urls import url

from . import views

urlpatterns=[
    url(r'^FacultyHome/$',views.FacultyHome,name='FacultyHome'),
    url(r'^FacultyHome/signout/$',views.signout,name='signout'),
    url(r'^profile/$',views.profile,name='profile'),
    url(r'^update/$',views.update,name='update'),
    url(r'^selectstud/$',views.selectedstud,name='selectstud'),
    url(r'^selectstud/vali/$',views.selectedstudvali,name='selectstudvali'),
    url(r'^selectstud/vali/change/$',views.change,name='change')
]



