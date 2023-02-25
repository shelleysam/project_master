from django.conf.urls import url
from quickstart import views,views1,views2
from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    url(r'^test/$',views.testApi),
    url(r'^test/([0-9]+)$',views.testApi),
    url(r'^login/$',views.login),
    url(r'^loggedin/$',views.loggedin),
    url(r'^get_pdf/$',views.get_pdf),
    url(r'^file_upload/$',views.file_upload),
    url(r'^get_appl/$',views.get_appl),
    url(r'^for_appl/$',views1.for_appl),
    url(r'^view_appl/$',views1.view_appl),
    url(r'^accp_clerk/$',views1.accp_clerk),
    url(r'^rej_clerk/$',views1.rej_clerk),
    url(r'^sec_for_appl/$',views1.sec_for_appl),
    url(r'^sec_view_appl/$',views1.sec_view_appl),
    url(r'^sec_accp/$',views1.sec_accp),
    url(r'^sec_rej/$',views1.sec_rej),
    url(r'^esign/$',views2.employeesignup),
    url(r'^esign/([0-9]+)$',views2.employeesignup),
    url(r'^elogin/$',views2.employeelogin),
    url(r'^get_test1/$',views1.get_test1),
    url(r'^get_app_clerk/$',views1.get_app_clerk),
    url(r'^get_secapp/$',views1.get_secapp),
    url(r'^view_app/$',views2.view_app),
    url(r'^get_rej/$',views1.get_rej),
    url(r'^get_secaccp/$',views1.get_secaccp),
    url(r'^send_email/$',views2.send_email),
    url(r'^send_email1/$',views2.send_email1),
    url(r'^send_email2/$',views2.send_email2),
]
