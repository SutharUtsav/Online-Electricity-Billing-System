from django.contrib import admin
from django.urls import path
from .views import (
				generate_bill_view,
				render_pdf_view,
				render_pdf_download,
				render_pdf_delete,

			)

urlpatterns = [
    path('view/', generate_bill_view,name='view'),
    path('render_view/<pk>/', render_pdf_view,name='render_pdf_view'),
    path('render_download/<pk>/', render_pdf_download,name='render_pdf_download'),
    path('render_pdf_delete/<pk>/', render_pdf_delete,name='render_pdf_delete'),

]
