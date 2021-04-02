from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
#custome
from Billing_System.views import home_screen_view
from django.contrib.auth import views as auth_views
from .views import (

					Registration_view,
					logout_view,
                    login_view,
                    account_view,
                    index,
                    home,
                    view_bill,
                    generate_bill,
                    calculate,
                    check_status,
                    status_pdf_view,
                    status_pdf_download,
                    utility,

                    
                    

)
from Billing_System import views


urlpatterns = [
    #url(r'home_view', home_screen_view,name="home"),
    url(r'^login_view/$', login_view,name='login'),
    url(r'^register/$',Registration_view,name="register"),
    url(r'^logout/$',logout_view,name="logout"),
    url(r'^account/$',account_view,name="account"),
    #password reset
    path('password_channge/done/',auth_views.PasswordChangeDoneView.as_view(template_name='registration/password_change_done.html'),name='password_change_done'),
    path('password_change/',auth_views.PasswordChangeView.as_view(template_name='registration/password_change.html'),name='password_change'),
    path('password_reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
    path('reset/<slug:uidb64>/<slug:token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),  

    #view bill
    path('view_bill/',view_bill,name='view_bill'), 
    path('generate_bill/',generate_bill,name='generate_bill'),
    #calculate
    path('utility/',utility,name='utility'), 
    path('calculate/',calculate,name='calculate'), 
    path('check_status/',check_status,name='status'), 
    path('status_pdf_download/<pk>/', status_pdf_download,name='status_pdf_download'),
    path('status_pdf_view/<pk>/', status_pdf_view,name='status_pdf_view'),

    #by utsav
    path("home/",views.index,name='home'),
     path("login_home/",views.home,name='login_home') 
]
