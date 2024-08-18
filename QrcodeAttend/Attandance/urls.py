from django.urls import path
from .import views

urlpatterns=[
    path('qrcode/',views.qrcodegeneration,name='Attandance-qrcodegeneration'),
    path('generate-qr-code/', views.generate_qr_code, name='generate-qr-code'),

    path('studentattendance/', views.studentattendance, name='student-attendance'),
    path('submit-attendance/', views.submit_attendance, name='submit-attendance'),
]