from django.contrib import admin
from django.urls import path
from payment import views

urlpatterns = [
    path('',views.payment,name='payment'),
    path('netbanking/',views.netbanking,name='netbanking'),
    path('bhim/',views.bhim,name='bhim'),
    path('mobilebanking/',views.mobilebanking,name='mobilebanking'),
    path('cradit/',views.cradit,name='cradit'),
]