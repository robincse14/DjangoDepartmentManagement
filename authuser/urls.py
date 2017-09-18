from django.conf.urls import url

from . import views

urlpatterns=[
    url('^AuthUserHome/$',views.AuthUserHome,name='AuthUserHome'),
    url('^AuthUserHome/signout/$',views.signout,name='signout'),
    url('^addfaculty/$',views.addfaculty,name='addfaculty'),
    url('^deletefaculty/$',views.deletefaculty,name='deletefaculty'),
    url('^deletefaculty/vali/$',views.deletefacultyvali,name='deletefacultyvali'),
    url('^deletestudent/$',views.deletestudent,name='deletestudent'),
    url('^deletestudent/vali/$',views.deletestudentvali,name='deletestudentvali'),
    url('^viewstudent/$',views.viewstudent,name='viewstudent'),
    url('^viewfaculty/$',views.viewfaculty,name='viewfaculty'),
    url('^viewstudent/vali/$',views.viewstudentvali,name='viewstudentvali'),
    url('^viewfaculty/vali/$',views.viewfacultyvali,name='viewfacultyvali'),
    url('^viewinfo/$',views.viewinfo,name='viewinfo'),
]


