from django.conf.urls import include,url
from . import views

urlpatterns = [
    url(r'^$',views.home,name='student_home'),
    url(r'^list_json/$', views.student_list_json.as_view(), name="student_list_json"), #utk papar list student bila guna url .../list_json
    url(r'^home/$',views.home_json,name='student_home_json'),   #utk papar page home
    url(r'^sbadmin/$',views.home_sbadmin,name='student_home_sbadmin'),   #utk papar page sbadmin
]